# -*- coding: utf-8 -*-
"""
N light bulbs are connected by a wire. Each bulb has a switch associated with 
it, however due to faulty wiring, a switch also changes the state of all the 
bulbs to the right of current bulb. Given an initial state of all bulbs, find 
the minimum number of switches you have to press to turn on all the bulbs. 
You can press the same switch multiple times.
Note : 0 represents the bulb is off and 1 represents the bulb is on.
Input : [0 1 0 1]
Return : 4

Explanation :
	press switch 0 : [1 0 1 0]
	press switch 1 : [1 1 0 1]
	press switch 2 : [1 1 1 0]
	press switch 3 : [1 1 1 1]
"""
class Solution:
    def bulbs(self,A):
        if not A:
            return 0
        n = 0
        status = 0
        for bulb in A:
            if bulb == status:
                n += 1
                status = int( not status)
        return n

class Solution2:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return []
        checkup = {}
        for i,num in enumerate(nums):
            complement = target - num
            if checkup.get(complement):
                return [checkup.get(complement),i]
            else:
                checkup = {num : i}
        return []
print(Solution2().twoSum([3,3],6))