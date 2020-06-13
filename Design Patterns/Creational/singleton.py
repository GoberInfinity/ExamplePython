"""
Ensure a class only has one instance, and provide a global point of
access to it.
"""


class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            #Calls the constructor of the class
            cls._instance = super().__call__(*args, **kwargs) 
        return cls._instance

# A metaclass is the class of a class. A class defines how an instance of the 
# class (i.e. an object) behaves while a metaclass defines how a class behaves.
class MyClass(metaclass=Singleton):
    """
    Example class.
    """

    def __init__(self):
        self.att = "Attribute"


"""
The expression MyClass() creates a new instance of class MyClass. 
When the interpreter encounters MyClass(), the following occurs:

1.The __call__() method of MyClass parent class is called. So type’s __call__() method is invoked.
2.That __call__() method in turn invokes the following: __new__(), __init__()
"""
m1 = MyClass()
m2 = MyClass()
print(m1 is m2)
