# A mix-in is a small class that only defines a
# set of additional methods that a class should provide. Mix-in classes don’t define their
# own instance attributes nor require their __init__ constructor to be called.
# Avoid using multiple inheritance if mix-in classes can achieve the same outcome
# Compose mixins to create complex functionality from simple behaviors


class MyMixin:
    @classmethod
    def from_str(cls, number):
        return cls(int(number))

    def to_str(self):
        return f"str {str(self.number)}"


class MyClass(MyMixin):
    def __init__(self, number):
        self.number = number


my_object = MyClass.from_str("10")
print(my_object.to_str())
