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

claim_list = []
for line in file('input.txt'):
    try:
        claim_list.append(parseClaim(line))
    except:
        print "Could not parse: %s" % line
        raise

fabric = {}


for claim in claim_list:
    for x in xrange(claim.x, claim.x + claim.i):
        for y in xrange(claim.y, claim.y + claim.j):
            fabric[x] = fabric.get(x, {})
            fabric[x][y] = fabric[x].get(y, [])
            fabric[x][y].append(claim.id)

overlapping_claims = {}
for x in fabric:
    for y in fabric[x]:
        if len(fabric[x][y]) > 1:
            for id in fabric[x][y]:
                claims = overlapping_claims.get(id, set())
                claims.add((x,y))
                overlapping_claims[id] = claims

def borderBox(claim):
    """Returns the list of points that border a claim"""
    left_edge = claim.x - 1
    right_edge = claim.x + claim.i + 1
    top_edge = claim.y - 1
    bottom_edge = claim.y + claim.j + 1
    border_points = set()
    for i in xrange(claim.x - 1, claim.x + claim.i + 1):
        border_points.add((i, top_edge))
        border_points.add((i, bottom_edge))
    for j in xrange(claim.y - 1, claim.y + claim.j + 1):
        border_points.add((left_edge, j))
        border_points.add((right_edge, j))
    return sorted(border_points)

# for claim in claim_list:
#     bordering_claim = False
#     bordering_claims = {}
#     for (x,y) in borderBox(claim):
#         if not fabric.get(x):
#             continue
#         if not fabric[x].get(y):
#             continue
#         square = fabric[x].get(y)
#         bordering_claims.get(claim.id, []).extend(tmp)
#     if not bordering_claim and not overlapping_claims.get(claim.id):
#         pprint('Claim %s has no bordering claims and no overlapping claims' % claim.id)

for claim in claim_list:
    if claim.id not in overlapping_claims:
        print claim.id
