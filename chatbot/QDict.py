import Predicat

QBank = {
    'parameter':[
        ["Question",'type'],
        ["QCM",['Option 1','Option 2'],'type',['Valeur 1','Valeur 2']]
    ]
}

class QDict:
    # Creates a Question Dictionnary
    def __init__(self,qbank):
        self.qbank = qbank
    # Returns a question to predicate a parameter
    def ask_for(self,parameter,qcm = False):
        q = self.qbank.get(parameter,None) # Question bank entry
        if q is not None:
            if qcm:
                return q[1][0]
            else:
                return q[0][0]
    # Transforms a message in a predicat-type value, returns None if not possible
    def parse_message(self,type,message):
        pass
    # Turns an answer into a predicate
    def parse_answer(self,parameter,message,qcm = False):
        q = self.qbank.get(parameter,None) # Question bank entry
        if q is not None:
            t,v = (None,None)
            if qcm:
                t = q[1][2] # Type
                v = q[1][3][message]
            else:
                t = q[0][2] # Type
                v = self.parse_message(t,message)
            p = Predicat(parameter,t)
            p.value = message
        return p
