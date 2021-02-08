#! env python
# -*- coding: utf-8 -*-

import copy
import unittest
from typing import List

# ctci.q9_9
# Date: 2021/01/31
# 9.9. Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
# so that none of them share the same row, column or diagonal.
# In this case, "diagonal" means all diagonals, not just the two that bisect the board.

BOARD_SIZE = 8


class Board:
    def __init__(self):
        self.board = [-1] * BOARD_SIZE

    def print(self):
        for row in self.board:
            for column in range(BOARD_SIZE):
                print(" {} ".format("Q" if row == column else "_"), end='')
            print('')

    def str(self):
        result = "\n"
        for row in self.board:
            for column in range(BOARD_SIZE):
                result += " {} ".format("Q" if row == column else "_")
            result += "\n"
        return result


def place_queen(row: int, board: Board, results: List):
    if row == BOARD_SIZE:
        results.append(copy.deepcopy(board))
    else:
        for column in range(BOARD_SIZE):
            if check(board, row, column):
                board.board[row] = column
                place_queen(row + 1, board, results)


def check(board: Board, row: int, column: int) -> bool:
    for i in range(row):
        q = board.board[i]

        if q == column:
            return False

        if (row - i) == abs(column - q):
            return False
    return True


class Test(unittest.TestCase):
    def test_1(self):
        results = []
        place_queen(0, Board(), results)
        self.assertEqual(len(results), 92)
        self.assertEqual("""
 Q  _  _  _  _  _  _  _ 
 _  _  _  _  Q  _  _  _ 
 _  _  _  _  _  _  _  Q 
 _  _  _  _  _  Q  _  _ 
 _  _  Q  _  _  _  _  _ 
 _  _  _  _  _  _  Q  _ 
 _  Q  _  _  _  _  _  _ 
 _  _  _  Q  _  _  _  _ 
""", results[0].str())
        return


if __name__ == '__main__':
    unittest.main()
