import json

class Class1:
    def __init__(self):
        self.a = 'this'
        self.b = 33

class Class2:
    def __init__(self):
        self.x = 'hello'
        self.y = Class1()
        self.z = 'world'


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        else:
            return json.JSONEncoder.default(self, obj)

if __name__ == '__main__':
    a = Class2()

print(json.dumps(a, cls=ComplexEncoder, sort_keys=False, indent=2, separators=(',', ': ')))