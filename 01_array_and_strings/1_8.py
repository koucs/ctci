#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest


# ctci.1_8
# Date: 2020/08/15
# Filename: 1_8 
# Author: acto_mini

def is_substring(s1, s2):
    return s1 in s2


def is_rotate(s1, s2):
    if len(s1) != len(s2):
        return False

    return is_substring(s2, s1+s1)


class Test(unittest.TestCase):
    TEST_DATA = [
        (['waterbottle', 'erbottlewat'], True),
        (['waterbottle', 'ebottlewate'], False)
    ]

    def test_1(self):
        for in_data, result in self.TEST_DATA:
            self.assertEqual(is_rotate(in_data[0], in_data[1]), result)
        return


if __name__ == '__main__':
    unittest.main()
