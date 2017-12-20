# -*- coding: utf-8 -*-
"""
Given a number, tell number of bits set in the number in its binary 
representation. 
"""

class Solution:
    # @param number : int
    # @return an integer
    def numSetBits(number):
        counter = 0
        while number:
            counter += number & 1
            number >>= 1
        return counter

print(Solution().numSetBits(-15))