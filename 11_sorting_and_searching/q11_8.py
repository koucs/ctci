#! env python
# -*- coding: utf-8 -*-

import unittest
from typing import List


# Cracking The Coding Interview (5th) q11_8
#
# Imagine you are reading in a stream of integers.
# Periodically, you wish to be able to look up the rank of a number x (the number of values less than or equal tox).
# Implement the data structures and algorithms to support these operations.
# That is, implement the method track(int x), which is called when each number is generated,
# and the method getRankOfNumber(int x),
# which returns the number of values less than or equal to x (not including x itself).
#
# EXAMPLE
# Stream (in order of appearance): 5, 1, 4, 4, 5, 9, 7, 13, 3
# getRankOfNumber(l) = 0
# getRankOfNumber(3) = 1
# getRankOfNumber(4) = 3

class RankNode:
    left_size = 0
    left, right = None, None
    data = 0

    def __init__(self, data: int):
        self.data = data

    def insert(self, data: int):
        if data <= self.data:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = RankNode(data)
            self.left_size += 1
        else:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = RankNode(data)

    def get_rank(self, target: int) -> int:
        if target == self.data:
            return self.left_size
        elif target < self.data:
            if self.left is not None:
                return self.left.get_rank(target)
            else:
                return -1
        else:
            right_rank = -1 if self.right is None else self.right.get_rank(target)
            if right_rank == -1:
                return -1
            return self.left_size + 1 + right_rank


class StreamReader:
    root_node = None

    def track(self, num: int):
        if self.root_node is None:
            self.root_node = RankNode(num)
        else:
            self.root_node.insert(num)

    def track_bulk(self, nums: List):
        for i in nums:
            self.track(i)

    def get_rank(self, num: int) -> int:
        if self.root_node is not None:
            return self.root_node.get_rank(num)
        return -1


class Test(unittest.TestCase):
    def test_1(self):
        reader = StreamReader()
        reader.track_bulk([5, 1, 4, 4, 5, 9, 7, 13, 3])
        self.assertEqual(0, reader.get_rank(1))
        self.assertEqual(1, reader.get_rank(3))
        self.assertEqual(3, reader.get_rank(4))
        return


if __name__ == '__main__':
    unittest.main()
