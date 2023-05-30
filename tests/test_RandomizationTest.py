import unittest

import numpy as np

from manly_randomization_test import RandomizationTest
class TestSimpleCase(unittest.TestCase):

    """ unittest methods for testing """

    def test_empty_file(self):
        """ Test that """

        group1 = np.array([1, 2, 3, 4, 5])
        group2 = np.array([1, 2, 3, 4, 5])

        test = RandomizationTest(group1, group2)
        p_value = test.test()

        self.assertTrue(False)