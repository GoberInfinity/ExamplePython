letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

# [start:end:step] start through not past end, by step

# Avoid using start, end, and stride together in a single slice.
# If you need all three parameters, consider doing two assignments
# (one to slice, another to stride)
# Slicing and then striding will create an extra shallow copy of the data.
# The first operation should try to reduce the size of the resulting slice
# as much as possible.
# If your program can’t afford the time or memory required for two steps,
# consider using islice from the itertools.
print(letters[:])  # Copy of the elements
print(letters[:5])  # [0, 5)
print(letters[:-1])  # [0, last)
print(letters[4:])  # [4, )
print(letters[-3:])  # [-3,)
print(letters[::-1])  # Reverse of the elements
