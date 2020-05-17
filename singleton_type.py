class Singleton(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class MyClass(metaclass=Singleton):
    pass


a = MyClass()
b = MyClass()
c = MyClass()
d = MyClass()
print(a)
print(b)
print(c)
print(d)
