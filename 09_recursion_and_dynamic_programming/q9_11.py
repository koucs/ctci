#! env python
# -*- coding: utf-8 -*-

import re
import time
import unittest
from typing import List, Optional, Iterator, Dict


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


def f_dp(exp: str, result: bool, t_dict: Dict, f_dict: Dict) -> Optional[List]:
    if result and exp in t_dict:
        return t_dict[exp]
    if not result and exp in f_dict:
        return f_dict[exp]

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
                left_true, left_false = f_dp(left, True, t_dict, f_dict), f_dp(left, False, t_dict, f_dict)
                right_true, right_false = f_dp(right, True, t_dict, f_dict), f_dp(right, False, t_dict, f_dict)
                append(ans, left_true, op, right_true)
                append(ans, left_true, op, right_false)
                append(ans, left_false, op, right_true)
            elif op == "&":
                left_true, right_true = f_dp(left, True, t_dict, f_dict), f_dp(right, True, t_dict, f_dict)
                append(ans, left_true, op, right_true)
            elif op == "^":
                left_true, left_false = f_dp(left, True, t_dict, f_dict), f_dp(left, False, t_dict, f_dict)
                right_true, right_false = f_dp(right, True, t_dict, f_dict), f_dp(right, False, t_dict, f_dict)
                append(ans, left_true, op, right_false)
                append(ans, left_false, op, right_true)
    else:
        for s in get_operator_indexes(exp):
            left, op, right = exp[:s], exp[s], exp[s + 1:]

            if op == "|":
                left_false, right_false = f_dp(left, False, t_dict, f_dict), f_dp(right, False, t_dict,
                                                                                  f_dict)
                append(ans, left_false, op, right_false)
            elif op == "&":
                left_true, left_false = f_dp(left, True, t_dict, f_dict), f_dp(left, False, t_dict, f_dict)
                right_true, right_false = f_dp(right, True, t_dict, f_dict), f_dp(right, False, t_dict, f_dict)
                append(ans, left_true, op, right_false)
                append(ans, left_false, op, right_true)
                append(ans, left_false, op, right_false)
            elif op == "^":
                left_true, left_false = f_dp(left, True, t_dict, f_dict), f_dp(left, False, t_dict, f_dict)
                right_true, right_false = f_dp(right, True, t_dict, f_dict), f_dp(right, False, t_dict, f_dict)
                append(ans, left_true, op, right_true)
                append(ans, left_false, op, right_false)

    if result:
        t_dict[exp] = ans
    else:
        f_dict[exp] = ans
    return ans


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
        start_time = time.time()
        print(f("1^0|0|1", True))
        self.assertEqual(2, len(f("1|1^0", True)))
        self.assertEqual(0, len(f("1|1^0", False)))
        self.assertEqual(0, len(f("0^0^0", True)))
        self.assertEqual(2, len(f("0^0^0", False)))
        self.assertEqual(0, len(f("1&1&0", True)))
        self.assertEqual(34209, len(f("1^1&0|1^0^1&0|1^0&0&1|1", True)))
        self.assertEqual(24577, len(f("1^1&0|1^0^1&0|1^0&0&1|1", False)))
        print(f"test_1: {time.time() - start_time}")  # test_1: 13.460424423217773XL
        return

    def test_2(self):
        start_time = time.time()
        print(f_dp("1^0|0|1", True, {}, {}))
        self.assertEqual(2, len(f_dp("1|1^0", True, {}, {})))
        self.assertEqual(0, len(f_dp("1|1^0", False, {}, {})))
        self.assertEqual(0, len(f_dp("0^0^0", True, {}, {})))
        self.assertEqual(2, len(f_dp("0^0^0", False, {}, {})))
        self.assertEqual(0, len(f_dp("1&1&0", True, {}, {})))
        self.assertEqual(34209, len(f_dp("1^1&0|1^0^1&0|1^0&0&1|1", True, {}, {})))
        self.assertEqual(24577, len(f_dp("1^1&0|1^0^1&0|1^0&0&1|1", False, {}, {})))
        print(f"test_2: {time.time() - start_time}")  # test_2: 0.03798079490661621
        return


if __name__ == '__main__':
    unittest.main()
