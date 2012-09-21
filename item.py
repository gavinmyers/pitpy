class Item:
  def __init__(self,id,icon,x,y,z):
    self.id = id
    self.icon = icon
    self.x = x
    self.y = y
    self.z = z

class Level:
  def __init__(self):
    self.items = []

class World:
  def __init__(self):
    self.levels = []
