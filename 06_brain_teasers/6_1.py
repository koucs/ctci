#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest

# ctci.6_1
# The Heavy Pill:
# You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but one has pills of weight
# 1.1 grams. Given a scale that provides an exact measurement, how would you find the heavy bottle?
# You can only use the scale once.
# Date: 2020/10/07
# Author: koucs

NORMAL_PILLS = 1.0
HEAVY_PILLS = 1.1


def find_heavy_bottle(weight: int, bottles: int) -> int:
    all_normal_weight = sum([NORMAL_PILLS * i for i in range(1, bottles + 1)])
    return int((weight - all_normal_weight) / 0.1)


def weight(heavy_index: int, bottles: int) -> int:
    return sum([HEAVY_PILLS * i if i == heavy_index else NORMAL_PILLS * i for i in range(1, bottles + 1)])


class Test(unittest.TestCase):
    def test_1(self):
        w = weight(5, 10)
        self.assertEqual(find_heavy_bottle(w, 10), 5)
        w = weight(13, 20)
        self.assertEqual(find_heavy_bottle(w, 20), 13)
        return


if __name__ == '__main__':
    unittest.main()
