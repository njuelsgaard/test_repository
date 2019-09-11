#!usr/bin/env python

#Day 2 Sandbox script
import math

class Point(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  @property
  def length(self):
    return math.sqrt(self.x**2+self.y**2)

  @property
  def angle(self):
    return math.atan(self.y/self.x)*180/math.pi

  def new_polar(self,length,angle):
    self.x = length*math.cos(angle*math.pi/180)
    self.y = length*math.sin(angle*math.pi/180)

p = Point(y=9,x=12)
print(f"{p.x},{p.y}")
print(p.length)
print(f"{p.angle:0.1f}")
p.new_polar(25,45)
print(f"{p.x},{p.y}")
print(p.length)
print(f"{p.angle:0.1f}")