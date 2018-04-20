# -*- coding: utf-8 -*-
"""
Given two strings, write a method to decide if one is a permutation of the
other.

Hint: Is whitespace is significant?
"""
import unittest
from collections import Counter
 
def is_Permutation(f_string, s_string):
    f_string = sorted(f_string)
    s_string = sorted(s_string)
    return f_string == s_string

"""
def is_Permutation(f_string, s_string):
    if len(f_string) != len(s_string):
        return False
    counter = Counter()
    for c in f_string:
        counter[c] += 1
    for c in s_string:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True
"""

class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = is_Permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = is_Permutation(*test_strings)
            self.assertFalse(result)

unittest.main()
