#! env python
# -*- coding: utf-8 -*-

import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest


# ctci.3_4
# Date: 2020/08/16
# Filename: 3_4 
# Author: koucs

def move(a, b):
    '''Move from top of one stack to top of other stack'''

    b.append(a.pop())


def towers(n, f, t, s):  # from, to, spare
    if n == 1:
        move(f, t)
    else:
        print('[f->s] {} moving from {} to {} spare {}'.format(n, f, t, s))
        towers(n - 1, f, s, t)
        print('[f->t] {} moving from {} to {} spare {}'.format(n, f, t, s))
        towers(1, f, t, s)
        print('[s->t] {} moving from {} to {} spare {}'.format(n, f, t, s))
        towers(n - 1, s, t, f)


class Test(unittest.TestCase):
    def test_1(self):
        stack_a = []
        stack_b = []
        stack_c = []
        stack_a.append(3)
        stack_a.append(2)
        stack_a.append(1)

        print(stack_a)
        print(stack_b)
        print(stack_c)

        towers(3, stack_a, stack_b, stack_c)

        self.assertEqual([], stack_a)
        self.assertEqual([3, 2, 1], stack_b)
        self.assertEqual([], stack_c)


if __name__ == '__main__':
    unittest.main()
