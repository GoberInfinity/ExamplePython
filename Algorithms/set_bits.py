"""
Given a number, tell number of bits set in the number in its binary
representation.
Note: Only works for positive numbers
"""


def numSetBits(number):
    counter = 0
    while number:
        counter += number & 1
        number >>= 1
    return counter


print(numSetBits(15))
