import util
from string import lowercase

test_input = """
aA
abBA
aBAB
aabAAB
dabAcCaCBAcCcaDA
"""
def reaction(left, right):
    if left != right and (ord(left) % 32) == (ord(right) % 32):
        return True
    return False

def reactPolymer(polymer):
    index = 1
    while True:
        if len(polymer) == 0 or index >= len(polymer):
            break
        if reaction(polymer[index-1], polymer[index]):
            polymer = polymer[0:index-1] + polymer[index+1:]
            index -= 1
        else:
            index += 1
    return polymer

polymers = []
for line in util.get_data(5).read().split('\n'):
# for line in test_input.split('\n'):
    polymer = line
    if not polymer:
        continue
    polymers.append(polymer)

def removeUnit(polymer, unit):
    index = 0
    while True:
        if len(polymer) == 0 or index >= len(polymer):
            break
        if ord(polymer[index]) % 32 == ord(unit) % 32:
            polymer = polymer[:index] + polymer[index+1:]
        else:
            index += 1
    return polymer

for polymer in polymers:
    reactedPolymer = reactPolymer(polymer)
    print 'A: %d' % len(reactedPolymer)
    reducedPolymers = [removeUnit(polymer, c) for c in lowercase]
    print 'got reducedPolymers'
    reactedReducedPolymers = []
    for i, p in enumerate(reducedPolymers):
        reactedReducedPolymers.append(reactPolymer(p))
        print 'got %s reduced polymers' % chr(ord('a') + i)
    index, bestReducedPolymer = util.best([len(i) for i in reactedReducedPolymers], True)
    print 'B: %d (worst unit: %s)' % (bestReducedPolymer, chr(ord('a') + index))
