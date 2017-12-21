# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        solution = 0
        for num in nums:
            solution ^= num
        return solution
    
print(Solution().singleNumber([1,1,2,2,3,4,4]))