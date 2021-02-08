#! env python
# -*- coding: utf-8 -*-

import unittest
from typing import List, Optional


# Date: 2021/01/19
# Author: koucs
#
# 9.3.
# A magic index in an array A[0...n-1] is defined to be an index such that A[i] = i.
# Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
#
# FOLLOW UP
# What if the values are not distinct?

def magic_index(l: List) -> Optional[int]:
    for i, v in enumerate(l):
        if i == v:
            return i
    return None


def magic_index_2(l: List) -> Optional[int]:
    idx = 0
    while idx < len(l):
        if idx == l[idx]:
            return idx
        idx = max(l[idx], idx + 1)
    return None


def magic_index_distinct(l: List, start: int, end: int) -> Optional[int]:
    if end < start or start < 0 or len(l) <= end:
        return None
    mid = (start + end) // 2
    if l[mid] == mid:
        return mid
    elif l[mid] < mid:
        return magic_index_distinct(l, mid + 1, end)
    else:
        return magic_index_distinct(l, start, mid - 1)


def magic_index_fast(l: List, start: int, end: int) -> Optional[int]:
    if end < start or start < 0 or len(l) <= end:
        return None

    mid_i = (start + end) // 2
    mid_v = l[mid_i]
    if mid_v == mid_i:
        return mid_v

    left_end = min(mid_i - 1, mid_v)
    left_result = magic_index_fast(l, start, left_end)
    if left_result is not None:
        return left_result

    right_start = max(mid_i + 1, mid_v)
    return magic_index_fast(l, right_start, end)


class Test(unittest.TestCase):
    sorted_nums = [
        ([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13], 7),
        ([-2, -1, 0, 3], 3),
        ([3, 4, 5], None),
        ([-20, 0, 1, 2, 3, 4, 5, 6, 20], None)]

    def test_distinct(self):
        for t in self.sorted_nums:
            self.assertEqual(t[1], magic_index(t[0]))
            self.assertEqual(t[1], magic_index_2(t[0]))
            self.assertEqual(t[1], magic_index_distinct(t[0], 0, len(t[0]) - 1))

    not_distinct_sorted_nums = [
        ([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13], 7),
        ([-2, -1, 0, 3], 3),
        ([3, 4, 5], None),
        ([-20, 5, 5, 5, 5, 5, 7, 20], 5)]

    def test_not_distinct(self):
        for t in self.not_distinct_sorted_nums:
            self.assertEqual(t[1], magic_index(t[0]))
            self.assertEqual(t[1], magic_index_2(t[0]))
            self.assertEqual(t[1], magic_index_fast(t[0], 0, len(t[0]) - 1))


if __name__ == '__main__':
    unittest.main()
