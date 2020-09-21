"""
Given an integer array, find three numbers whose product is maximum and output
the maximum product.
"""


class Solution:
    # @param A : List[int]
    # @return an integer
    def maximumProduct(self, nums):
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])


print(Solution().maximumProduct([-100, 10, 50, 63, 1, -10000]))
