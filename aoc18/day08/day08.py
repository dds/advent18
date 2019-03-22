from pprint import pprint
import util
import string
from collections import defaultdict
import string

sample_input = """
2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
""".strip()

expected_output = """\
A----------------------------------
    B----------- C-----------
                     D-----
"""

rawdata = util.get_data(8).read().split('\n')
# rawdata = sample_input.split('\n')

data = []

class Node(object):
    def __init__(self):
        self.children = []
        self.metadata = []

    def value(self):
        if not self.children:
            return sum(self.metadata)
        c = 0
        for j in self.metadata:
            i = j-1
            if len(self.children) > i:
                c += self.children[i].value()
        return c

def parseTree(ints):
    index = 0
    assert len(ints) > index+1
    n = Node()
    n_children, n_metadata = ints[index], ints[index+1]
    index += 2
    while n_children > 0:
        step, subtree = parseTree(ints[index:])
        index += step
        n_children -= 1
        n.children.append(subtree)
    for i in range(0, n_metadata):
        n.metadata.append(ints[index])
        index += 1
    return index, n

def parseLine(line):
    ints = list(map(int, line.split()))
    return parseTree(ints)

_, root = parseLine(rawdata[0])
label_i = -1
def printTree(node):
    global label_i
    label_i += 1
    label = string.letters[label_i % len(string.letters)]
    for n in node.children:
        printTree(n)
    pprint('Node: %s, metadata: %s' % (label, node.metadata))

def sumMetadata(node):
    return sum(node.metadata) + sum([sumMetadata(c) for c in node.children])

printTree(root)
pprint('%d' % sumMetadata(root))
pprint('%d' % root.value())
