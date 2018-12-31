class SingleTon(type):
    _instance = None
    def __call__(self, *args, **kwargs):
        print(self._instance)
        if self._instance is None:
            self._instance = super().__call__(*args, **kwargs)
        return self._instance

class SingleTonDecorator:
    def __init__(self, klass):
        self.klass = klass
        print(self.klass)
        self._instance = None

    def __call__(self, *args, **kwargs):
        print(self._instance)
        if self._instance is None:
            self._instance = self.klass(*args, **kwargs)
        return self._instance

@SingleTonDecorator
class MyClass():
    pass

a = MyClass()
b = MyClass()
a.name = "Hardik"
print(b.name)
print(a==b)