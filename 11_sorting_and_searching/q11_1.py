#! env python
# -*- coding: utf-8 -*-

import unittest
from typing import List


# Cracking The Coding Interview (5th) q11_1
# You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B.
# Write a method to merge B into A in sorted order.

def merge(arr_a: List, arr_b: List) -> List:
    arr_b_idx = 0
    ans = [None for i in range(len(arr_a))]
    for i, v in enumerate(arr_a):
        while arr_b_idx < len(arr_b) and (v is None or v > arr_b[arr_b_idx]):
            ans[i + arr_b_idx] = arr_b[arr_b_idx]
            arr_b_idx += 1
        if (i + arr_b_idx) >= len(arr_a):
            break
        ans[i + arr_b_idx] = v
    return ans


class Test(unittest.TestCase):
    def test_1(self):
        a = [33, 44, 55, 66, 88, 99, None, None, None]
        b = [11, 22, 77]
        self.assertEqual(merge(a, b), [11, 22, 33, 44, 55, 66, 77, 88, 99])
        a = [11, 22, 55, 66, 88, None, None, None]
        b = [33, 44, 99]
        self.assertEqual(merge(a, b), [11, 22, 33, 44, 55, 66, 88, 99])
        a = [9, 10, 11, 12, 13, None, None, None, None]
        b = [4, 5, 6, 7]
        self.assertEqual(merge(a, b), [4, 5, 6, 7, 9, 10, 11, 12, 13])
        return


if __name__ == '__main__':
    unittest.main()
