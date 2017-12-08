import Predicat

class Query:
    # Creates a query
    def __init__(self,db,preds = []):
        self.database = db
        self.predicats = pred
        self.most_variant = None
    def add_predicat(self,pred):
        self.preds.append(pred)
    # Runs the query
    def execute(self):
        pass
    # Gets most varied parameter
    def get_most_variant(self):
        return self.most_variant
    # Returns number of rows
    def length(self):
        pass
    # Turns predicat array into sql select query
    def sql_query(self):
        pass
