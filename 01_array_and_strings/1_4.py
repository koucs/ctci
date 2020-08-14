#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest

# ctci.1_4
# Date: 2020/08/14
# Filename: 1_4 
# Author: acto_mini

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** -7
AtoZ = [chr(i) for i in range(65, 65 + 26)]
atoz = [chr(i) for i in range(97, 97 + 26)]


def replace(str):
    return str.replace(' ', '%20')


class Test(unittest.TestCase):
    TEST_DATA = [
        (['Mr John Smith', 'Mr%20John%20Smith'])
    ]

    def test_1(self):
        for list in self.TEST_DATA:
            self.assertEqual(replace(list[0]), list[1])
        return


if __name__ == '__main__':
    unittest.main()
