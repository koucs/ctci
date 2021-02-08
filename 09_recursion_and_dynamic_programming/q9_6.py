#! env python
# -*- coding: utf-8 -*-

import unittest
from typing import List, Optional


# Date: 2021/01/23
# 9.6. Implement an algorithm to print all valid
# (e.g., properly opened and closed) combinations of n-pairs of parentheses.

def parentheses_recursive(s: str, ans: List, left_remains: int, right_remains: int, depth: int) -> Optional[List]:
    if left_remains < 0 or right_remains < 0 or right_remains < left_remains:
        return None
    if left_remains == right_remains == 0:
        ans.append(str(s))
        return ans
    else:
        if left_remains > 0:
            s = s[:depth] + "(" + s[depth+1:]
            parentheses_recursive(s, ans, left_remains-1, right_remains, depth+1)
        if right_remains > left_remains:
            s = s[:depth] + ")" + s[depth+1:]
            parentheses_recursive(s, ans, left_remains, right_remains-1, depth+1)


def parentheses(n: int) -> Optional[List]:
    ans = []
    parentheses_recursive(str(), ans, n, n, 0)
    return ans


class Test(unittest.TestCase):
    def test_1(self):
        self.assertCountEqual(parentheses(2), ["()()", "(())"])
        self.assertCountEqual(parentheses(3), ["()()()", "(())()", "()(())", "((()))", "(()())"])
        return


if __name__ == '__main__':
    unittest.main()
