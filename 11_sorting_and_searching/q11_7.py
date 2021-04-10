#! env python
# -*- coding: utf-8 -*-

import unittest
from typing import List, Optional


# Cracking The Coding Interview (5th) q11_7
#
# A circus is designing a tower routine consisting of people standing atop one another's shoulders.
# For practical and aesthetic reasons, each person must be both shorter and lighter than the person below him or her.
# Given the heights and weights of each person in the circus,
# write a method to compute the largest possible number of people in such a tower.
#
# EXAMPLE:
# Input (ht,wt):
# (65, 100) (70, 150) (56, 90) (75, 190) (60, 95) (68, 110)
# Output:The longest tower is length 6 and includes from top to bottom:
# (56, 90) (60,95) (65,100) (68,110) (70,150) (75,190)


def get_increasing_subsequence(in_arr: List) -> List:
    sorted_in_arr = sorted(in_arr, key=lambda x: x[0], reverse=False)
    return longest_increasing_subsequence(sorted_in_arr)


def longest_increasing_subsequence(in_arr: List) -> List:
    solutions = [[] for _ in range(len(in_arr))]
    longest_increasing_subsequence_inbounds(in_arr, solutions, 0)
    best_sequence = []
    for i in range(len(in_arr)):
        best_sequence = seq_max_with_length(best_sequence, solutions[i])
    return best_sequence


def longest_increasing_subsequence_inbounds(in_arr: List, solutions: List, current_index: int):
    # O(n^2) algorithm
    if current_index < 0 or len(in_arr) <= current_index:
        return None
    current_element = in_arr[current_index]
    best_sequence = None
    for i in range(current_index):
        if is_before(in_arr[i], current_element):
            best_sequence = seq_max_with_length(best_sequence, solutions[i])

    new_solution = []
    if best_sequence is not None:
        new_solution += best_sequence
    new_solution.append(current_element)

    solutions[current_index] = new_solution
    longest_increasing_subsequence_inbounds(in_arr, solutions, current_index + 1)


def seq_max_with_length(seq1: Optional[List], seq2: Optional[List]) -> Optional[List]:
    if not seq1:
        return seq2
    elif not seq2:
        return seq1
    return seq1 if len(seq1) > len(seq2) else seq2


def is_before(elem1: List, elem2: List) -> bool:
    return True if elem1[0] < elem2[0] and elem1[1] < elem2[1] else False


class Test(unittest.TestCase):
    def test_1(self):
        in_arr = [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)]
        expected = [(56, 90), (60, 95), (65, 100), (68, 110), (70, 150), (75, 190)]
        self.assertEqual(expected, get_increasing_subsequence(in_arr))

        in_arr = [[1, 1], [1, 7], [1, 9], [2, 2], [2, 6], [3, 3], [3, 5], [4, 4]]
        expected = [[1, 1], [2, 2], [3, 3], [4, 4]]
        self.assertEqual(expected, get_increasing_subsequence(in_arr))

        return


if __name__ == '__main__':
    unittest.main()
