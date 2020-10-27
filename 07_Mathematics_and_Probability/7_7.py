#! env python
# -*- coding: utf-8 -*-

import unittest


# ctci.7_7
# Design an algorithm to find the kth number such that the only prime factors are 3,5, and 7.
# Date: 2020/10/25
# Filename: 7_7 
# Author: koucs

def find_kth_num_of_prime_factors(k: int) -> int:
    # num = 3^a * 5^b * 7^c
    # O(n^2) algorithm
    num_list = [1]
    for i in range(k):
        min_val = 1_000_000
        candidate_prime_factor = None
        for j in num_list:
            if j * 3 < min_val and j * 3 not in num_list:
                min_val = j * 3
            if j * 5 < min_val and j * 5 not in num_list:
                min_val = j * 5
            if j * 7 < min_val and j * 7 not in num_list:
                min_val = j * 7
        num_list.append(min_val)
    return num_list[k - 1]


def find_kth_num_of_prime_factors_ans(k: int) -> int:
    q3 = [3]
    q5 = [5]
    q7 = [7]
    num_list = [1]
    for i in range(k):
        if q3[0] < q5[0] and q3[0] < q7[0]:
            num_list.append(q3.pop(0))
            q3.append(num_list[-1] * 3)
            q5.append(num_list[-1] * 5)
            q7.append(num_list[-1] * 7)
        elif q5[0] < q7[0]:
            num_list.append(q5.pop(0))
            q5.append(num_list[-1] * 5)
            q7.append(num_list[-1] * 7)
        else:
            num_list.append(q7.pop(0))
            q7.append(num_list[-1] * 7)
    return num_list[k - 1]


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, find_kth_num_of_prime_factors(1))
        self.assertEqual(9, find_kth_num_of_prime_factors(5))
        self.assertEqual(63, find_kth_num_of_prime_factors(13))

        self.assertEqual(1, find_kth_num_of_prime_factors_ans(1))
        self.assertEqual(9, find_kth_num_of_prime_factors_ans(5))
        self.assertEqual(63, find_kth_num_of_prime_factors_ans(13))
        return


if __name__ == '__main__':
    unittest.main()
