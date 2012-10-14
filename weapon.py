import random
from thing import Thing

class Weapon(Thing):
  def __init__(self):
    self.at = "" 
    self.df = "DEX" 
    self.dm = "STR"

  def damage(self,user):
    return random.randint(1,user.attributes[self.dm].value)

  def attack(self,user):
    return user.attributes[self.at].value 

  def defend(self,user):
    return user.attributes[self.df].value 

class MartialArts(Weapon):
  def __init__(self):
    Weapon.__init__(self)
    self.at = "KTE" 

class ProjectileWeapon(Weapon):
  def __init__(self):
    Weapon.__init__(self)
    self.at = "BOW"
    self.projectiles = 100

  def attack(self,user):
    if self.projectiles == 0: return 0
    self.projectiles -= 1
    return user.attributes[self.at].value 

  def defend(self,user):
    return user.attributes[self.df].value / 2 

  def damage(self,user):
    if self.projectiles == 0: return 0
    return random.randint(20,50)

class BladeWeapon(Weapon):
  def __init__(self):
    Weapon.__init__(self)
    self.at = "BLD"

  def attack(self,user):
    return user.attributes[self.at].value 

  def defend(self,user):
    return user.attributes[self.df].value  

  def damage(self,user):
    return random.randint(20,50)
