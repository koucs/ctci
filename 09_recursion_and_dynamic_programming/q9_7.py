#! env python
# -*- coding: utf-8 -*-

import unittest
from typing import List, Optional


# 9.7. Implement the "paint fill" function
# Date: 2021/01/27


def fill(img: List, cache: List, x: int, y: int, new_color: int, old_color: int) -> Optional[List]:
    if img[x][y] == new_color or cache[x][y]:
        if not cache[x][y]:
            cache[x][y] = True
        return None

    cache[x][y] = True

    if img[x][y] == old_color:
        img[x][y] = new_color
        if x > 0:
            fill(img, cache, x - 1, y, new_color, old_color)
        if x < (len(img) - 1):
            fill(img, cache, x + 1, y, new_color, old_color)
        if y > 0:
            fill(img, cache, x, y - 1, new_color, old_color)
        if y < (len(img[0]) - 1):
            fill(img, cache, x, y + 1, new_color, old_color)

    return img


def paint_fill(img: List, x: int, y: int, color: int) -> Optional[List]:
    if img[x][y] == color:
        return img
    old_color = img[x][y]
    cache = [[False] * len(img[0]) for i in range(len(img))]
    ans = list(map(list, img))
    return fill(ans, cache, x, y, color, old_color)


class Test(unittest.TestCase):
    def test_1(self):
        p1 = [[0, 0],
              [0, 2]]
        a1 = [[3, 3],
              [3, 2]]
        self.assertEqual(a1, paint_fill(p1, 0, 0, 3))

        p2 = [[0, 0, 0, 1],
              [0, 1, 0, 2],
              [0, 1, 1, 2]]
        a2 = [[4, 4, 4, 1],
              [4, 1, 4, 2],
              [4, 1, 1, 2]]
        self.assertEqual(a2, paint_fill(p2, 1, 2, 4))

        p3 = [[2, 1, 1, 2, 2],
              [2, 1, 1, 0, 0],
              [2, 1, 2, 1, 2],
              [2, 2, 2, 2, 2]]
        a3 = [[0, 1, 1, 2, 2],
              [0, 1, 1, 0, 0],
              [0, 1, 0, 1, 0],
              [0, 0, 0, 0, 0]]
        self.assertEqual(a3, paint_fill(p3, 2, 2, 0))

        return


if __name__ == '__main__':
    unittest.main()
