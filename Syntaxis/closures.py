# Python supports closures: functions that refer to variables from the scope in which
# they were defined. This is why the helper function is able to access the group
# argument to sort_priority.


def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)

    values.sort(key=helper)


numbers_eg = [8, 3, 1, 2, 5, 4, 7, 6]
group_eg = {2, 3, 5, 7}
sort_priority(numbers_eg, group_eg)
# >>> [2, 3, 5, 7, 1, 4, 6, 8]

# In Python 3, there is special syntax for getting data out of a closure. The nonlocal
# statement is used to indicate that scope traversal should happen upon assignment for a
# specific variable name.
# The only limit is that nonlocal won’t traverse up to the modulelevel scope
# (to avoid polluting globals).


def sort_priority2(numbers, group):
    found = False

    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found


# However, much like the anti-pattern of global variables, I’d caution against using
# nonlocal for anything beyond simple functions. The side effects of nonlocal can be
# hard to follow.
# When your usage of nonlocal starts getting complicated, it’s better to wrap your state
# in a helper class.


class Sorter(object):
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)


sorter = Sorter(group_eg)
numbers_eg.sort(key=sorter)
assert sorter.found is True
