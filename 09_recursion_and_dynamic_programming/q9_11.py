#! env python
# -*- coding: utf-8 -*-

import re
import unittest
from typing import List, Optional, Iterator


# ctci.q9_11
# Date: 2021/02/07
# Given a boolean expression consisting of the symbols 0, 1, &, |, and ^, and a desired boolean result value 'result',
# implement a function to count the number of ways of parenthesizing the expression such that it evaluates to 'result'.
#
# EXAMPLE
# Expression: 1^0|0|1
# Desired result: false (0)
# Output: 2 ways. 1^((0|0)|1) and 1^(0|(0|1))


def get_operator_indexes(str_) -> Iterator[int]:
    pattern = r'&|\||\^'
    for match in re.finditer(pattern, str_):
        yield match.start()


def append(ans: List, left: Optional[List], op: str, right: Optional[List]):
    if left is None or len(left) == 0 or right is None or len(right) == 0:
        return
    for i in left:
        for j in right:
            ans.append("({}){}({})".format(i, op, j))


def f(exp: str, result: bool) -> Optional[List]:
    ans = []
    if len(exp) == 1:
        if result == bool(int(exp)):
            return list(exp)
        else:
            return None

    if result:
        for s in get_operator_indexes(exp):
            left, op, right = exp[:s], exp[s], exp[s + 1:]

            if op == "|":
                left_true, left_false = f(left, True), f(left, False)
                right_true, right_false = f(right, True), f(right, False)
                append(ans, left_true, op, right_true)
                append(ans, left_true, op, right_false)
                append(ans, left_false, op, right_true)
            elif op == "&":
                left_true, right_true = f(left, True), f(right, True)
                append(ans, left_true, op, right_true)
            elif op == "^":
                left_true, left_false = f(left, True), f(left, False)
                right_true, right_false = f(right, True), f(right, False)
                append(ans, left_true, op, right_false)
                append(ans, left_false, op, right_true)
    else:
        for s in get_operator_indexes(exp):
            left, op, right = exp[:s], exp[s], exp[s + 1:]

            if op == "|":
                left_false, right_false = f(left, False), f(right, False)
                append(ans, left_false, op, right_false)
            elif op == "&":
                left_true, left_false = f(left, True), f(left, False)
                right_true, right_false = f(right, True), f(right, False)
                append(ans, left_true, op, right_false)
                append(ans, left_false, op, right_true)
                append(ans, left_false, op, right_false)
            elif op == "^":
                left_true, left_false = f(left, True), f(left, False)
                right_true, right_false = f(right, True), f(right, False)
                append(ans, left_true, op, right_true)
                append(ans, left_false, op, right_false)

    return ans


class Test(unittest.TestCase):
    def test_1(self):
        print(f("1^0|0|1", True))
        self.assertEqual(2, len(f("1|1^0", True)))
        self.assertEqual(0, len(f("1|1^0", False)))
        self.assertEqual(0, len(f("0^0^0", True)))
        self.assertEqual(2, len(f("0^0^0", False)))
        self.assertEqual(0, len(f("1&1&0", True)))
        self.assertEqual(34209, len(f("1^1&0|1^0^1&0|1^0&0&1|1", True)))
        self.assertEqual(24577, len(f("1^1&0|1^0^1&0|1^0&0&1|1", False)))
        return


if __name__ == '__main__':
    unittest.main()
