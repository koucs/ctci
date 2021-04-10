#! env python
# -*- coding: utf-8 -*-

import unittest
from typing import List


# Cracking The Coding Interview (5th) q11_3
#
# Given a sorted array of n integers that has been rotated an unknown number of times,
# write code to find an element in the array.
# You may assume that the array was originally sorted in increasing order.
#
# EXAMPLE
# Input: find 5 in {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
# Output: 8 (the index of 5 in the array)

def find(arr: List, target: int) -> int:
    if arr[0] == target:
        return 0
    elif arr[0] > target:
        i = 1
        last = len(arr) - 1
        while i <= last:
            if arr[i] == target:
                return i
            i += 1
    else:
        i = len(arr) - 1
        last = 1
        while i >= last:
            if arr[i] == target:
                return i
            i -= 1


def find_text_solution(arr: List, target: int, left: int, right: int) -> int:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    # right を再帰的に mid-1 で指定する都合上, right < left となって無限ループになることを避けるための条件文
    if right < left:
        return -1

    if arr[left] < arr[mid]:
        if arr[left] <= target <= arr[mid]:
            return find_text_solution(arr, target, left, mid - 1)
        else:
            return find_text_solution(arr, target, mid + 1, right)
    elif arr[mid] < arr[right]:
        if arr[mid] <= target <= arr[right]:
            return find_text_solution(arr, target, mid + 1, right)
        else:
            return find_text_solution(arr, target, left, mid - 1)
    elif arr[left] == arr[mid]:
        if arr[left] != arr[right]:
            return find_text_solution(arr, target, mid + 1, right)
        else:
            left_result = find_text_solution(arr, target, left, mid - 1)
            return left_result if left_result != -1 else find_text_solution(arr, target, mid + 1, right)
    return -1


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5), 8)

        array = [55, 60, 65, 70, 75, 80, 85, 90, 95, 15, 20, 25, 30, 35, 40, 45]
        self.assertEqual(find(array, 55), 0)
        self.assertEqual(find(array, 60), 1)
        self.assertEqual(find(array, 90), 7)
        self.assertEqual(find(array, 95), 8)
        self.assertEqual(find(array, 15), 9)
        self.assertEqual(find(array, 30), 12)
        self.assertEqual(find(array, 45), 15)
        return

    def test_2(self):
        array = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
        self.assertEqual(find_text_solution(array, 5, 0, len(array) - 1), 8)

        array = [55, 60, 65, 70, 75, 80, 85, 90, 95, 15, 20, 25, 30, 35, 40, 45]
        self.assertEqual(find_text_solution(array, 55, 0, len(array) - 1), 0)
        self.assertEqual(find_text_solution(array, 60, 0, len(array) - 1), 1)
        self.assertEqual(find_text_solution(array, 90, 0, len(array) - 1), 7)
        self.assertEqual(find_text_solution(array, 95, 0, len(array) - 1), 8)
        self.assertEqual(find_text_solution(array, 15, 0, len(array) - 1), 9)
        self.assertEqual(find_text_solution(array, 30, 0, len(array) - 1), 12)
        self.assertEqual(find_text_solution(array, 45, 0, len(array) - 1), 15)

        array = [2, 2, 2, 3, 4, 2]
        # self.assertEqual(find_text_solution(array, 2, 0, len(array) - 1), 2)
        self.assertEqual(find_text_solution(array, 3, 0, len(array) - 1), 3)
        self.assertEqual(find_text_solution(array, 4, 0, len(array) - 1), 4)

        return


if __name__ == '__main__':
    unittest.main()
