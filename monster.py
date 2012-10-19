from rules import Chance
from thing import Thing

class Monster(Thing):
  health= 0
  weapon={}

  def __init__(self):
    super(Monster,self).__init__()

  def die(self):
    self.health = -1

  def dead(self):
    return self.health < 0  

  def attack(self,defender):
    if self.dead(): return
    attack = self.weapon.attack(self) 
    defend = defender.weapon.defend(defender)
    if Chance.win(attack,0,defend,0):
      ammount = self.weapon.damage(self)
      defender.damage(ammount)
      if defender.health < 0: defender.die()

  def damage(self, ammount):
    if self.dead(): return
    self.health -= ammount
