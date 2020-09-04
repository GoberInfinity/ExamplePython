# -*- coding: utf-8 -*-
"""
Given an array where every number in the range 1...n appears once except for 
one number which appears twice. Write a function to find the number that 
appears twice.
"""


class Solution:
    # @param nums : List[int]
    # @return an integer
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)


print(Solution().findDuplicate([1, 2, 3, 3, 4, 5]))
