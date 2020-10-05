#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest


# ctci.5_1
# Date: 2020/09/22
# Filename: 5_1 
# Author: koucs


def replace_bit(m: int, n: int, i: int, j: int) -> int:
    # ensure (j-i-1) == len(n)
    len = j - i + 1
    mask = ~((2 ** len - 1) << i)
    return (m & mask) | (n << i)


class Test(unittest.TestCase):
    def test_1(self):
        N = 0b10000000000
        M = 0b10011
        i, j = 2, 6
        self.assertEqual(replace_bit(N, M, i, j), 0b10001001100)
        return


if __name__ == '__main__':
    unittest.main()
