# -*- coding: utf-8 -*-
"""
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function
to check if they are one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bae -> false
"""

import unittest

def is_one_edit(s1, s2):
    if len(s1) ==  len(s2):
        return is_edit(s1, s2)
    elif len(s1) + 1 == len(s2):
        return is_delete(s1, s2)
    elif len(s1) - 1 == len(s2):
        return is_delete(s2, s1)
    return False

def is_edit(first, second):
    is_different = False
    for (i, char) in enumerate(first):
        if first[i] != second[i]:
            if is_different:
                return False
            is_different = True
    return True 

def is_delete(s1, s2):
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if(i != j):
                return False
            j += 1
        else:
            i += 1
            j += 1
    return True 

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = is_one_edit(test_s1, test_s2)
            self.assertEqual(actual, expected)

print(unittest.main())
