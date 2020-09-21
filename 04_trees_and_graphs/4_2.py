#! env python
# -*- coding: utf-8 -*-

import unittest
from graph import *


# ctci.4_2
# Date: 2020/08/29
# Filename: 4_2 
# Author: koucs


def search_bfs(g: Graph, start: GraphNode, end: GraphNode) -> bool:
    q = []
    start.visited = State.VISITED
    q.append(start)
    while len(q) != 0:
        u: GraphNode = q.pop(0)  # dequeue
        if u is not None:
            for v in u.adjacent:
                if v.state == State.UNVISITED:
                    if v == end:
                        return True
                    else:
                        v.state = State.VISITED
                        q.append(v)
            u.state = State.VISITED

    return False


class Test(unittest.TestCase):
    def test_1(self):
        node1 = GraphNode(1)
        node2 = GraphNode(2)
        node3 = GraphNode(3)
        node4 = GraphNode(4)
        node1.adjacent.append(node2)
        node2.adjacent.append(node3)
        node4.adjacent.append(node3)
        # 1 --> 2 --> 3 <-- 4
        graph1 = Graph([node1, node2, node3, node4])

        self.assertEqual(search_bfs(graph1, node2, node3), True)
        self.assertEqual(search_bfs(graph1, node2, node4), False)

        return


if __name__ == '__main__':
    unittest.main()
