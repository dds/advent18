#!/usr/bin/env python2
import heapq

from aoc18 import util

TEST = False
SAMPLE_INPUT = 18
INPUT = 9306

_coords_cache = {}


def PowerLevel(coords, serial):
    global _coords_cache
    c = _coords_cache.get(coords, None)
    if c is None:
        x, y = coords
        power = (x + 10) * (x * y + 10 * y + serial)
        power = (int(power / 100) % 10)
        power = power - 5
        c = _coords_cache[coords] = power
    return c


grid = {}


def CreatePowerGrid(serial):
    global grid
    grid[(0, 0)] = PowerLevel((0, 0), serial)
    for ii in range(1, 301):
        grid[(0, ii)] = grid[(0, ii - 1)] + PowerLevel((1, ii + 1), serial)
        grid[(ii, 0)] = grid[(ii - 1, 0)] + PowerLevel((ii + 1, 1), serial)
    for ii in range(1, 301):
        for jj in range(1, 301):
            p = PowerLevel((ii + 1, jj + 1), serial)
            s = grid[(ii - 1, jj)] + grid[(ii,
                                           jj - 1)] - grid[(ii - 1), jj - 1]
            grid[(ii, jj)] = p + s


def TotalPowerLevel(origin, size, serial):
    o_x, o_y = origin
    power = 0
    for x in range(o_x, o_x + size):
        for y in range(o_y, o_y + size):
            power += PowerLevel((x, y), serial)
    return power


def Part2PowerLevels(serial):
    global grid
    CreatePowerGrid(serial)
    for size in range(1, 301):
        for i in range(0, 301 - size):
            for j in range(0, 301 - size):
                aa = grid[(i, j)]
                bb = grid[(i + size, j)]
                cc = grid[(i, j + size)]
                dd = grid[(i + size, j + size)]
                power = aa - bb - cc + dd
                yield (i + 2, j + 2, size), power


if __name__ == '__main__':
    soln = heapq.nlargest(
        1, enumerate(Part2PowerLevels(9306)), key=lambda i: i[1][1])[0]
    print(soln)
