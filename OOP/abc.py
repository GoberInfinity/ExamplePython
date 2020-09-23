# The built-in collections.abc module defines a set of abstract base classes
# that provide all of the typical methods for each container type
# When you subclass from these abstract base classes
# and you forget to implement required methods
# the module will tell you something is wrong. (Like Hashable or Sequence)
# Inherit directly from Python's container types (like dict) for simple use cases

from collections.abc import Set


class FrequencyList(list):
    def __init__(self, members):
        super().__init__(members)

    def frequency(self):
        counts = {}
        for item in self:
            counts.setdefault(item, 0)
            counts[item] += 1
        return counts


foo = FrequencyList(["a", "b", "a", "c", "b", "a", "d"])
print(len(foo))
print(foo.frequency())


class ListSet(Set):
    def __init__(self, iterable):
        self.elements = lst = []
        for element in iterable:
            if element not in lst:
                lst.append(element)

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, value):
        return value in self.elements

    def __len__(self):
        return len(self.elements)


set1 = ListSet("ABCDEF")
set2 = ListSet("DEFGHI")
intersect = set1 & set2
