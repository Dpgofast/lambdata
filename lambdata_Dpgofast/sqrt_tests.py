#!/usr/bin/env python

import unittest
from lecture  import *

# newton_sqrt1, newton_sqrt2, lazy_sqrt, builtin_sqrt


class SqrtTests(unittest.TestCase):
    """Obligatory docstring, test square roots!"""
    def test_sqrt9(self):
        self.assertEqual(newton_sqrt1(9), 3)

    def test_sqrt2(self):
        '''Test for equality to newtons square root.'''
        self.assertAlmostEqual(newton_sqrt1(2), 1.41421356237)

if __name__ == '__main__':
    unittest.main()
