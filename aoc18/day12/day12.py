#!/usr/bin/env python
from aoc18 import util

PLANT = 1
NOPLANT = 0


def parseInitialState(line):
    header = "initial state: "
    assert line.startswith(header)
    line = line[len(header):]
    pots = []
    for c in line.strip():
        if c == '#':
            pots.append(PLANT)
        else:
            pots.append(NOPLANT)
    return pots


class Rule(object):
    def __init__(self, l2, l1, has, r1, r2, res):
        self.l2 = l2
        self.l1 = l1
        self.has = has
        self.r1 = r1
        self.r2 = r2
        self.res = res

    def apply(self, pots, index):
        if not pots:
            pots = [NOPLANT]
        newPots = list(pots)
        i_l2 = index - 2
        i_l1 = index - 1
        i_r2 = index + 2
        i_r1 = index + 1
        e_l2 = (0 <= i_l2 < len(pots)) and pots[i_l2]
        e_l1 = (0 <= i_l1 < len(pots)) and pots[i_l1]
        e_i = (0 <= index < len(pots)) and pots[index]
        e_r1 = (0 <= i_r1 < len(pots)) and pots[i_r1]
        e_r2 = (0 <= i_r2 < len(pots)) and pots[i_r2]
        if all([
                e_l2 == self.l2, e_l1 == self.l1, e_i == self.has,
                e_r1 == self.r1, e_r2 == self.r2
        ]):
            if index == -2:
                newPots = [self.res, 0] + newPots
            elif index == -1:
                newPots = [self.res] + newPots
            elif 0 <= index < len(pots):
                newPots[index] = self.res
            elif index == len(pots):
                newPots = newPots + [self.res]
            else:
                newPots = newPots + [0, self.res]
        return newPots

    def __repr__(self):
        s = (
            "<Rule "
            + ''.join([
                ['.', '#'][c]
                for c in (self.l2, self.l1, self.has, self.r1, self.r2)
            ])
            + ": "
            + ['.', '#'][self.res]
            + ">"
        )
        return s


def parseRule(line):
    args = [c == '#' for c in line[:5]]
    args += [[0, 1][line.strip().endswith('#')]]
    return Rule(*args)


def parseRules(inputfile):
    return [parseRule(line) for line in inputfile]


def regenerate(pots, rules):
    index = -2
    while True:
        if index > len(pots) + 1:
            break
        for rule in rules:
            p = rule.apply(pots, index)
            if len(p) != len(pots):
                index += 1
            pots = p
        index += 1
    return pots


def graphPots(pots):
    output = ''
    for i in pots:
        output += ['.', '#'][i]
    return output
