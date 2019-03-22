import sys
from pprint import pprint

class Claim(object):
    def __init__(self, id, x, y, i, j):
        self.id = id
        self.x = x
        self.y = y
        self.i = i
        self.j = j

    def __repr__(self):
        return 'Claim %s: (%d,%d) %dx%d' % (self.id, self.x, self.y, self.i, self.j)

def parseClaim(line):
    # #1 @ 432,394: 29x14
    # ID    X   Y    I  J
    claim_id, atsign, coords, size = line.split(' ')
    # strip '#"
    claim_id = claim_id[1:]
    x, y = coords.split(',')
    # strip ':'
    y = y[:-1]
    x, y = int(x), int(y)
    i, j = size.split('x')
    i, j = int(i), int(j)
    return Claim(claim_id, x, y, i, j)

claims = []
for line in sys.stdin:
    try:
        claims.append(parseClaim(line))
    except:
        print "Could not parse: %s" % line
        raise

fabric = {}
for claim in claims:
    for x in xrange(claim.x, claim.x + claim.i):
        for y in xrange(claim.y, claim.y + claim.j):
            fabric[x] = fabric.get(x, {})
            fabric[x][y] = fabric[x].get(y, [])
            fabric[x][y].append(claim.id)

overlap = 0
for x in fabric:
    for y in fabric[x]:
        if len(fabric[x][y]) > 1:
            overlap += 1

pprint('Total overlap squares: %d' % overlap)
