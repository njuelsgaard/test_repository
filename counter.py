#!usr/bin/env python

import sys

a = list()

def funcPrint(s):
  print(s)
  return
  
for i in range(10):
  funcPrint(i)
  a.append(i)
  
#comp = 4 +10j
#funcPrint(comp.real)
#funcPrint(comp.imag)

b = a
#if b = a, modifications to a will appear in b and vice versa
a[1] = 99
b[2] = -2
print(b)

newDict = {1:"hello",2:"world"}
print(newDict.values())

mylist = ['a','b','c','d','e','e','e','e','e','e']
print(mylist)
print(set(mylist))

myfstring = f"new string has {a[1]} and {4+10j} and {set(mylist)}"
funcPrint(myfstring)

#myfstring becomes a permanent at this point
a[1] = -99
mylist = ['a','b']
print(myfstring)

unpackdict = {1:'first',2:'second',3:'thrid'}
print("This dictionary has 1={1}, 2={2},3={3}".format(**unpackdict))