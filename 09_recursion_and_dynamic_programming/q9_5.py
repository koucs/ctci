#! env python
# -*- coding: utf-8 -*-

import unittest
from typing import List, Optional


# Date: 2021/01/23
# Author: koucs
#
# 9.5. Write a method to compute all permutations of a string.
# (that contains no duplicate letters.)

def permutations(s: str) -> Optional[List]:
    if len(s) < 1:
        return None
    elif len(s) == 1:
        return [s]
    ans = []
    c = s[-1]
    for word in permutations(s[:-1]):
        for i in range(0, len(word) + 1):
            ans.append(word[:i] + c + word[i:])
    return ans


class Test(unittest.TestCase):
    def test_1(self):
        self.assertCountEqual(permutations("abc"), ["abc", "acb", "bac", "bca", "cab", "cba"])
        self.assertCountEqual(permutations("ABCD"), ["ABCD", "ABDC", "ACBD", "ACDB",
                                                     "ADBC", "ADCB", "BACD", "BADC", "BCAD", "BCDA", "BDAC", "BDCA",
                                                     "CABD", "CADB", "CBAD", "CBDA", "CDAB", "CDBA", "DABC", "DACB",
                                                     "DBAC", "DBCA", "DCAB", "DCBA"])
        return


if __name__ == '__main__':
    unittest.main()
