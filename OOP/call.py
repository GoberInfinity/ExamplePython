# Python allows classes to define the __call__ special method.
# __call__ allows an object to be called just like a function
# When you need a function to maintain state, consider defining a class that provides
# the __call__ method instead of defining a stateful closure


class BetterCountForDefaultDict:
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0


counter = BetterCountForDefaultDict()
counter()  # >>> counter.added = 1
