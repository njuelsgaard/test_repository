import math

class Point(object):
  ''' Defines a single point in cartesian space
      Must be cartesian.'''
  def __init__(self,x,y):
    self.x = x
    self.y = y
    
  def distance_to(self,next_p):
    if isinstance(next_p, Point):
      return math.sqrt((next_p.x-self.x)**2+(next_p.y-self.y)**2)