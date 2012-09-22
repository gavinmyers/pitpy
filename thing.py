from rules import Chance

class Thing:
  name = ""
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

  def attack(self, defender):
    attack = self.attributes["KTE"].value 
    defend = defender.attributes["DEX"].value
    if Chance.win(attack,0,defend,0):
      defender.damage(self.attributes["STR"].value)

  def damage(self, ammount):
    self.health -= ammount
