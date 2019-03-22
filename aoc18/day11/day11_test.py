#!/usr/bin/env python
import heapq
import unittest

from aoc18.day11 import day11


class TestDay11(unittest.TestCase):
    def test_PowerLevel(self):
        assert day11.PowerLevel((122, 79), 57) == -5
        assert day11.PowerLevel((217, 196), 39) == 0
        assert day11.PowerLevel((101, 153), 71) == 4

    def test_TotalPowerLevel(self):
        self.assertEqual(
            day11.PowerLevel((33, 45), 18),
            day11.TotalPowerLevel((33, 45), 1, 18))

        self.assertEqual(day11.TotalPowerLevel((33, 45), 3, 18), 29)
        self.assertEqual(day11.TotalPowerLevel((21, 61), 3, 42), 30)
