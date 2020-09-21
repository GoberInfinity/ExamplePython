"""
Given the array of IDs, which contains many duplicate integers and one unique integer,
find the unique integer.
Note: All integers except one appear exactly 2 times.
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


print(Solution().singleNumber([1, 1, 2, 2, 3, 4, 4]))
