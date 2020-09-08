from itertools import islice

# Make an iterator that returns selected elements from the iterable.
# The parameters should be None or positive
# islice(iterable, start, stop[, step]) => iterator
list(islice([1, 2, 3, 4, 5, 6], None, 5, 2))

# If you need to reverse to use slice you can use reversed() that revers an iterator.
list(islice(reversed([1, 2, 3, 4, 5, 6]), None, None))
