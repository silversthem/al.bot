class Predicat:
    # Creates a predicat
    def __init__(self,t,p):
        self.type = t
        self.parameter = p
        self.value = None
    # Checks if predicat is valid
    def is_complete(self):
        return self.value is not None
    # Sets predicat value if valid
    def set_value(self,v):
        pass
    # Parses to sql syntax
    def sql_query(self):
        pass
