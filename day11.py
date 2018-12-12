from __future__ import print_function
from pprint import pprint
import util
import string
from collections import defaultdict
import string
import re
import random ; random.seed()
import math
import skimage
import numpy
import matplotlib.pyplot as plt

TEST = False
SAMPLE_INPUT = 18
INPUT = 9306

def getInput():
    if TEST:
        return SAMPLE_INPUT
    else:
        return INPUT

def rackId(x):
    return x + 10

def powerLevel(p):
    x, y = p
    r = rackId(x)
    lvl = r * y
    lvl += getInput()
    lvl = lvl * r
    lvl = (lvl % 1000) / 100
    return lvl - 5

def hood(p, size):
    points = [p]
    X, Y = p
    for i in range(1, size):
        for j in range(1, size):
            x = min(300, X+i)
            y = min(300, Y+i)
            if (x,y) not in points:
                points += [(x,y)]
    return points

caches = []

def fillPowerLevels(size):

def findBestSquare(size):
    best_power = 0
    index_best_power = 0
    if not 0 < size < 301:
        return (0, 0)
    for x in range(1, 301):
        for y in range(1, 301):
            power = sum(powerLevel(p) for p in hood((x,y), size))
            if power > best_power:
                best_power = power
                index_best_power = util.toI((301,301), (x,y))
    return (best_power, util.toC((301, 301), index_best_power))

SQUARE_SIZES = {}

def run():
    for size in range(1, 300):


if __name__ == '__main__':
    run()
