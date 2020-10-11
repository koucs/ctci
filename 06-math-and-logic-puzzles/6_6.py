#! env python
# -*- coding: utf-8 -*-

import unittest
from typing import List


# ctci.6_6
# Date: 2020/10/11
# Filename: 6_6 
# Author: koucs

# How many lockers are left open if each locker is toggles once for each of its divisors.
# locker's state
# True: open
# False: close

def lock_unlock(lockers: List, num: int):
    for i in range(1, num):
        for j in range(i, num, i):
            lockers[j] = not lockers[j]
    return


class Test(unittest.TestCase):
    def test_1(self):
        l = [False] * 100
        lock_unlock(l, 100)

        # [1, 4, 9, 16, 25, 36, 49, 64, 81]
        print([i for i, v in enumerate(l) if v == True])

        # n != square number: even number of divisors.
        #                     ex: n=15 (1,15)(3,5)
        # n == square number: odd number of divisors.
        #                     ex: n=36 (1,36)(2,18)(3,12)(4,9)(6,6) <- 6 is counted as a single number
        self.assertEqual(l.count(True), 9)
        return


if __name__ == '__main__':
    unittest.main()
