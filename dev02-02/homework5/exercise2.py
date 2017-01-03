#!/usr/bin/env python3

class Empty(object):
    def __init__(self):
        super(Empty, self).__init__()
    def __str__(self): return "[]"
    def isEmpty(self): return True
    def Length(self): return 0
    def Sum(self): return 0
    def Map(self, fn): return self
    def Filter(self, p): return self
    def Fold(self, f, z): return z

class Node(object):
    def __init__(self, head, tail):
        super(Node, self).__init__()
        self.head = head
        self.tail = tail
    def __str__(self):
        return str(self.head) + " << " + str(self.tail)
    def IsEmpty(self): return False
    def Head(self): return self.head
    def Tail(self): return self.tail
    def Sum(self):
        return self.head + self.tail.Sum()
    def Length(self):
        return 1 + self.tail.Length()
    def Map(self, fn):
        return Node(fn(self.head), self.tail.Map(fn))
    def Filter(self, p):
        l = self.tail.Filter(p)
        if p(self.head):
            return Node(self.head, l)
        else:
            return l
    def Fold(self, f, z):
        return f(self.head, self.tail.Fold(f,z))

Empty = Empty()

l = Node(5, Node(9, Node(-1, Empty)))

#exercise 2
empty = l.IsEmpty()
ln = l.Length()
sm = l.Sum()
print("exercise 2 List results \n isEmpty: {0} \n Length: {1} \n Sum: {2} \n".format(empty, ln, sm))

#exercise 3
mp = l.Map(lambda x:  x + 2)
fl = l.Filter(lambda x: x % 3 == 0)
print("exercise 3 List results \n Map: {0} \n Filter: {1}".format(mp, fl))

#exercise 4
fold = l.Fold(lambda x, y: x+y, 0)
print(fold)
