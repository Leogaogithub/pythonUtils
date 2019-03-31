import json

class Class1:
    def __init__(self):

        self.a = 'this'
        self.b = 33

    #def reprJSON(self):
        #return dict(a=self.a, b=self.b)

class Class2:
    def __init__(self):
        self.x = 'hello'
        self.y = Class1()
        self.z = 'world'

    #def reprJSON(self):

        #return dict(x=self.x, y=self.y, z=self.z)
        #return self.__dict__

class Class3:
    def __init__(self):
        self.m = 'leo'
        self.n = Class2()
        self.o = Class2()
        self.l = 238

    #def reprJSON(self):
        #return dict(m=self.m, n=self.n, o=self.o, l=self.l)
        #return self.__dict__

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        else:
            return json.JSONEncoder.default(self, obj)

if __name__ == '__main__':
    c = Class3()

#print(json.dumps(c, cls=ComplexEncoder, sort_keys=False, indent=2, separators=(',', ': ')))

#print(c.reprJSON())

def  divide_by_six(x):
    if x/6:
        return True
    else:
        return False

print(divide_by_six())