#! env python
# -*- coding: utf-8 -*-

import unittest
from typing import List


# ctci.q9_1
# Give the number of ways to climb n steps 1, 2, or 3 steps at a time.
def count_stairs(n: int, patterns: List) -> List:
    l = []
    for i in patterns:
        if (n - i) < 0: continue

        stairs = count_stairs(n - i, patterns)
        if len(stairs) == 0:
            l.append([i])
            continue

        for j in stairs:
            l.append([i] + j)
    return l


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(len(count_stairs(4, [1, 2, 3])), 7)
        return


if __name__ == '__main__':
    unittest.main()
