"""
Print all the subsets of a set
"""


def subsets(nums):
    res = [[]]
    for num in sorted(nums):
        res += [item + [num] for item in res]
    return res


print(subsets([1, 2, 3]))
