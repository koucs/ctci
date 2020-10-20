#! env python
# -*- coding: utf-8 -*-

import unittest
from typing import Optional


# ctci.7_4
# The only operation we have to work with is the add operator. In each of these problems,
# it's useful to think in depth about what these operations really do or how to phrase
# them in terms of other operations (either add or operations we've already completed).
# Date: 2020/10/20
# Author: koucs

def minus(v: int) -> int:
    result = 0
    offset = 1 if v < 0 else -1
    while v != 0:
        result += offset
        v += offset
    return result


def multi(v1: int, v2: int) -> int:
    if abs(v1) < abs(v2):
        return multi(v2, v1)
    if v2 < 0:
        v1 = minus(v1)
    sum = 0
    for i in range(abs(v2)):
        sum += v1
    return sum


def sub(v1: int, v2: int) -> int:
    return v1 + minus(v2)


def div(v1: int, v2: int) -> Optional[int]:
    if v2 == 0:
        return None
    if v1 == 0 or (abs(v1) < abs(v2)):
        return 0

    offset = -1 if (v1 < 0 and v2 > 0) or (v1 > 0 and v2 < 0) else 1
    result = 0
    v1 = abs(v1)
    v2 = abs(v2)
    while (v1 >= v2):
        result += offset
        v1 += minus(v2)

    return result


class Test(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multi(10, 0), 0)
        self.assertEqual(multi(5, 3), 15)
        self.assertEqual(multi(4, -3), -12)
        self.assertEqual(multi(-2, 5), -10)
        self.assertEqual(multi(-1, -5), 5)
        return

    def test_sub(self):
        self.assertEqual(sub(10, 0), 10)
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(4, -3), 7)
        self.assertEqual(sub(-2, 5), -7)
        self.assertEqual(sub(-1, -5), 4)
        return

    def test_div(self):
        self.assertEqual(div(10, 0), None)
        self.assertEqual(div(0, 1), 0)
        self.assertEqual(div(5, 3), 1)
        self.assertEqual(div(4, -3), -1)
        self.assertEqual(div(-20, 5), -4)
        self.assertEqual(div(-1, -5), 0)
        return


if __name__ == '__main__':
    unittest.main()
