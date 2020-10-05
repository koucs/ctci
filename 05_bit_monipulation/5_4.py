#! env python
# -*- coding: utf-8 -*-

import sys, unittest

# ctci.5_4
# Date: 2020/09/30
# Filename: 5_4 
# Author: koucs

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** -7
AtoZ = [chr(i) for i in range(65, 65 + 26)]
atoz = [chr(i) for i in range(97, 97 + 26)]


# ((n & (n-1)0 == 0)
#  => Check n == 2^x (two to the x-th power)
def check(n: int) -> bool:
    return (n & (n - 1)) == 0


class Test(unittest.TestCase):
    def test_1(self):
        for i in range(0, 257):
            print("n:{} ans:{}".format(i, check(i)))
        return


if __name__ == '__main__':
    unittest.main()
