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

hasThreeLetters = {}
hasTwoLetters = {}

for i in id_list:
    chars = ''.join(sorted(i))
    charlen = len(chars)
    index = 0
    for c in chars:
        stridelen = 0
         while True:
            if index+stridelen >= charlen:
                break
            if chars[index+stridelen] == c:
                stridelen += 1
            else:
                break
        index += stridelen
        if stridelen == 3:
            hasThreeLetters[i] = 1
            next
        if stridelen == 2:
            hasTwoLetters[i] = 1
            next

pprint(hasThreeLetters)
pprint(hasTwoLetters)

print 'Checksum %d' % (len(hasThreeLetters) * len(hasTwoLetters))
