from pprint import pprint
import util
import string
from collections import defaultdict
import string

Test = 0
PlayerCount = 405
LastMarblePoints = 7170000

if Test:
  PlayerCount = 9
  LastMarblePoints = 25


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        left = ' ' or repr(self.prev)
        right = ' ' or repr(self.next)
        return '%s%d%s' % (left, self.value, right)

class CircleList(object):
    def __init__(self):
        self._head = None
        self._tip = None

    def add(self, new):
        prev = self._tip
        if prev:
            new.next = prev.next
            prev.next = new
            new.prev = prev
            new.next.prev = new
            self._tip = new
        else:
            self._head = self._tip = new.prev = new.next = new
        #print self._tip.prev.value, self._tip.value, self._tip.next.value

    def add2(self, node):
        self._tip = self._tip.next
        self.add(node)

    def rem(self):
        t = self._tip
        l = self._tip.prev
        r = self._tip.next
        # print l.value, t.value, r.value
        l.next = r
        r.prev = l
        self._tip = r
        #print self._tip.prev.value, self._tip.value, self._tip.next.value
        return t

    def rem7(self):
        for _ in range(0, 7):
            # print self._tip.prev.value, self._tip.value, self._tip.next.value
            self._tip = self._tip.prev
        return self.rem()

    def __repr__(self):
        ints = []
        t = self._head
        start = self._head.value
        while True:
            ints.append(t.value)
            t = t.next
            if t.value == start:
                break
        return '[' + ', '.join(map(str, ints)) + ']'

circle = CircleList()
circle.add(Node(0))

def play():
    curMarble = maxMarble = 1
    scores = defaultdict(int)
    turn = 0
    while maxMarble < LastMarblePoints:
        player = turn % PlayerCount
        if curMarble % 23:
            circle.add2(Node(curMarble))
        else:
            scores[player] += curMarble + circle.rem7().value

        turn += 1
        maxMarble = max(maxMarble, curMarble)
        if turn >= maxMarble:
            curMarble = maxMarble + 1
        # print turn, player+1, circle

    best = bestPlayer = 0
    for k, v in scores.items():
        if v > best:
            best = v
            bestPlayer = k
    print best, bestPlayer

if __name__ == '__main__':
    play()
