# A Counter is a dict subclass for counting hashable objects.
from collections import Counter

letters = Counter(["a", "b", "c", "a", "b", "b"])
# >>> Counter({'b': 3, 'a': 2, 'c': 1})
