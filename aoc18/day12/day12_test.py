import io
import unittest

from aoc18 import util
from aoc18.day12 import day12


class Day12Test(unittest.TestCase):
    def test_import(self):
        pass

    def test_getInput(self):
        print(util.getInput(12))

    def test_getTestInput(self):
        print(util.getInput(12, 1))

    def test_parseInput(self):
        print(day12.parseInitialState(util.getInput(12, 1).readline()))
        print(day12.parseRule("...## => #"))

    def test_apply(self):
        pots = day12.parseInitialState("initial state: #")
        rule = day12.parseRule("....# => #")
        self.assertListEqual([1, 0, 1], rule.apply(pots, -2))

        rule = day12.parseRule("...#. => #")
        self.assertListEqual([1, 1], rule.apply(pots, -1))

        rule = day12.parseRule("#.... => #")
        self.assertListEqual([1, 0, 1], rule.apply(pots, 2))

        rule = day12.parseRule(".#... => #")
        self.assertListEqual([1, 1], rule.apply(pots, 1))

        pots = day12.parseInitialState(
            "initial state: #..#.#..##......###...###")
        rules = [
            day12.parseRule(i) for i in [
                "...## => #",
                "..#.. => #",
                ".#... => #",
                ".#.#. => #",
                ".#.## => #",
                ".##.. => #",
                ".#### => #",
                "#.#.# => #",
                "#.### => #",
                "##.#. => #",
                "##.## => #",
                "###.. => #",
                "###.# => #",
                "####. => #",
            ]
        ]
        self.assertEqual(
            day12.graphPots(pots), day12.graphPots(rules[1].apply(pots, 0)))

    def test_regenerate(self):
        data = util.getInput(12, 0).read().split('\n')
        pots = day12.parseInitialState(data[0])
        rules = [day12.parseRule(l) for l in data[1:] if l.strip()]
        newPots = day12.regenerate(pots, rules)
        print('')
        print(day12.graphPots(pots))
        print(day12.graphPots(newPots))
