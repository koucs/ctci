from random import randint


class Node:

    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values:
            self.add_multiple(values)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def add_to_beginning(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        return self.head

    def add_multiple(self, values):
        for value in values:
            self.add(value)

    def generate(self, n, min_value, max_value):
        self.head = self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self


class DoublyLinkedList(LinkedList):

    def add(self, value):
        if self.head is None:
            self.tail = self.head = Node(value, None, self.tail)
        else:
            self.tail.next = Node(value, None, self.tail)
            self.tail = self.tail.next
        return self

    def add_to_beginning(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            node = Node(value, self.head)
            self.head = node
            node.next.prev = node
        return self.head
