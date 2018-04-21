# -*- coding: utf-8 -*-
"""
Given a string, write a function to check if it is a permutation of
a palindrome. A palindrome is a word or phrase that is the same forwards and 
backwards. A permutation is a rearrangement of letters. The palindrome does not 
need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations:"taco cat'; "atco cta'; etc.)
"""
import unittest

def is_pal_perm(string):
    lookup_table = [0 for _ in range(ord('z') - ord('a') + 1)]
    odd_letters = 0
    
    for char in string:
        char_index = to_index(char)
        if char_index != -1:
            lookup_table[char_index] += 1
            if lookup_table[char_index] % 2:
                odd_letters += 1
            else:
                odd_letters -= 1
    return odd_letters <= 1

def to_index(c):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    val = ord(c)

    if a <= val <= z:
        return val - a
    elif A <= val <= Z:
        return val - A
    return -1

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = is_pal_perm(test_string)
            self.assertEqual(actual, expected)
            
print(unittest.main())
            