#!/usr/bin/env python3
from functools import reduce

#exercise 1
list1 = [1,2,3,4]
print(list1)

#exercise 2
list1 = [1,2,3,4]
print(len(list1))

#exercise 3
list1 = [1,2,3,4]
def add(x,y): return x+y
sums = reduce(add , list1)
print(sums)

#exercise 4
list1 = [1,2,3,4]
print(list1[::-1])

#exercise 5
list1 = [1,2,3,4]
mult = int(input('exercise5 multiply by?>'))
def multiply(x): return x*mult
sums = map(multiply, list1)
print(list(sums))
