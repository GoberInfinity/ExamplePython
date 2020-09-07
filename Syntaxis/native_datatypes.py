# -*- coding: utf-8 -*-

import fractions


# TODO: Add Ords
# - prioirity queue
# - Ordered Dict
def numerical_operations():
    """
    Common Numerical Operations
    """
    print(11 / 2)
    print(11 // 2)


def fraction():
    """
    Usage of Python fractions
    """
    x = fractions.Fraction(1, 3)
    print(x)


def lists():
    """
    Common List Operations
    The list can expand dinamically as new items are added
    """
    a_list = ["a", "b", "mpilgrim", "z", "example"]

    # Adding Items To A List See: http://www.diveintopython3.net/native-datatypes.html#extendinglists
    # the append() method takes a single argument, which can be any datatype.
    # Here, you’re calling the append() method with a list of three items.
    a_list.append(True)
    a_list.append(["g", "h", "i"])

    # The extend() method takes a single argument, which is always a list, and adds
    # each of the items of that list to a_list.
    a_list.extend(["d", "e", "f"])
    a_list.insert(0, "Ω")

    # Searching For Values In A List
    a_list.count("g")
    "new" in a_list

    # Removing Items From A List
    del a_list[1]
    a_list.remove("new")

    # removes the last item in the list
    a_list.pop()


def tuples():
    """
    A tuple is an immutable list. A tuple can not be changed in any way once it
    is created.
    Tuples are faster than lists. If you’re defining a constant set of values 
    and all you’re ever going to do with it is iterate through it, use a tuple 
    instead of a list.
    """
    a_tuple = ("a", "b", "mpilgrim", "z", "example")
    print(a_tuple)


def sets():
    """
    A set is an unordered “bag” of unique values.
    """
    a_list = ["a", "b", "mpilgrim", "z", "example"]
    b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
    a_set_2 = set(a_list)
    a_set = {1, 2}
    a_set.add(4)
    a_set.update([10, 20, 30])

    # 	The discard() method takes a single value as an argument and removes that
    # value from the set
    a_set.discard(21)

    # if the value doesn’t exist in the set, the remove() method raises a
    # KeyError exception.
    a_set.remove(21)
    a_set.discard(10)
    a_set.difference(b_set)


def dictionary():
    """
    It is best to think of a dictionary as an unordered set of key: value pairs
    with the requirement that the keys are unique (within one dictionary)
    """
    # Dictionaries
    a_dict = {"server": "db.diveintopython3.org", "database": "mysql"}
    # Modifying A Dictionary
    a_dict["database"] = "blog"
    colors = {"red": ["5"], "green": [""], "blue": ["0"]}
    colors.get("green", [])[0] or 0  # It's going to evaluate to 0
