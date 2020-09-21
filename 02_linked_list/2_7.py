#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest
from linked_list import LinkedList, Node


# ctci.2_7
# Date: 2020/08/15
# Filename: 2_7 
# Author: koucs

def palindrome(doubly):
    palindrome = False

    slow = doubly.head
    fast = doubly.head
    stack = []

    while fast is not None and fast.next is not None:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    # 要素数が奇数の場合は真ん中の値は飛ばす
    if fast != None:
        slow = slow.next

    while slow.next is not None:
        if slow.value != stack.pop():
            return False
        slow = slow.next

    return True


class Test(unittest.TestCase):
    def test_1(self):
        linked_list = LinkedList("kayak")
        actual = palindrome(linked_list)
        self.assertEqual(actual, True)

        linked_list = LinkedList("canoe")
        actual = palindrome(linked_list)
        self.assertEqual(actual, False)
        return


if __name__ == '__main__':
    unittest.main()
