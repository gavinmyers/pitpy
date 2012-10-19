from rules import Chance
from rules import Combat 
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
    
  def damage(self, ammount):
    if self.dead(): return
    self.health -= ammount
    if self.health < 0: self.die()
