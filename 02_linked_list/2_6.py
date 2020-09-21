#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest
from linked_list import LinkedList, Node


# ctci.2_6
# Date: 2020/08/15
# Filename: 2_6 
# Author: koucs

def find_loop_node(link_list):
    slow = link_list.head
    fast = link_list.head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if fast == None or fast.next == None:
        return None

    slow = link_list.head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


class Test(unittest.TestCase):
    def test_find_loop_node(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)
        n6 = Node(6)
        n7 = Node(7)
        n8 = Node(8)
        n9 = Node(9)
        n10 = Node(10)
        n11 = Node(11)

        l1 = LinkedList()
        l1.head = n1
        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5
        n5.next = n6
        n6.next = n7
        n7.next = n8
        n8.next = n9
        n9.next = n10
        n10.next = n11
        n11.next = n6
        actual = find_loop_node(l1)
        self.assertEqual(actual, n6)

        l1 = LinkedList()
        l1.head = n1
        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5
        n5.next = n6
        n6.next = n7
        n7.next = n8
        n8.next = n9
        n9.next = n10
        n10.next = n11
        n11.next = n8
        actual = find_loop_node(l1)
        self.assertEqual(actual, n8)


if __name__ == '__main__':
    unittest.main()
