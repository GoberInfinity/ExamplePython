a_list = [1, 9, 8, 4]
a_dict = {"a": 1, "b": 2, "c": 3}
a_set = set(range(10))

# Avoid using more than two expressions in a list comprehension.
# This could be two conditions, two loops, or one condition and one loop.
# As soon as it gets more complicated than that,
# you should use normal if and for statements

# The problem with list comprehensions is that they may create a whole new list
# containing one item for each value in the input sequence.
# This is fine for small inputs, but for large inputs this could consume memory
# and cause your program to crash.
# To avoid this behavior you can use a generator.

print([elem * 2 for elem in a_list])
print({value: key for key, value in a_dict.items()})
print({x ** 2 for x in a_set})
print({x for x in a_set if x % 2 == 0})
