# -*- coding: utf-8 -*-
"""
Determine whether an integer is a palindrome. Do this without extra space.
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """        
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        if x > 0 and x <= 9:
            return True 
        
        reversed_number = 0
        while x > reversed_number:
            reversed_number = reversed_number * 10 + x % 10
            x //= 10
        return x == reversed_number or x == (reversed_number // 10)
    
print(Solution().isPalindrome(151))