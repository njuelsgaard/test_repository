#!usr/bin/env python

#Day 2 Sandbox script

class Point(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y


p = Point(y=9,x=12)
print(f"{p.x},{p.y}")