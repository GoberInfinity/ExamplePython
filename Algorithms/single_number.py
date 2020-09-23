"""
Given the array of IDs, which contains many duplicate integers and one unique integer,
find the unique integer.
Note: All integers except one appear exactly 2 times.
"""


def singleNumber(nums):
    solution = 0
    for num in nums:
        solution ^= num
    return solution


print(singleNumber([1, 1, 2, 2, 3, 4, 4]))
