import Predicat

class Query:
    # Creates a query
    def __init__(self,db,preds = []):
        self.database = db
        self.predicats = pred
        self.most_variant = None
        self.cursor = None
        self.answer = None
    # Returns first row
    def answer(self):
        return self.answer
    # Adds a predicat to the array
    def add_predicat(self,pred):
        self.preds.append(pred)
    # Runs the query
    def execute(self):
        self.cursor = self.database.cursor()
        rows = self.cursor.execute(self.sql_query())
        self.answer = self.cursor.fetchone()
        if self.answer is None: # No answer
            pass
        vrs = {}
        row = self.answer
        # Computing variances of parameters
        while row is not None:
            # Computing for occurence of parameters
            row = self.cursor.fetchone()
        # Finding most variant


    # Gets most varied parameter
    def get_most_variant(self):
        return self.most_variant
    # Returns number of rows
    def length(self):
        return 0 if self.cursor is None else self.cursor.rowcount()
    # Turns predicat array into sql select query
    def sql_query(self):
        pass
