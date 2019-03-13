# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 16:55:02 2018

@author: C5232886
"""

import unittest
from target_gre_dec_27 import is_prime

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(validate_mount_point(['aba']))

if __name__ == '__main__':
    unittest.main()