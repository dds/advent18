import util
from string import ascii_lowercase as lowercase
from collections import defaultdict
import string

sample_input = """
1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
"""

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def parseCoords(line):
    return list(map(int, line.split(',')))


centers = []
maxdim = 0
# for i, line in enumerate(sample_input.split('\n')):
for i, line in enumerate(util.get_data(6).read().split('\n')):
    if not line:
      continue
    coords = parseCoords(line)
    maxdim = max(maxdim, coords[0], coords[1])
    centers.append(coords)

dimensions = [maxdim, maxdim]

def toI(c):
    return c[1] * dimensions[1] + c[0]

board = [-1] * toI(dimensions)

def toC(i):
    quotient, remainder = divmod(i, dimensions[1])
    return remainder, quotient

areas = defaultdict(int)
infiniteAreas = {}

def edgePoint(p):
    if p[0] == 0 or p[0] == dimensions[0] or p[1] == 0 or p[1] == dimensions[1]:
        return True
    return False

def printBoard():
    stringBoard = ''
    for i, c in enumerate(board):
        stringBoard += c
        if (i + 1) % dimensions[1] == 0:
            stringBoard += '\n'
    print(stringBoard)

total_region = 0

for i in range(0, toI(dimensions)):
    c = toC(i)
    distances = [distance(c, p) for p in centers]
    index, value = util.best(distances, worst=True)
    distance_sum = sum(distances)
    if distance_sum < 10000:
        total_region += 1
    del distances[index]
    if edgePoint(c):
        infiniteAreas[index] = 1
    if not value in distances:
        areas[index] += 1

for i in infiniteAreas:
    del areas[i]
print(util.best(list(areas.values()))[1])
print(total_region)
