import fractions

# TODO: Add Ords


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

    # http://www.diveintopython3.net/native-datatypes.html#extendinglists
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
