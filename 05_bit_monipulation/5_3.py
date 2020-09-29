#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest

# ctci.5_3
# Date: 2020/09/29
# Filename: 5_3 
# Author: koucs

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** -7
AtoZ = [chr(i) for i in range(65, 65 + 26)]
atoz = [chr(i) for i in range(97, 97 + 26)]


def get_next(num: int):
    c = num

    c0 = 0  # 右端から連続する 0 bit の数
    while c & 1 == 0 and c != 0:
        c0 += 1
        c >>= 1

    c1 = 0  # （c0 の ビットを除く）　右端から連続する 1 bit の数
    while c & 1 == 1 and c != 0:
        c1 += 1
        c >>= 1

    p = c0 + c1

    print(bin(num)[2:])
    print(c0, c1, p)

    # p番目のビットを 0 -> 1 に反転
    # そこから右に、 (c0+1)個の 0 bit (c1-1)個の 1 bit を配置
    result = bin(num)[2:][0:len(bin(num)[2:]) - int(p) - 1] \
             + "1" \
             + "0" * (c0 + 1) \
             + "1" * (c1 - 1)
    print(result)
    return result


def get_prev(num: int):
    c = num

    c1 = 0  # 右端から連続する 1 bit の数
    while c & 1 == 1 and c != 0:
        c1 += 1
        c >>= 1

    c0 = 0  # （c1 の ビットを除く）右端から連続する 0 bit の数
    while c & 1 == 0 and c != 0:
        c0 += 1
        c >>= 1

    p = c0 + c1

    print(bin(num)[2:])
    print(c0, c1, p)

    # p番目のビットを 1 -> 0 に反転
    # そこから右に、 (c1+1)個の 1 bit (c0-1)個の 0 bit を配置
    result = bin(num)[2:][0:len(bin(num)[2:]) - int(p) - 1] \
             + "0" \
             + "1" * (c1 + 1) \
             + "0" * (c0 - 1)
    print(result)
    return result


class Test(unittest.TestCase):
    def test_1(self):
        num = 13948
        bin_num = bin(num)[2:]
        self.assertEqual(bin_num, "11011001111100")
        self.assertEqual(get_next(num), "11011010001111")
        self.assertEqual(get_prev(num), "11011001111010")
        return


if __name__ == '__main__':
    unittest.main()
