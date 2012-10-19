from rules import Chance

class Thing(object):
  def __init__(self):
    self.name = ""
    self.x = 0
    self.y = 0
    self.z = 0
    self.height = 0
    self.width = 0
    self.weight = 0
    self.contents = []
    self.location = {}
    self.attributes = {}
    self.style = "?"
  
  def attribute(self,attr,v1,v2):
    self.attributes[attr] = attr(v1,v2)

  def icon(self):
    return self.style
