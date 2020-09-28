#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest

# ctci.5_2
# Date: 2020/09/28
# Filename: 5_2 
# Author: koucs

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** -7
AtoZ = [chr(i) for i in range(65, 65 + 26)]
atoz = [chr(i) for i in range(97, 97 + 26)]


def check_binary(num: float) -> str:
    if num >= 1 or 0 >= num:
        return "ERROR"
    result = "."
    while num != 0:
        if len(result) >= 32:
            return "ERROR"

        r = num * 2
        if r >= 1:
            result += "1"
            num = r - 1
        else:
            result += "0"
            num = r

    return result


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(check_binary(float(0.625)), ".101")
        self.assertEqual(check_binary(float(2 ** -31)), ".0000000000000000000000000000001")
        self.assertEqual(check_binary(float(2 ** -32)), "ERROR")
        self.assertEqual(check_binary(float(1)), "ERROR")
        return


if __name__ == '__main__':
    unittest.main()
