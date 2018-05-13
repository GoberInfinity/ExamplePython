# -*- coding: utf-8 -*-
"""
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
            print(f"this is p {p} this is nums[i] {nums[i] }" )
        p = 1
        print(output)
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
            print(p)
        print(output)
        return output
    
Solution().productExceptSelf([1,2,3,4])