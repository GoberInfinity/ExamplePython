"""
Given an integer, reverse it.
"""


def reverse(number):
    if number == 0:
        return 0
    is_negative = False
    if number < 0:
        is_negative = True
        number = -number
    result = 0
    while number != 0:
        digit = number % 10
        number = number // 10
        result = result * 10 + digit
    if is_negative:
        return -result
    return result


print(reverse(-15))
