# -*- coding: utf-8 -*-
"""
URLify: Write a method to replace all spaces in a string with '%2e: You may 
assume that the string has sufficient space at the end to hold the additional
characters
"""
from collections import deque


def urlify(string, length):
    new_index = len(string)

    for i in reversed(range(length)):
        if string[i] == " ":
            string[new_index - 3 : new_index] = "%20"
            new_index -= 3
        else:
            string[new_index - 1] = string[i]
            new_index -= 1

    return string


### Solution without length
""" 
def URLify(string):
    if not string:
        return ""
    result = deque()
    string = list(string)
    beginning_space = True 
    
    for char in string[::-1]:
        if char == " ":
            string.pop()
        else:
            break
    for char in string[::-1]:
        if char != " ":
            result.appendleft(char)
        else:
            result.appendleft("%20")
    print(''.join(result))
"""


class Test(unittest.TestCase):
    """Test Cases"""

    # Using lists because Python strings are immutable
    data = [
        (
            list("much ado about nothing      "),
            22,
            list("much%20ado%20about%20nothing"),
        ),
        (list("Mr John Smith    "), 13, list("Mr%20John%20Smith")),
    ]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)


unittest.main()
