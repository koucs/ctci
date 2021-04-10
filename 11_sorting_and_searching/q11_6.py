#! env python
# -*- coding: utf-8 -*-

import unittest
from typing import List, Tuple


# Cracking The Coding Interview (5th) q11_6
#
# Given an M x N matrix in which each row and each column is sorted in ascending order,
# write a method to find an element.

def partition(matrix: List, target: int, src: Tuple, mid: Tuple, dst: Tuple) -> Tuple:
    # lower_left partition
    result = search_from_matrix_bin(matrix, target, mid[0], dst[0], src[1], mid[1] - 1)
    if result != (-1, -1):
        return result
    # upper right partition
    return search_from_matrix_bin(matrix, target, src[0], mid[0] - 1, mid[1], dst[1])


def inbounds(matrix: List, row: int, col: int) -> bool:
    return (0 <= row < len(matrix)) and (0 <= col < len(matrix[0]))


def search_from_matrix_bin(matrix: List, target: int, r_left: int, r_right: int, c_left: int, c_right: int) -> Tuple:
    src = r_left, c_left
    dst = r_right, c_right

    if not inbounds(matrix, r_left, c_left) or not inbounds(matrix, r_right, c_right):
        return -1, -1
    if matrix[r_left][c_left] == target:
        return r_left, c_left
    if r_left > r_right or c_left > c_right:
        return -1, -1

    diag_dist = min(r_right - r_left, c_right - c_left)
    r_right = r_left + diag_dist
    c_right = c_left + diag_dist

    while r_left <= r_right and c_left <= c_right:
        r, c = (r_left + r_right) // 2, (c_left + c_right) // 2
        if target > matrix[r][c]:
            r_left = r + 1
            c_left = c + 1
        else:
            r_right = r - 1
            c_right = c - 1

    print(f"row: {src[0]}, col: {src[1]}, val: {matrix[src[0]][src[1]]}")
    print(f"row: {dst[0]}, col: {dst[1]}, val: {matrix[dst[0]][dst[1]]}")
    print()
    return partition(matrix, target, src, (r_left, c_left), dst)


def search_from_matrix(matrix: List, target: int) -> Tuple:
    if len(matrix) == 0:
        # Returns (-1, -1) if the target value was not found in matrix
        return -1, -1
    return search_from_matrix_bin(matrix, target, 0, len(matrix) - 1, 0, len(matrix[0]) - 1)


def search_text_solution1(matrix: List, target: int) -> Tuple:
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return row, col
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    return -1, -1


class Test(unittest.TestCase):
    mat1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
            [5, 10, 15, 20, 25, 30, 35, 40, 45],
            [10, 20, 30, 40, 50, 60, 70, 80, 90],
            [13, 23, 33, 43, 53, 63, 73, 83, 93],
            [14, 24, 34, 44, 54, 64, 74, 84, 94],
            [15, 25, 35, 45, 55, 65, 75, 85, 95],
            [16, 26, 36, 46, 56, 66, 77, 88, 99]]
    mat2 = [[15, 30, 50, 70, 73],
            [35, 40, 100, 102, 120],
            [36, 42, 105, 110, 125],
            [46, 51, 106, 111, 130],
            [48, 55, 109, 140, 150]]

    def test_1(self):
        self.assertEqual((2, 0), search_from_matrix(Test.mat1, 10))
        self.assertEqual((3, 0), search_from_matrix(Test.mat1, 13))
        self.assertEqual((4, 0), search_from_matrix(Test.mat1, 14))
        self.assertEqual((6, 0), search_from_matrix(Test.mat1, 16))
        self.assertEqual((4, 3), search_from_matrix(Test.mat1, 44))
        self.assertEqual((6, 4), search_from_matrix(Test.mat1, 56))
        self.assertEqual((5, 5), search_from_matrix(Test.mat1, 65))
        self.assertEqual((4, 6), search_from_matrix(Test.mat1, 74))
        self.assertEqual((6, 8), search_from_matrix(Test.mat1, 99))

        self.assertEqual((1, 1), search_from_matrix(Test.mat2, 40))

    def test_2(self):
        self.assertEqual((1, 1), search_text_solution1(Test.mat1, 10))
        self.assertEqual((3, 0), search_text_solution1(Test.mat1, 13))
        self.assertEqual((4, 0), search_text_solution1(Test.mat1, 14))
        self.assertEqual((6, 0), search_text_solution1(Test.mat1, 16))
        self.assertEqual((6, 4), search_text_solution1(Test.mat1, 56))
        self.assertEqual((5, 5), search_text_solution1(Test.mat1, 65))
        self.assertEqual((4, 6), search_text_solution1(Test.mat1, 74))
        self.assertEqual((6, 8), search_text_solution1(Test.mat1, 99))

        self.assertEqual((1, 1), search_text_solution1(Test.mat2, 40))

        return


if __name__ == '__main__':
    unittest.main()
