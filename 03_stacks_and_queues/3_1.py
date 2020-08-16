#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest


# ctci.3_1
# Date: 2020/08/16
# Filename: 3_1 
# Author: acto_mini


class TertiaryStack:

    def __init__(self, size):
        if size <= 0:
            raise Exception("Size must be at least one")

        self.items = [None] * size
        self.st_one_len = 0
        self.st_one_cur = -1
        self.st_two_len = 0
        self.st_two_cur = size
        self.st_three_len = 0
        self.st_three_cur = size / 2
        self.st_three_cur_dir = 1

    def push(self, st_num, item):
        if item is None:
            raise Exception("Item cannot be None (reserved).")

        if st_num == 1:
            if self.st_one_cur + 1 >= self.st_three_cur or \
                    self.items[self.st_one_cur + 1] is not None:
                raise Exception("Stack one is full")

            self.items[self.st_one_cur + 1] = item
            self.st_one_cur += 1
            self.st_one_len += 1

        elif st_num == 2:
            if self.st_two_cur - 1 <= self.st_three_cur or \
                    self.items[self.st_two_cur - 1] is not None:
                raise Exception("Stack two is full")

            self.items[self.st_two_cur - 1] = item
            self.st_two_cur -= 1
            self.st_two_len += 1

        elif st_num == 3:
            next_slot = self.st_three_cur + (self.st_three_len *
                                             self.st_three_cur_dir)

            if next_slot <= self.st_one_cur or next_slot >= self.st_two_cur or \
                    self.items[next_slot] is not None:
                raise Exception("Stack three cannot expand further")

            self.items[next_slot] = item
            self.st_three_cur = next_slot
            self.st_three_len += 1
            self.st_three_cur_dir *= -1

        else:
            raise Exception("Unknown stack referenced")

    def pop(self, st_num):
        if st_num == 1:
            if self.st_one_len > 0:
                item = self.items[self.st_one_cur]
                self.items[self.st_one_cur] = None
                self.st_one_len -= 1
                self.st_one_cur -= 1
                return item

        elif st_num == 2:
            if self.st_two_len > 0:
                item = self.items[self.st_two_cur]
                self.items[self.st_two_cur] = None
                self.st_two_len -= 1
                self.st_two_cur += 1
                return item

        elif st_num == 3:
            if self.st_three_len > 0:
                item = self.items[self.st_three_cur]
                self.items[self.st_three_cur] = None
                self.st_three_len -= 1
                self.st_three_cur += self.st_three_len * self.st_three_cur_dir
                self.st_three_cur_dir *= -1
                return item

        else:
            raise Exception("Unknown stack referenced")


def peek(self, st_num):
    if st_num == 1:
        if self.st_one_len > 0:
            return self.items[self.st_one_cur]
    elif st_num == 2:
        if self.st_two_len > 0:
            return self.items[self.st_two_cur]
    elif st_num == 3:
        if self.st_three_len > 0:
            return self.items[self.st_three_cur]
    else:
        raise Exception("Unknown stack referenced")


def count(self, st_num):
    if st_num == 1:
        return self.st_one_len
    elif st_num == 2:
        return self.st_two_len
    elif st_num == 3:
        return self.st_three_len
    else:
        raise Exception("Unknown stack referenced")


def enumerate(self):
    return self.items


class Test(unittest.TestCase):
    def test_1(self):
        stack = TertiaryStack(30)
        stack.push(1, 10)
        stack.push(1, 11)
        stack.push(1, 12)
        stack.push(2, 20)
        stack.push(2, 21)
        stack.push(2, 22)

        self.assertEqual(stack.pop(1), 12)
        self.assertEqual(stack.pop(1), 11)
        self.assertEqual(stack.pop(1), 10)

        self.assertEqual(stack.pop(2), 22)
        self.assertEqual(stack.pop(2), 21)
        self.assertEqual(stack.pop(2), 20)

        return


if __name__ == '__main__':
    unittest.main()
