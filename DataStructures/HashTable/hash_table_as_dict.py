# Built in data structure
empty_dict = dict()
non_empty_dict = {"key", "val"}

# Get a key from dict with a a default value if the key doesn't exist
empty_dict.get("non_existant_key", None)

# List comprehension to generate a dictionary
random_dict = {key: 0 for key in range(10)}

# Append element to a list that is a value in a dict
elements = {0: [0], 1: [0]}
(elements[0]).append(1)
