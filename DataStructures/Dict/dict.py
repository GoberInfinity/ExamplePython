# Built in data structure
# Avoid dictionaries that contain dictionaries
# It is relatively slower to initialize an empty dictionary by calling dict() than
# using the empty literal, because the name dict must be looked up in the global scope
# in case it has been rebound.
empty_dict = {}  # or dict()
non_empty_dict = {"key", "val"}

# Get a key from dict with a a default value if the key doesn't exist
empty_dict.get("non_existant_key", "default value")

# List comprehension to generate a dictionary
random_dict = {key: 0 for key in range(10)}

# Append element to a list that is a value in a dict
elements = {0: [0], 1: [0]}
(elements[0]).append(1)
