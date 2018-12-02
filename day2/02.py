import sys
import re
from pprint import pprint

id_list = []
for line in sys.stdin:
    try:
        id_list.append(line[:-1])
    except:
        print "Could not parse: %s" % line
        raise

def countSameCharacters(s1, s2):
    index = 0
    if s1 == s2:
        return len(s1)
    while s1[index] == s2[index]:
        index += 1
    return index

for id1, s in enumerate(id_list):
    n = len(s)
    for id2, j in enumerate(id_list[id1:]):
        stride = countSameCharacters(s, j)
        if stride == n:
            continue
        stretch = countSameCharacters(s[stride+1:], j[stride+1:])
        if stride + stretch + 1 == n:
            print '(%d, %d) : %s' % (id1, id2, s[0:stride] + s[stride+1:])
            continue
