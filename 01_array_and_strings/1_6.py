#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest


# ctci.1_6
# Date: 2020/08/14
# Filename: 1_6 
# Author: koucs


def rotate_matrix(matrix, n):
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            offset = i - first
            # 上橋の値を保存
            top = matrix[first][i]
            # 左端 → 上橋
            matrix[first][i] = matrix[last - offset][first]
            # 下端 → 左端
            matrix[last - offset][first] = matrix[last][last - offset]
            # 右端 → 下端
            matrix[last][last - offset] = matrix[i][last]
            # 上端 → 右端
            matrix[i][last] = top
    return matrix


class Test(unittest.TestCase):
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

    def test_1(self):
        for in_data, expected_data in self.data:
            self.assertEqual(rotate_matrix(in_data, len(in_data)), expected_data)
        return


if __name__ == '__main__':
    unittest.main()
