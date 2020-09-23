# Metaclass is a class whose instances are classes
# (Classes are instances of metaclasses)
# You can gain leverage by modify the way that classes are produced by performing
# extra actions or injecting code.
# When this is the case, you can use metaclass programming to modify the way that some
# of your class objects are created.
# In the vast majority of cases, you don’t need metaclasses
# Info: https://ent1c3d.github.io/Python-Synopsis/site/advanced/Python_Metaclasses/


class Meta(type):
    def __new__(cls, name, bases, dct):
        # Delegates via super() to the __new__() method of the parent metaclass (type)
        # to actually create a new class
        new_class = super().__new__(cls, name, bases, dct)
        new_class.attr = 100
        # Returns the newly created class
        return new_class


class Sub(metaclass=Meta):
    pass


print(Sub.attr)  # noqa
