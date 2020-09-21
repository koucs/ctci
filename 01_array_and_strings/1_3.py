#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest

# ctci.1_3
# Date: 2020/08/14
# Filename: 1_3 
# Author: koucs

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    char_count = [0 for _ in range(256)]

    for char in str1:
        char_num = ord(char)
        char_count[char_num] += 1

    for char in str2:
        char_num = ord(char)
        char_count[char_num] -= 1
        if char_count[char_num] < 0:
            return False

    return True


class Test(unittest.TestCase):
    TEST_DATA = [
        (['vivek', 'keviv'], True),
        (['a', 'aa '], False),
        (['a', ''], False),
        (['', 'a'], False),
        (['vivek', 'vivek '], False)
    ]

    def test_1(self):
        for texts, expected_result in self.TEST_DATA:
            self.assertEqual(check_permutation(texts[0], texts[1]), expected_result)


if __name__ == '__main__':
    unittest.main()
