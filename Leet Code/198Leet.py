# -*- coding: utf-8 -*-
"""
You are a professional robber planning to rob houses along a street. Each house 
has a certain amount of money stashed, the only constraint stopping you from 
robbing each of them is that adjacent houses have security system connected 
and it will automatically contact the police if two adjacent houses were broken
 into on the same night.

Given a list of non-negative integers representing the amount of money of each 
, determine the maximum amount of money you can rob tonight without alerting 
the police. 
"""

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev1, prev2, current = 0, 0, 0
        for num in nums:
            current = max(prev2 + num, prev1)
            prev2 = prev1
            prev1 = current
        return current
        
        """ Second approach
        answer = [0] * (len(nums)+2)
        for num in range(2,len(nums)+2): 
            answer[num] = max(nums[num-2] + answer[num-2], answer[num-1])
        return answer[len(nums)+1] """
