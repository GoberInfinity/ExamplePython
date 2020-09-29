from collections import defaultdict

# The functionality of both dictionaries and defaultdict are almost same
# except for the fact that defaultdict never raises a KeyError.
# It provides a default value for the key that does not exists.
# All that defaultdict requires is a function for the default value hook


def log_missing():
    print("Key added")
    return 0


current = {"green": 12, "blue": 3}
increments = [
    ("red", 5),
    ("blue", 17),
    ("orange", 9),
]
result = defaultdict(log_missing, current)
for key, amount in increments:
    result[key] += amount
# >>>
# Key added
# Key added
# After: {‘orange’: 9, ‘green’: 12, ‘blue’: 20, ‘red’: 5}

# When the list class is passed as the default_factory argument,
# then a defaultdict is created with default value for the key as a list.

default_as_list = defaultdict(list)

for i in range(5):
    default_as_list[i].append(i)
# >>> {0: [0], 1: [1], 2: [2], 3: [3], 4: [4]}
