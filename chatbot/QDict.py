from . import Predicat

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
                return (q[1][0],q[1][2])
            else:
                return (q[0][0],q[0][1])
    # Transforms a user message in a predicat-type value, returns None if not possible
    def parse_message(self,t,message):
        message = message.lower()
        nb_int=0
        value=[]
        negative=False
        for word in message.split(" "):
            if word=="ne" or word=="non" or word=="pas" or word=="n'aime" or word=="hors":
                negative=True
        quantif=-1
        for word in message.split(' '):
            if negative and (word=='veux' or word=='aime' or word=='aimerai'):
                quantif=0
            elif word=='peu' or word=='rarement' or (word=='grave' and negative) or word=='occasionnellement' or (word=='pourquoi' and negative):
                quantif=0.33
            elif word=='souvent' or word=='surement' or word=='utile' or word=='envisageable' or word=='essayer'\
             or word=='j\'essayerai' or word=='essayerai':
                quantif=0.66
            elif word=='veux' or word=='absolument' or word=='necessaire' or word=='tres' or word=='vitale' or word=='':
                quantif=1
        if t == "fbool":
            if negative and quantif != -1:
                return 0*quantif
            elif not negative and quantif != -1:
                return 1*quantif
        elif t == "int":
            for word in message.split(' '):
                try:
                    value.append(int(word))
                    nb_int +=1
                except:
                    pass
            return value
        elif t == "union":
            union = []
            nb_union = 0
            for word in message.split(' '):
                if not negative:
                    if word=="ecran" or word=="tactile" or word=='amovible' or word=='batterie'\
                     or word=='flash' or word=='autofocus' or word=='4G' or word=='extension' or word=='memoire':
                        union.append(True)
                        nb_union+=1
                elif negative:
                    if word=="ecran" or word=="tactile" or word=='amovible' or word=='batterie'\
                    or word=='flash' or word=='autofocus' or word=='4G' or word=='extension' or word=='memoire':
                        union.append(False)
                        nb_union+=1
            return union
    # Turns an answer into a predicate
    def parse_answer(self,parameter,message,qcm = False):
        q = self.qbank.get(parameter,None) # Question bank entry
        if q is not None:
            t,v = (None,None)
            if qcm:
                t = q[1][2] # Type
                v = q[1][3][int(message)]
            else:
                t = q[0][1] # Type
                v = self.parse_message(t,message)
            p = Predicat.Predicat(parameter,t)
            p.set_value(v)
        return p
