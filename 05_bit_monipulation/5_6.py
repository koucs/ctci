#! env python
# -*- coding: utf-8 -*-

import unittest


# ctci.5_6
# Date: 2020/10/03
# Filename: 5_6 
# Author: koucs

def swap_odd_even_bits(x: int) -> int:
    # hex(sys.maxsize) = 0x7fffffffffffffff
    even_mask = 0x2AAAAAAAAAAAAAAA
    odd_mask = 0x1555555555555555
    return (x & even_mask) >> 1 | (x & odd_mask) << 1


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(swap_odd_even_bits(0b0101), 0b1010)
        self.assertEqual(swap_odd_even_bits(10), 5)
        self.assertEqual(swap_odd_even_bits(0xCC), 0xCC)
        return


if __name__ == '__main__':
    unittest.main()
