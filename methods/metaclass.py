# method __new__
# method __call__

class A:
    def __init__(self, name):
        self.name = name
    def __new__(cls,name, *args, **kwargs):
        if name == 'amir':
            return None
        else:
            return super().__new__(cls, *args, **kwargs)
    def __call__(self, * args, ** kwargs):
        print(f'Hello {self.name}')

a = A('amir')
print(a)
print(a.__class__) # None type


b = A('ali')
b()
print(b.name)