#! env python
# -*- coding: utf-8 -*-
from __future__ import annotations

import unittest, sys


# ctci.7_3
# Given two lines on a Cartesian plane, determine whether the two lines would intersect.
# Date: 2020/10/18
# Author: koucs

class Line:
    def __init__(self, slope: float, y_intercept: float):
        self.slope = slope
        self.y_intercept = y_intercept
        return

    def is_intersect(self, line: Line):
        # floatの値の判定には == を使わない
        # 切片が同じ直線の判定
        check1 = abs(self.y_intercept - line.y_intercept) < sys.float_info.epsilon
        # 傾きが異なる直線の判定
        check2 = abs(self.slope - line.slope) > sys.float_info.epsilon
        return check1 or check2


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Line(2.0, 5.0).is_intersect(Line(2.0, 3.0)), False)
        self.assertEqual(Line(2.0, 5.0).is_intersect(Line(5.0, 3.0)), True)
        self.assertEqual(Line(2.0, 5.0).is_intersect(Line(2.0, 5.0)), True)
        return


if __name__ == '__main__':
    unittest.main()
