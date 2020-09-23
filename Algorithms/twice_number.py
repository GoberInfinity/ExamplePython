"""
Given an array where every number in the range 1...n appears once except for
one number which appears twice. Write a function to find the number that
appears twice.
"""


def findDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)


print(findDuplicate([1, 2, 3, 3, 4, 5]))
