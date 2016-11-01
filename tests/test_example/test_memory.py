"""Testing file for network utilities

"""

import unittest
import sys
import os

from os.path import dirname
from os.path import join

sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from simple_example.memory_analysis import get_free_mem_size
from simple_example.memory_analysis import get_total_hd_size



class MemoryTest(unittest.TestCase):
    """Testing class for handling network utils

    """
    def __init__(self, *args, **kwargs):
        """NetworkUtilsTestCase constructor

        """
        super(MemoryTest, self).__init__(*args, **kwargs)

    def setUp(self):
        """setup

        """
        pass

    def tearDown(self):
        """teardown

        """
        pass

    def test_free_memory_check(self):
        assert (get_free_mem_size() > 3)

    def test_total_hd_size(self):
        assert (get_total_hd_size() == '30GB')


