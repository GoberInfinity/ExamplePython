a_list = ["a", "b", "mpilgrim", "z", "example"]
normal_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
set_from_list = set(a_list)
a_set = {1, 2}
a_set.add(4)
a_set.update([10, 20, 30])
# Takes a single value as an argument and removes that value from the set
a_set.discard(21)
# if the value doesn’t exist remove()  raises a KeyError exception.
a_set.remove(21)
a_set.difference(normal_set)
