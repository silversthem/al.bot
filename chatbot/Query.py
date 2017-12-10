from . import Predicat

def get_variance_dict():
    vrs = {'price':0,
    'OS':[0,0],
    'weight':0,
    'photo':0,
    'memory':0,
    'sim':[0,0,0],
    'battery_amp':0,
    'size':0,
    'moveable_battery':[0,0],
    'memory_upgrade':[0,0]}
    return vrs

def handle_variance(vrs,row,c):
    p = 1 if c % 2 is 1 else -1
    vrs['price'] += row[4]*p
    vrs['OS'][0 if row[3] is "Android" else 1] += 1
    vrs['weight'] += row[7]*p
    vrs['photo'] += row[12]*p
    vrs['memory'] += row[22]*p
    vrs['sim'][0 if row[18] == "compatiblecartenanoSIM" else 1 if row[18] == "compatiblecartemicro-SIM" else 2] += 1
    vrs['battery_amp'] += row[26]*p
    vrs['size'] += row[6]*p
    vrs['moveable_battery'][int(row[10])] += 1
    vrs['memory_upgrade'][int(row[23])] += 1


class Query:
    # Creates a query
    def __init__(self,db,preds = []):
        self.database = db
        self.predicats = preds
        self.most_variant = None
        self.cursor = None
        self.answer = None
        self.length = 0
    # Returns first row
    def get_answer(self):
        return self.answer
    # Adds a predicat to the array
    def add_predicat(self,pred):
        self.predicats.append(pred)
    # Runs the query
    def execute(self):
        self.cursor = self.database.cursor()
        rows = self.cursor.execute(self.sql_query())
        self.answer = self.cursor.fetchone()
        if self.answer is None: # No answer
            pass
        vrs = get_variance_dict()
        row = self.answer
        # Computing variances of parameters
        c = 0
        while row is not None:
            handle_variance(vrs,row,c)
            row = self.cursor.fetchone()
            c += 1
        self.length = c
        # Finding most variant
        self.most_variant = max(vrs,key=vrs.get)

    # Gets most varied parameter
    def get_most_variant(self):
        return self.most_variant
    # Turns predicat array into sql select query
    def sql_query(self):
        fr = ' FROM Phone JOIN Phys ON Phone.id = Phys.phone JOIN Camera ON Phone.id = Camera.phone JOIN Hardware ON Phone.id = Hardware.phone'
        if len(self.predicats) is 0:
            return 'SELECT *' + fr
        elif len(self.predicats) is 1:
            return 'SELECT *' + fr + ' WHERE ' + self.predicats[0].sql_query()
        else:
            q = 'SELECT *' + fr + ' WHERE ' + self.predicats[0].sql_query()
            for i in range(1,len(self.predicats)):
                if isinstance(self.predicats[i],Predicat.Predicat):
                    q += ' AND ' + self.predicats[i].sql_query()
            return q
