#!/usr/bin/env python3

class Empty(object):
    def __init__(self):
        super(Empty, self).__init__()
        self.isEmpty = True

class Node(object):
    def __init__(self, head, tail):
        super(Node, self).__init__()
        self.isEmpty = False
        self.Head = head
        self.Tail = tail



Empty = Empty()

def isEmpty(li):
    if(li.isEmpty):
        return True
    else:
        return False

def length(l):
    global lng
    def calc(li):
        if(li.isEmpty):
            return Empty
        else:
            lng = lng + 1
            return calc(li.Tail)
    calc(l)

def map(li, fn):
    le = len(li)
    x = 0
    ret = []
    while x < le:
        ret.append(fn(li[x], x))
        x = x + 1
    return ret

def filter(li, fn):
    le = len(li)
    x = 0
    ret = []
    while x < le:
        if(fn(li[x])):
            ret.append(li[x])
        x = x + 1
    return ret
l = Node(1, Node(2, Empty))
li = [1,2,3,4]

res = map(li, lambda val, idx:  val * 1)
print(res)

res = filter(li, lambda val: val % 2 == 0)

print(res)
