import random
from thing import Thing
from attribute import *

class Weapon(Thing):
  def __init__(self):
    Thing.__init__(self)
    self.at = {} 
    self.df = Dexterity 
    self.dm = Strength 

  def damage(self,user):
    return random.randint(1,user.attributes[self.dm].value)

  def attack(self,user):
    return user.attributes[self.at].value 

  def defend(self,user):
    return user.attributes[self.df].value 

class MartialArts(Weapon):
  def __init__(self):
    Weapon.__init__(self)
    self.at = Karate 

class ProjectileWeapon(Weapon):
  def __init__(self):
    Weapon.__init__(self)
    self.at =Bow 
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
    self.at = Sword 

  def damage(self,user):
    return random.randint(20,50)
