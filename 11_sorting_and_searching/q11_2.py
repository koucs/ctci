#! env python
# -*- coding: utf-8 -*-

import unittest
from typing import List


# Cracking The Coding Interview (5th) q11_2
#
# Write a method to sort an array of strings so that all the anagrams are next to each other.

def anagrams_sort(string_arr: List) -> List:
    pairs = [(sorted(s), s) for s in string_arr]
    # Sort time-complexity :  Average Case & Amortized Worst Case = O(n log n)
    # https://wiki.python.org/moin/TimeComplexity
    pairs = sorted(pairs)
    return [right for left, right in pairs]


class Test(unittest.TestCase):
    def test_1(self):
        strings = ["cat", "bat", "rat", "arts", "tab", "tar", "car", "star"]
        self.assertEqual(anagrams_sort(strings), ["bat", "tab", "car", "cat", "arts", "star", "rat", "tar"])
        return


if __name__ == '__main__':
    unittest.main()
