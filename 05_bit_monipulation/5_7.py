#! env python
# -*- coding: utf-8 -*-

import unittest
from typing import List


# ctci.5_7
# Date: 2020/10/04
# Filename: 5_7 
# Author: koucs

# An array A[1…n] contains all the integers from 0 to n except for one number which is missing.
# In this problem, we cannot access an entire integer in A with a single operation.
# The elements of A are represented in binary, and the only operation we can use to access them is
# “fetch the jth bit of A[i]”, which takes constant time.
# Write code to find the missing integer. Can you do it in O(n) time?

# 下位jビットを返却する
def fetch(l: List, i: int, j: int) -> int:
    # return 0/1 bit
    return (l[i] >> j) & 1


def find_missing(input: List, column: int) -> int:
    # XXX: 一番左側が1のbitにすべき
    if column > 32:
        return 0

    one_bits = []
    zero_bits = []

    for i, n in enumerate(input):
        if fetch(input, i, column) == 0:
            zero_bits.append(n)
        else:
            one_bits.append(n)

    if len(zero_bits) <= len(one_bits):
        v = find_missing(zero_bits, column + 1)
        return (v << 1) | 0
    else:
        v = find_missing(one_bits, column + 1)
        return (v << 1) | 1


class Test(unittest.TestCase):
    def test_1(self):
        l = list(range(11))
        l.remove(5)  # remove "5" data (not "5"'s index data)
        self.assertEqual(find_missing(l, 0), 5)
        l = list(range(100))
        l.remove(10)
        self.assertEqual(find_missing(l, 0), 10)
        return


if __name__ == '__main__':
    unittest.main()
