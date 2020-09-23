"""
Determine whether an integer is a palindrome. Do this without extra space.
"""


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    if 9 >= x > 0:
        return True
    reversed_number = 0
    while x > reversed_number:
        reversed_number = reversed_number * 10 + x % 10
        x //= 10
    return x in (reversed_number, reversed_number // 10)


print(isPalindrome(151))
