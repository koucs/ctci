#! env python
# -*- coding: utf-8 -*-

import unittest


# ctci.3_2
# Date: 2020/08/16
# Filename: 3_2 
# Author: acto_mini

class StackWithMinimumValue():

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if len(self.min_stack) == 0:
            self.min_stack.append(val)
            return

        prev_min = self.min_stack[-1]
        prev_min = val if prev_min > val else prev_min
        self.min_stack.append(prev_min)

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    def min_val(self):
        return self.min_stack[-1]


class Test(unittest.TestCase):
    def test_1(self):
        stack = StackWithMinimumValue()
        stack.push(5)
        self.assertEqual(5, stack.min_val())
        stack.push(6)
        self.assertEqual(5, stack.min_val())
        stack.push(3)
        self.assertEqual(3, stack.min_val())
        stack.push(7)
        self.assertEqual(3, stack.min_val())

        self.assertEqual(7, stack.pop())
        self.assertEqual(3, stack.min_val())
        self.assertEqual(3, stack.pop())
        self.assertEqual(5, stack.min_val())

        return


if __name__ == '__main__':
    unittest.main()
