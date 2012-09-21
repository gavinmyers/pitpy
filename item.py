class Item:
  def __init__(self,id,icon,x,y,z):
    self.id = id
    self.icon = icon
    self.x = x
    self.y = y
    self.z = z
  @staticmethod
  def generate(id,icon,x,y,z):
    return Item(id,icon,x,y,z)

class Level:
  def __init__(self):
    self.items = []
  @staticmethod
  def generate():
    return Level()

class World:
  def __init__(self):
    self.levels = []
  @staticmethod
  def generate():
    return World()
