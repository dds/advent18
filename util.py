def best(data, worst=False):
    index = best = 0
    best = data[index]
    for i in range(0, len(data)):
        if (worst and (data[i] < best)) or (not worst and data[i] > best):
            best = data[i]
            index = i
    return index, best
def get_data(day):
    return open('/home/dds/src/dds/advent18/%d/input.txt' % day)

def toI(dim, c):
    return c[1] * dim[1] + c[0]
def toC(dim, c):
    q, r = divmod(i, dim[1])
    return r, q
def parseCoords(line):
    return list(map(int, line.split(',')))
def neighbors(c):
    return [(c[0]-1, c[1]),
            (c[0]+1, c[1]),
            (c[0], c[1]-1),
            (c[0], c[1]+1)]
def neighbors8(c):
    return neighbors(c) + [(c[0]-1, c[1]-1),
                           (c[0]+1, c[1]-1),
                           (c[0]-1, c[1]+1),
                           (c[0]+1, c[1]+1)]
def edgePoint(p):
    if p[0] == 0 or p[0] == dimensions[0] or p[1] == 0 or p[1] == dimensions[1]:
        return True
    return False
