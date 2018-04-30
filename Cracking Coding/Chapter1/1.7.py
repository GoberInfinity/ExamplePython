# -*- coding: utf-8 -*-
"""
Given an image represented by an NxN matrix, write a method to rotate the image 
by 90 degrees
"""
import unittest

def rotate_matrix(matrix):
    matrix = matrix[::-1]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j < i:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            else:
                continue
    return matrix 

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)
            
print(unittest.main())