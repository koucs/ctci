#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest

# ctci.1_7
# Date: 2020/08/14
# Filename: 1_7 
# Author: koucs

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** -7
AtoZ = [chr(i) for i in range(65, 65 + 26)]
atoz = [chr(i) for i in range(97, 97 + 26)]


def zero_replace(matrix, col_length, row_length):
    bool_col = [False for i in range(col_length)]
    bool_row = [False for i in range(row_length)]

    for i in range(col_length):
        for j in range(row_length):
            if matrix[i][j] == 0:
                bool_col[i] = True
                bool_row[j] = True

    for i in range(col_length):
        for j in range(row_length):
            if bool_col[i] or bool_row[j]:
                matrix[i][j] = 0
    return matrix


class Test(unittest.TestCase):
    TEST_DATA = [
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
         ]),
        ([
             [1, 2],
             [3, 4],
             [0, 5]
         ], [
             [0, 2],
             [0, 4],
             [0, 0]
         ])
    ]

    def test_1(self):
        for in_data, expected_data in self.TEST_DATA:
            self.assertEqual(zero_replace(in_data, len(in_data), len(in_data[0])), expected_data)


if __name__ == '__main__':
    unittest.main()
