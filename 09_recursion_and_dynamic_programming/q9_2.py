#! env python
# -*- coding: utf-8 -*-

import pprint
import unittest
from typing import List, Optional


# ctci.9_2
# Date: 2020/12/31
# Filename: 9_2 
# Author: koucs

# 9.2
# Imagine a robot sitting on the upper left corner of an X by Y grid.
# The robot can only move in two directions: right and down.
# How many possible paths are there for the robot to go from (0,0) to (X,Y)?
def paths(current_x: int, current_y: int, goal_x: int, goal_y,
          off_limit_x: Optional[int], off_limit_y: Optional[int]) -> List:
    ahead_x_paths, ahead_y_paths = [], []

    if current_x < goal_x and (off_limit_x is None or (current_x + 1 != off_limit_x or current_y != off_limit_y)):
        ahead_x_paths = paths(current_x + 1, current_y, goal_x, goal_y, off_limit_x, off_limit_y)
    if current_y < goal_y and (off_limit_y is None or (current_x != off_limit_x or current_y + 1 != off_limit_y)):
        ahead_y_paths = paths(current_x, current_y + 1, goal_x, goal_y, off_limit_x, off_limit_y)

    result = [[[goal_x, goal_y]]] if current_x == goal_x and current_y == goal_y else []

    for path in ahead_x_paths:
        path.insert(0, [current_x, current_y])
        result.append(path)
    for path in ahead_y_paths:
        path.insert(0, [current_x, current_y])
        result.append(path)

    return result


class Test(unittest.TestCase):
    def test_1(self):
        pprint.pprint(paths(0, 0, 4, 1, None, None))
        self.assertEqual(len(paths(0, 0, 4, 1, None, None)), 5)

        pprint.pprint(paths(0, 0, 4, 1, 3, 1))
        self.assertEqual(len(paths(0, 0, 4, 1, 3, 1)), 1)
        return


if __name__ == '__main__':
    unittest.main()
