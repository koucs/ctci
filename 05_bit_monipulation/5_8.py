#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, unittest
from typing import List


# ctci.5_8
# draws a horizontal line from (xl, y) to (x2, y).
# Date: 2020/10/05
# Filename: 5_8 
# Author: koucs

# screenの幅は8の倍数
def draw_horizontal_line(screen: List, width: int, x1: int, x2: int, y: int):
    byte_width = width // 8
    height = len(screen) / byte_width

    if x1 > x2:
        x1, x2 = x2, x1
    if x1 < 0 or x2 > width or y > height:
        raise

    x1_offset = x1 % 8
    x1_start = x1 // 8
    if x1_offset != 0:
        x1_start += 1

    x2_offset = x2 % 8
    x2_end = x2 // 8

    for i in range(x1_start, x2_end):
        screen[byte_width * y + i] = 0xFF

    x1_mask = 0xFF >> x1_offset
    x2_mask = (0xFF << x2_offset) & 0xFF

    if (x1 / 8) == (x2 / 8):
        screen[byte_width * y + x1 // 8] = x1_mask & x2_mask
    else:
        if x1_offset != 0:
            screen[byte_width * y + x1_start - 1] = x1_mask
        if x2_offset != 0:
            screen[byte_width * y + x2_end] = x2_mask

    return


class Test(unittest.TestCase):
    def test_1(self):
        screen = [0] * 8 * 3  # x=8, y=3
        draw_horizontal_line(screen, 64, 20, 42, 1)
        self.assertEqual(screen, [0] * 8 + [0, 0, 15, 255, 255, 252, 0, 0] + [0] * 8)

        screen = [0] * 8 * 5  # x=8, y=5
        draw_horizontal_line(screen, 64, 8, 16, 1)
        self.assertEqual(screen, [0] * 8 + [0, 255, 0, 0, 0, 0, 0, 0] + [0] * 24)

        return


if __name__ == '__main__':
    unittest.main()
