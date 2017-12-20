# -*- coding: utf-8 -*-
"""
Given an 2D array, reverse the elements in each array 
"""
class Solution:
    # @param A : 2D array
    # @return an 2D array
    def reverse2D(self,A):
        n = len(A[0])
        B = []
        for i in range(len(A)):
            B.append([0] * n)
            for j in range(len(A[i])):
                B[i][n - 1 - j] = A[i][j]
        return B

print(Solution().reverse2D([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))