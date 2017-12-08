import Query
import QDict

# Creates a albot instance from a session
def create_bot(db,qdict,session_id):
    # Creating predicat array
    # Creating Albot
    pass

# If an answer has been found
def state(session_id):
    pass

class Albot:
    # Creates a bot instance
    def __init__(self,s,db,qdict,predicats = [],current = None):
        self.db = db
        self.query = Query(db,predicats)
        self.current = current
        self.qdict = qdict
        self.session = s
    # Returns last question for a session
    def get_last_question(self):
        pass
    # Inserts answer for a question (updates sessions_steps table answer)
    def insert_answer(self,qid,message):
        pass
    # Handles an user answer, and returns either a phone or a new question
    def interact(self,message):
        q = self.get_last_question() # Pulling last question from database
        self.insert_answer(q[0],message) # Inserting user answer in database
        param = q[4] # Parameter in question
        pred = self.qdict.parse_answer(param,message)
        if pred.is_complete(): # Predicat is valid
            self.query.add_predicat(pred)
            self.query.execute() # Running query
            if self.query.length() < 10: # Found answers
                return (1,'Answer')
            else: # New question
                return self.ask(self.query.get_most_variant())
        else: # Predicat is not valid, calling for qcm question
            return self.ask(param,qcm)
    # Returns new question
    def ask(self,param,qcm = False):
        return self.qdict.ask_for(param,qcm)
