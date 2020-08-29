from typing import List
from enum import Enum


class State(Enum):
    UNVISITED = 1
    VISITED = 2
    VISITING = 3


class GraphNode:
    def __init__(self, data):
        self.data = data
        self.state = State.UNVISITED
        self.adjacent: List[GraphNode] = []


class Graph:
    def __init__(self, nodes: List[GraphNode]):
        self.nodes = nodes

    def reset(self):
        for n in self.nodes: n.visited = State.UNVISITED
