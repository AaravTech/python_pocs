#!/usr/bin/python3
"""
This is baseclass for createing any singleton class.
"""
__author__ = "Hardik Patel"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Hardik Patel"
__email__ = "hnmpatel@live.com"
__status__ = "Production"


class SingleTon(type):
    """
    Usage - 
        class MyClass(metaclass=SingleTon):
            pass

        a = MyClass()
        b = MyClass()
        assert (a==b)
    """
    # Defining _instances dictionary for storing instances for each class
    # which has inherited this class and returning everytime same object
    # This class can be overwrriten by any class to create singleton class
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # Checking instance is still instance of same class
        if cls not in cls._instances:
            # Creating new instance if not created previously  
            cls._instances[cls] = super().__call__(*args, **kwargs)
        # returning same instance everytime
        return cls._instances[cls]

class MyClass:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if MyClass.__instance is None:
            MyClass.__instance = object.__new__(cls, *args, **kwargs)
        return MyClass.__instance

    def __init__(self, x):
        self.x = 10


if __name__ == "__main__":
    # class MyClass(metaclass=SingleTon):
    #     pass
    # Creating first object of SingleTon class obj1
    # and assign string "First object" to title attribute
    obj1 = MyClass()
    obj1.title = "First object"
    print(obj1.title)

    # Creating second object of SingleTon class obj2
    # and assign string "Second object" to title attribute
    obj2 = MyClass()
    obj2.title = "Second object"
    print(obj2.title)

    # Printing first object's title attribute which
    # is updated by second object as both the objects
    # are referring to same instance
    print(obj1.title)
    print(obj1==obj2)
