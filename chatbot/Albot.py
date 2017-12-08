import Query
import QDict

# Creates a albot instance from a session
def create_bot(db,qdict,session_id):
    # Creating predicat array
    cursor = db.cursor()
    rows = cursor.execute('SELECT * FROM Session_Step WHERE session_id = ' + str(int(session_id)))
    preds = []
    if cursor.rowcount() > 0:
        for row in rows: # Fetching predicats
            parameter,predicat_type,value = row[4:7]
            p = Predicat(predicat_type,parameter)
            p.set_value(value)
            preds.append(p)
        # Returing new bot
        return Albot(int(session_id),db,qdict,preds)
    else:
        # Invalid session
        pass

# If an answer has been found
def state(db,session_id):
    cursor = db.cursor()
    rows = cursor.execute('SELECT answer FROM Session WHERE id = ' + str(int(session_id)))
    if rows.rowcount() > 0:
        answer = rows.fetchone()[1]
        if answer is not '':
            return (True,answer)
        else:
            return (False,'')
    else:
        return (False,'')

class Albot:
    # Creates a bot instance
    def __init__(self,s,db,qdict,predicats = []):
        self.db = db
        self.query = Query(db,predicats)
        self.current = current
        self.qdict = qdict
        self.session = s
    # Returns last question for a session
    def get_last_question(self):
        cursor = self.db.cursor()
        rows = cursor.execute('SELECT * FROM Session_Step WHERE session_id = ' + str(self.session) + 'ORDER BY id DESC LIMIT 1')
        return rows.fetchone()
    # Inserts answer for a question (updates sessions_steps table answer)
    def insert_answer(self,qid,message,pred_val):
        self.db.execute('UPDATE Session_Step SET answer = \"' + message + '\", value = \"' + pred_val + '\" WHERE id = ' + str(int(qid)))
        self.db.commit()
    # Handles an user answer, and returns either a phone or a new question
    def interact(self,message):
        q = self.get_last_question() # Pulling last question from database
        param = q[4] # Parameter in question
        pred = self.qdict.parse_answer(param,message)
        if pred.is_complete(): # Predicat is valid
            self.insert_answer(q[0],message,pred.value) # Inserting user answer in database
            self.query.add_predicat(pred)
            self.query.execute() # Running query
            if self.query.length() < 10: # Found answers
                return (1,'Answer')
            else: # New question
                self.ask(self.query.get_most_variant())
        else: # Predicat is not valid, calling for qcm question
            self.insert_answer(q[0],message,'')
            self.ask(param,qcm)
    # Inserts new question into database
    def ask(self,param,qcm = False):
        # Pulling question
        q = self.qdict.ask_for(param,qcm)
        # Inserting question
        qcm = '1' if qcm else '0'
        self.db.execute('INSERT INTO Session_Step VALUES (NULL,'+ str(self.session) +',\"' + q[0] + '\",\"\",\"' + param + '\",\"' + q[1] + '\",\"\",\"'+ qcm +'\")')
        self.db.commit()
