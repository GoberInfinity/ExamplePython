# The only time to seriously consider using private attributes is when you’re worried
# about naming conflicts with subclasses.
# This problem occurs when a child class unwittingly
# defines an attribute that was already defined by its parent class.
# This is primarily a concern with classes that are part of a public API
# the subclasses are out of your control


class ApiClass:
    def __init__(self):
        self.__value = 5

    def get(self):
        return self.__value


class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self.value = "hello"


a = Child()
print(f"{a.get()}, and, {a.value}, are different")
