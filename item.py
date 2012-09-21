class Item:
  def __init__(self,id,icon,x,y,z,h,w):
    self.id = id
    self.icon = icon
    self.x = x
    self.y = y
    self.z = z
    self.h = h
    self.w = w

class Level:
  def __init__(self,h,w):
    self.items = []
    self.h = h
    self.w = w

class World:
  def __init__(self):
    self.levels = []
