def param2col(name):
    d = {'price':'price','OS':'os','weight':'weight','photo':'back_res','memory':'memory','sim':'type_sim','battery_amp':'battery_amp','size':'size','moveable_battery':'moveable_battery','memory_upgrade':'memory_upgrade'}
    return d.get(name)

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
    def set_value(self,v,from_db = False):
        if from_db and len(v) == 0:
            self.value = None
            return
        if from_db:
            if self.type == "union":
                self.value = v.split(',')
            elif self.type == "int":
                self.value = [int(k) for k in v.split(',') if k is not '']
            elif self.type == "fbool":
                self.value = float(v)
        else:
            self.value = v
    # Parses to sql syntax
    def sql_query(self):
        if self.value is not None:
            if self.type == "union":
                if len(self.value) is 0:
                    return '1'
                elif len(self.value) is 1:
                    return param2col(self.parameter) + ' = ' + str(self.value[0])
                else:
                    q = param2col(self.parameter) + ' = ' + str(self.value[0])
                    for i in range(1,len(self.value)):
                        q += ' OR ' + param2col(self.parameter) + ' = ' + str(self.value[i])
                    return q
            elif self.type == "int":
                if len(self.value) is 1: # Number
                    return param2col(self.parameter) + ' = ' + str(self.value[0])
                elif len(self.value) is 2: # Interval
                    return param2col(self.parameter) + ' BETWEEN ' + str(self.value[0]) + ' AND ' + str(self.value[0])
            elif self.type == "fbool":
                col = param2col(self.parameter)
                return col + ' >= MAX('+col+')*' + str(self.value)
        return '1'
