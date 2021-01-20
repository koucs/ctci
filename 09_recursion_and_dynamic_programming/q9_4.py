#! env python
# -*- coding: utf-8 -*-

import unittest
from typing import List


# Date: 2021/01/20
# Author: koucs
#
# 9.4. Write a method to return all subsets of a set.

def get_subsets(set_str: str) -> List:
    ans = [[""], [set_str[0]]]
    for i in range(1, len(set_str)):
        prev_list = [list(sub_ans) for sub_ans in ans]
        ittr_char = set_str[i]
        for i, subset in enumerate(prev_list):
            if subset[0] == "":
                prev_list[i] = [ittr_char]
            else:
                subset.append(ittr_char)
        ans += prev_list
    return ans


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_subsets("a"), [[""], ["a"]])
        self.assertEqual(get_subsets("ab"), [[""], ["a"], ["b"], ["a", "b"]])
        self.assertEqual(get_subsets("abc"), [[""], ["a"], ["b"], ["a", "b"],
                                              ["c"], ["a", "c"], ["b", "c"], ["a", "b", "c"]])
        return


if __name__ == '__main__':
    unittest.main()
