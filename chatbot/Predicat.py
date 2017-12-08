class Predicat:
    # Creates a predicat
    def __init__(self,t,p):
        self.type = t
        self.parameter = p
        self.value = None
    # Checks if predicat is valid
    def is_complete(self):
        return self.value is not None
    # Parses to sql syntax
    def sql_query(self):
        pass
