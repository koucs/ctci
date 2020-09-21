#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
from enum import Enum
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest


# ctci.3_7
# Date: 2020/08/16
# Filename: 3_7 
# Author: koucs

class AnimalEnum(Enum):
    CAT = 1
    DOG = 2


class Animal():
    def __init__(self, enum: AnimalEnum):
        self.enum = enum

    def set_order(self, order):
        self.order = order

    def get_order(self):
        return self.order


class AnimalQueue():
    def __init__(self):
        self.order = 0
        self.cat_queue = []
        self.dog_queue = []

    def enqueue(self, animal: Animal):
        animal.set_order(self.order)
        self.order += 1
        if animal.enum == AnimalEnum.DOG:
            self.dog_queue.append(animal)
        else:
            self.cat_queue.append(animal)

    def dequeue_any(self):
        if len(self.dog_queue) == 0 and len(self.cat_queue) == 0:
            return None
        elif len(self.dog_queue) == 0 and len(self.cat_queue) > 0:
            return self.dequeue_cat()
        elif len(self.dog_queue) > 0 and len(self.cat_queue) == 0:
            return self.dequeue_dog()

        dog = self.dog_queue[0]
        cat = self.cat_queue[0]

        if dog.get_order() <= cat.get_order():
            return self.dequeue_dog()
        else:
            return self.dequeue_cat()

    def dequeue_dog(self):
        return self.dog_queue.pop(0)

    def dequeue_cat(self):
        return self.cat_queue.pop(0)


class Test(unittest.TestCase):
    def test_1(self):
        queue = AnimalQueue()
        queue.enqueue(Animal(AnimalEnum.DOG))
        queue.enqueue(Animal(AnimalEnum.DOG))
        queue.enqueue(Animal(AnimalEnum.CAT))
        queue.enqueue(Animal(AnimalEnum.CAT))
        queue.enqueue(Animal(AnimalEnum.CAT))

        self.assertEqual(AnimalEnum.CAT, queue.dequeue_cat().enum)
        self.assertEqual(AnimalEnum.DOG, queue.dequeue_any().enum)
        self.assertEqual(AnimalEnum.DOG, queue.dequeue_dog().enum)
        self.assertEqual(AnimalEnum.CAT, queue.dequeue_any().enum)
        self.assertEqual(AnimalEnum.CAT, queue.dequeue_any().enum)
        self.assertEqual(None, queue.dequeue_any())
        return


if __name__ == '__main__':
    unittest.main()
