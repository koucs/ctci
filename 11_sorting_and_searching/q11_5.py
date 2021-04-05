#! env python
# -*- coding: utf-8 -*-

import unittest
from typing import List


# Cracking The Coding Interview (5th) q11_5
#
# Given a sorted array of strings which is interspersed with empty strings,
# write a method to find the location of a given string.
#
# EXAMPLE
# Input: find "ball" in {"at", "", "", "", "ball", "", "", "car", "", "", "dad", "", "")
# Output: 4

def search(arr: List, search_str: str, first: int, last: int) -> int:
    mid = (first + last) // 2

    if arr[mid] is "":
        offset_left = mid - 1
        offset_right = mid + 1
        while True:
            if offset_left < first and last < offset_right:
                return -1
            elif first <= offset_left and arr[offset_left] is not "":
                mid = offset_left
                break
            elif offset_right <= last and arr[offset_right] is not "":
                mid = offset_right
                break
            offset_right += 1
            offset_left -= 1

    if arr[mid] == search_str:
        return mid
    elif search_str < arr[mid]:
        return search(arr, search_str, first, mid - 1)
    else:
        return search(arr, search_str, mid + 1, last)


class Test(unittest.TestCase):
    def test_1(self):
        arr = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
        self.assertEqual(4, search(arr, "ball", 0, len(arr) - 1))
        self.assertEqual(7, search(arr, "car", 0, len(arr) - 1))
        self.assertEqual(-1, search(arr, "bike", 0, len(arr) - 1))
        self.assertEqual(-1, search(arr, "", 0, len(arr) - 1))
        arr = ["apple", "", "", "banana", "", "", "", "carrot", "duck", "", "", "eel", "", "flower"]
        self.assertEqual(7, search(arr, "carrot", 0, len(arr) - 1))
        self.assertEqual(-1, search(arr, "ball", 0, len(arr) - 1))
        self.assertEqual(-1, search(arr, "apple pie", 0, len(arr) - 1))
        return


if __name__ == '__main__':
    unittest.main()
