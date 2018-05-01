# -*- coding: utf-8 -*-
"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row 
and column are set to 0.
"""
import unittest

def zero_matrix(matrix):
    columns = []
    rows = []
    
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == 0:
                rows.append(x)
                columns.append(y)
                
    for row in rows:
        nullify_row(matrix, row)

    for col in columns:
        nullify_column(matrix, col)

    return matrix

def nullify_row(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0
              
def nullify_column(matrix, column):
    for i in range(len(matrix)):
        matrix[i][column] = 0
              
class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

print(unittest.main())
     

        
                