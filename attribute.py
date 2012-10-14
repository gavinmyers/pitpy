class Attribute(object):
  def __init__(self,name,code,value,step):
    self.name = name 
    self.code = code 
    self.value = value 
    self.step = step 

class Strength(Attribute):
  def __init__(self,value,step):
    super(Strength,self).__init__("Strength","STR",value,step)

class Dexterity(Attribute):
  def __init__(self,value,step):
    super(Dexterity,self).__init__("Dexterity","DEX",value,step)

class Karate(Attribute):
  def __init__(self,value,step):
    super(Karate,self).__init__("Karate","KTE",value,step)

class Bow(Attribute):
  def __init__(self,value,step):
    super(Bow,self).__init__("Bow","BOW",value,step)

class Sword(Attribute):
  def __init__(self,value,step):
    super(Sword,self).__init__("Sword","BLD",value,step)
