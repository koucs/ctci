#! env python
# -*- coding: utf-8 -*-

import unittest
from typing import List, Optional, Dict


# ctci.q9_10
# Date: 2021/02/04

# 9.10.
# You have a stack of n boxes, with widths w_{i}, heights h_{i} and depths d_{i}.
# The boxes cannot be rotated and can only be stacked on top of one another
# if each box in the stack is strictly larger than the box above it in width, height, and depth.
# Implement a method to build the tallest stack possible,
# where the height of a stack is the sum of the heights of each box.


class Box:
    def __init__(self, height: float, width: float, depth: float):
        self.height = height
        self.width = width
        self.depth = depth


def check(base: Box, box: Box) -> bool:
    return base.height > box.height and base.width > box.width and base.depth > box.depth


def boxes_height(boxes: List[Box]) -> float:
    result = 0
    for box in boxes:
        result += box.height
    return result


def find_tallest_recursive(remain_boxes: List[Box], base_box: Optional[Box]) -> Optional[List[Box]]:
    if len(remain_boxes) == 0:
        return None

    max_height = -1
    max_boxes = None

    for i, b in enumerate(remain_boxes):
        if base_box is not None and not check(base_box, b):
            continue

        tmp_boxes = list(remain_boxes)
        tmp_boxes.remove(b)

        result = find_tallest_recursive(tmp_boxes, b)
        boxes = [b] + result if result is not None else [b]
        height = boxes_height(boxes)

        if max_height < height:
            max_height = height
            max_boxes = boxes

    return max_boxes


def find_tallest_dp(remain_boxes: List[Box], base_box: Optional[Box], cache: Dict) -> Optional[List[Box]]:
    if len(remain_boxes) == 0:
        return None

    if len(cache) != 0 and base_box in cache:
        return cache.get(base_box)

    max_height = -1
    max_boxes = None

    for i, b in enumerate(remain_boxes):
        if base_box is not None and not check(base_box, b):
            continue

        tmp_boxes = list(remain_boxes)
        tmp_boxes.remove(b)

        result = find_tallest_dp(tmp_boxes, b, cache)
        boxes = [b] + result if result is not None else [b]
        height = boxes_height(boxes)

        if max_height < height:
            max_height = height
            max_boxes = boxes

    cache[base_box] = max_boxes

    return max_boxes


def find_tallest(boxes: List[Box]) -> List[Box]:
    sorted_boxes = sorted(boxes, key=lambda box: box.height)
    return find_tallest_recursive(sorted_boxes, None)


def find_tallest2(boxes: List[Box]) -> List[Box]:
    sorted_boxes = sorted(boxes, key=lambda box: box.height)
    return find_tallest_dp(sorted_boxes, None, {})


class Test(unittest.TestCase):
    def test_1(self):
        # Box (height, width, depth)
        b1 = Box(4, 3, 1)
        b2 = Box(6, 8, 2)
        b3 = Box(8, 7, 3)
        self.assertEqual(find_tallest([b1, b2, b3]), [b3, b1])

        b1 = Box(1.5, 6.1, 7.3)
        b2 = Box(4.3, 6.3, 4.9)
        b3 = Box(4.1, 6.4, 9.4)
        b4 = Box(1.3, 0.8, 1.2)
        self.assertEqual(find_tallest([b1, b2, b3, b4]), [b3, b1, b4])
        return

    def test_2(self):
        # Box (height, width, depth)
        b1 = Box(4, 3, 1)
        b2 = Box(6, 8, 2)
        b3 = Box(8, 7, 3)
        self.assertEqual(find_tallest2([b1, b2, b3]), [b3, b1])

        b1 = Box(1.5, 6.1, 7.3)
        b2 = Box(4.3, 6.3, 4.9)
        b3 = Box(4.1, 6.4, 9.4)
        b4 = Box(1.3, 0.8, 1.2)
        self.assertEqual(find_tallest2([b1, b2, b3, b4]), [b3, b1, b4])
        return


if __name__ == '__main__':
    unittest.main()
