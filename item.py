class Attribute:
  name = ""
  code = ""
  value = 0
  step = 0

class Strength(Attribute):
  def __init__(self,value,step):
    self.name = "Strength"
    self.code = "STR"
    self.value = value
    self.step = step

class Dexterity(Attribute):
  def __init__(self,value,step):
    self.name = "Dexterity"
    self.code = "DEX"
    self.value = value

class Karate(Attribute):
  def __init__(self,value,step):
    self.name = "Karate"
    self.code = "KTE"
    self.value = value

class Thing:
  icon = 0
  x = 0
  y = 0
  z = 0
  height = 0
  width = 0
  weight = 0
  contents = []
  attributes = {} 

class Player(Thing):
  health= 0

