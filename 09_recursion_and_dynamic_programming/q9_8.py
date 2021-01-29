#! env python
# -*- coding: utf-8 -*-

import unittest
from typing import List, Optional


# Date: 2021/01/29
# 9.8. Given an infinite number of quarters (25 cents), dimes (10 cents),nickels (5 cents) and pennies (1 cent),
# write code to calculate the number of ways of representing n cents.

def small_changes(cents: int, coins: List) -> Optional[List]:
    """ coins: should be DISTINCT numbers """
    coins = list(filter(lambda x: x <= cents, coins))
    max_coin = max(coins)
    ans = []

    if (cents % max_coin) == 0:
        ans.append([max_coin] * (cents // max_coin))

    if len(coins) == 1:
        return ans

    i = 0
    partial_coins = list(coins)
    partial_coins.remove(max_coin)

    while cents > (max_coin * i):
        ret = small_changes(cents - (max_coin * i), partial_coins)
        for a in ret:
            ans.append([max_coin] * i + a)
        i += 1
    return ans


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(2, len(small_changes(5, [1, 5, 10, 25])))
        self.assertEqual(9, len(small_changes(20, [1, 5, 10, 25])))
        self.assertEqual(49, len(small_changes(50, [1, 5, 10, 25])))
        self.assertEqual(121, len(small_changes(75, [1, 5, 10, 25])))
        return


if __name__ == '__main__':
    unittest.main()
