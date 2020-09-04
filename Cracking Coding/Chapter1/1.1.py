# -*- coding: utf-8 -*-
"""
Implement an algorithm to determine if a string has all unique characters.
You cannot use additional data structures.
Hint: Is the string an ASCII string or Unicode string?
"""
import unittest


def is_ASCII_string(string):
    if len(string) > 128:
        return False
    char_set = [False for _ in range(128)]
    for (i, char) in enumerate(string):
        if char_set[ord(char)]:
            return False
        char_set[ord(char)] = True
    return True


class Test(unittest.TestCase):
    dataT = [("abcd"), ("s4fad"), ("")]
    dataF = [("23ds2"), ("hb 627jh=j ()")]

    def test_unique(self):
        for test_string in self.dataT:
            actual = is_ASCII_string(test_string)
            self.assertTrue(actual)

        for test_string in self.dataF:
            actual = is_ASCII_string(test_string)
            self.assertFalse(actual)


unittest.main()
