# -*- coding: utf-8 -*-
"""
Find the contiguous subarray within an array (containing at least one number) 
which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        max_far = nums[0]
        max_current = nums[0]

        for i in range(1, len(nums)):
            max_current = max(nums[i], nums[i] + max_current)
            max_far = max(max_far, max_current)
        return max_far
