import inspect
import os
import unittest

from aoc18 import util


class UtilTest(unittest.TestCase):

    def test_getInput(self):
        util.getInput(1)
        with self.assertRaises(IOError) as cm:
            util.getInput(99)
        print(cm.exception)
