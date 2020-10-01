#! env python
# -*- coding: utf-8 -*-

import unittest
from typing import List, TypeVar

# ctci.5_5
# Date: 2020/10/01
# Filename: 5_5 
# Author: koucs

T = TypeVar('T')


def safe_list_get(l: List, idx: int, default: T) -> T:
    try:
        return l[idx]
    except IndexError:
        return default


# ある整数AからBに変換するのに必要なbit数
def bit_swap_required(a: int, b: int) -> int:
    ans = 0
    a_bin = bin(a)[2:]
    b_bin = bin(b)[2:]

    # fill padding bit
    if len(a_bin) > len(b_bin):
        b_bin = "0" * (len(a_bin) - len(b_bin)) + b_bin
    elif len(a_bin) < len(b_bin):
        a_bin = "0" * (len(b_bin) - len(a_bin)) + a_bin

    for i in range(len(a_bin)):
        a_ittr = safe_list_get(a_bin, i, None)
        b_ittr = safe_list_get(b_bin, i, None)
        if a_ittr != b_ittr:
            ans += 1

    return ans


def bit_swap_required2(a: int, b: int) -> int:
    ans = 0
    c = a ^ b
    while c != 0:
        ans += c & 1
        c = c >> 1
    return ans


def bit_swap_required3(a: int, b: int) -> int:
    ans = 0
    c = a ^ b
    while c != 0:
        ans += 1
        c = c & (c - 1)
    return ans


class Test(unittest.TestCase):
    def test_1(self):
        # 31 = 0001 1111, 14 = 0000 1110
        self.assertEqual(bit_swap_required(31, 14), 2)
        self.assertEqual(bit_swap_required(12, 14), 1)
        self.assertEqual(bit_swap_required(7, 14), 2)

        self.assertEqual(bit_swap_required2(31, 14), 2)
        self.assertEqual(bit_swap_required2(12, 14), 1)
        self.assertEqual(bit_swap_required2(7, 14), 2)

        self.assertEqual(bit_swap_required3(31, 14), 2)
        self.assertEqual(bit_swap_required3(12, 14), 1)
        self.assertEqual(bit_swap_required3(7, 14), 2)
        return


if __name__ == '__main__':
    unittest.main()
