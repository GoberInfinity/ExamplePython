# -*- coding: utf-8 -*-
"""
Print all the subsets of a set
"""


class Solution:
    # @param A : array[int]
    # @return an array[array[int]]
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item + [num] for item in res]
        return res


print(Solution().subsets([1, 2, 3]))
