#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest

# ctci.1_5
# Date: 2020/08/14
# Filename: 1_5 
# Author: acto_mini

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** -7
AtoZ = [chr(i) for i in range(65, 65 + 26)]
atoz = [chr(i) for i in range(97, 97 + 26)]


def compress(string):
    ans = ''
    base = None
    count = 0
    for c in string:
        if base is None:
            base = c
            count = 1
        elif base == c:
            count += 1
        elif base != c:
            ans += base + str(count)
            base = c
            count = 1

    if base is not None:
        ans = ans + base + str(count)
    if len(ans) >= len(string):
        return string
    else:
        return ans


class Test(unittest.TestCase):
    TEST_DATA = [
        ('abcdef', 'abcdef'),
        ('abcdeff', 'abcdeff'),
        ('abcdeffffffff', 'a1b1c1d1e1f8'),
        ('aabcccccaaa', 'a2b1c5a3'),
        ('aabcccccaaaaa', 'a2b1c5a5'),
        ('aaaaaabbb', 'a6b3'),
        ('aaaaaa', 'a6'),
        ('', ''),
        ('a', 'a'),
        ('aa', 'aa')
    ]

    def test_1(self):
        for input, expected in self.TEST_DATA:
            self.assertEqual(compress(input), expected)
        return


if __name__ == '__main__':
    unittest.main()
