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

SAMPLE_INPUT = """
position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>
"""

def parseLine(line):
    pos_x, pos_y, dx, dy = list(map(int, re.findall(r'-?\d+', line)))
    return (pos_x, pos_y), (dx, dy)

class Image(object):
    def __init__(self, points, deltas):
        self.points = points
        self.deltas = deltas

    def rect(self):
        min_xy = (min(p[0] for p in self.points),
                  min(p[1] for p in self.points))
        max_xy = (max(p[0] for p in self.points),
                  max(p[1] for p in self.points))
        return (min_xy, max_xy)

    def dim(self):
        p1, p2 = self.rect()
        return (p2[0] - p1[0]+1, p2[1] - p1[1]+1)

    def size(self):
        dx, dy = self.dim()
        return dx * dy

    def inc(self):
        min_xy, max_xy = self.rect()

        M = []
        D = []
        for i, d in enumerate(self.deltas):
            p = self.points[i]
            q = (p[0] + d[0], p[1] + d[1])
            if (min_xy[0] <= q[0] <= max_xy[0]) and (min_xy[1] <= q[1] <= max_xy[1]):
                M += [q]
                D += [d]
        self.points = M
        self.deltas = D

    def com(self):
        S = len(self.points)
        if S == 0:
            return (0, 0)
        else:
            return (sum(p[0] for p in self.points) / float(S),
                    sum(p[1] for p in self.points) / float(S))

    def mu(self):
        S = len(self.points)
        if S == 0:
            return 0
        com = self.com()
        num = (2/float(S)) * sum(((p[0]-com[0])*(p[1]*com[1])) for p in self.points)
        u0 = sum((p[0]-com[0])**2 for p in self.points)
        u1 = sum((p[1]-com[1])**2 for p in self.points)
        return math.tan(0.5 * math.atan(num / ((1 / float(S)) * (u0 - u1))))

    def dot(self, p1, p2):
        return float((p1[0] * p2[0]) + (p1[1] * p2[1]))

    def mag(self, p):
        return math.sqrt(p[0]*p[0] + p[1]*p[1])

    def linearity(self):
        S = len(self.points)
        if S == 0:
            return 0
        else:
            S = float(S)
        com = self.com()
        u20 = 1/S * sum((p[0]-com[0])**2 for p in self.points)
        u02 = 1/S * sum((p[1]-com[1])**2 for p in self.points)
        u11 = 2/S * sum(((p[0]-com[0])*(p[1]*com[1])) for p in self.points)
        return math.sqrt((u20 - u02)**2 + 4*u11**2) / (u20 + u02)


    # def linearity(self, k=10):
    #     S = len(self.points)
    #     if S == 0:
    #         return 0
    #     p = random.sample(self.points, k*2)
    #     s = []
    #     n = []
    #     M = self.mu()
    #     for i in range(0, len(p)/2):
    #         p1, p2 = p[i], p[i+1]
    #         s += [(p1, p2)]
    #         x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    #         dy, dx = (y2 - y1), (x2 - x1)
    #         r = self.mag((dx, dy))
    #         m = ((-dy/r), (dx/r))
    #         if self.dot((-M, 1), m) + 1 < 0:
    #             m = ((-m[0], -m[1]))
    #         n += [m]
    #     A = 1 / float(S) * (sum(i[0] for i in n))
    #     B = 1 / float(S) * (sum(i[1] for i in n))
    #     return math.sqrt(A**2 + B**2)


    def trl(self):
        min_xy, _ = self.rect()
        x, y = min_xy
        return [(p[0] - x, p[1] - y) for p in self.points]

    def __str__(self):
        dim = self.dim()
        M = self.trl()
        out = ''
        for i in range(0, dim[0]*dim[1]):
            p = util.toC(dim, i)
            if p in M:
                c = '#'
            else:
                c = '.'
            out += c
            if (i+1) % dim[0] == 0:
                out += '\n'
        return out

    def image(self):
        dim = self.dim()
        sf = 12
        i = numpy.ones(((dim[1]+1)/sf, (dim[0]+1)/sf))
        for p in self.trl():
            i[p[1]/sf, p[0]/sf] -= float(1/sf)
            print(i[p[1]/sf, p[0]/sf])
        plt.show(plt.imshow(i, cmap='gray'))


def getInput():
  if TEST:
      return SAMPLE_INPUT.strip().split('\n')
  else:
      return util.get_data(10).read().strip().split('\n')


def parseData():
    def __str__(self):
        out = ''
        print(dim)
        print(Q)
    p, d = [], []
    for l in getInput():
        try:
            t, q = parseLine(l)
        except Exception, e:
            print("Failed parsing \"%s\": %s" % (l, e))
            raise
        p.append(t)
        d.append(q)
    return Image(p, d)

def main():
    data = parseData()
    L = len(data.points)
    turns = 0
    best_size = 0
    size = 1 << 100
    while len(data.points) == L:  # break when we start losing points outside the grid
        if data.size() < 800:
            size = data.size()
            best_size = turns
            print(turns, data)
        data.inc()
        turns += 1
    print('%d turns' % (turns,))

TEST = 0

if __name__ == '__main__':
    main()
