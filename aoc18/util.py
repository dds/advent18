import heapq
import inspect
import os

import aoc18


def best(data, worst=False):
    f = heapq.nlargest if not worst else heapq.nsmallest
    return f(1, iterable=enumerate(data), key=lambda i: i[1])[0]


def getInput(day, test=False):
    path = os.path.dirname(os.path.abspath(inspect.getfile(aoc18)))
    filename = 'input.txt' if not test else 'test_input.txt'
    return open('%s/day%02d/%s' % (path, day, filename))


def toI(dim, c):
    return c[1] * dim[0] + c[0]


def toC(dim, i):
    q, r = divmod(i, dim[0])
    return (r, q)


def parseCoords(line):
    return list(map(int, line.split(',')))


def neighbors(c):
    return [(c[0] - 1, c[1]), (c[0] + 1, c[1]), (c[0], c[1] - 1),
            (c[0], c[1] + 1)]


def neighbors8(c):
    return neighbors(c) + [(c[0] - 1, c[1] - 1), (c[0] + 1, c[1] - 1),
                           (c[0] - 1, c[1] + 1), (c[0] + 1, c[1] + 1)]


# def edgePoint(p):
#     if p[0] == 0 or p[0] == dimensions[0] or p[1] == 0 or p[1] == dimensions[1]:
#         return True
#     return False


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
