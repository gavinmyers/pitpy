#!/usr/bin/env python

import pyglet
import unittest
from thing import * 
from monster import *
from weapon import *
from rules import *
from deck import *
from attribute import *

class u(unittest.TestCase):
  def testBattle(self):
    bowman = Monster()
    bowman.name = "Bow Man"
    bowman.weapon = ProjectileWeapon()
    bowman.attribute(Strength,0,0)
    bowman.attribute(Bow,100,0)  
    bowman.attribute(Dexterity,250,0)
    bowman.health = 16

    swordsman = Monster()
    swordsman.name = "Swords Guy"
    swordsman.weapon = BladeWeapon()
    swordsman.attribute(Strength,0,0)
    swordsman.attribute(Sword,100,0)  
    swordsman.attribute(Dexterity,250,0)
    swordsman.health = 16

    miyagi = Monster()
    miyagi.name = "Mr. Miyagi"
    miyagi.weapon = MartialArts()
    miyagi.attribute(Strength,250,0)
    miyagi.attribute(Dexterity,250,0)
    miyagi.attribute(Karate,250,0)
    miyagi.health = 16 

    daniel = Monster()
    daniel.name = "Daniel"
    daniel.weapon = MartialArts()
    daniel.attribute(Strength,100,0)
    daniel.attribute(Dexterity,100,0)
    daniel.attribute(Karate,100,0)
    daniel.health = 16
    deadMiyagis = 0
    deadDaniels = 0
    deadSwordsmen = 0
    deadBowmen = 0
    for i in range(2500):
      swordsman.attack(bowman)
      if bowman.health < 1: 
        deadBowmen += 1 
        bowman.health = 16
        swordsman.health = 16
      bowman.attack(swordsman)
      if swordsman.health < 1:
        deadSwordsmen += 1
        bowman.health = 16
        swordsman.health = 16

      daniel.attack(miyagi)
      if miyagi.health < 1: 
        deadMiyagis += 1 
        miyagi.health = 16
        daniel.health = 16
      miyagi.attack(daniel)
      if daniel.health < 1:
        deadDaniels += 1
        miyagi.health = 16
        daniel.health = 16
    #print str(deadMiyagis) + " vs " + str(deadDaniels)
    #print str(deadBowmen) + " vs " + str(deadSwordsmen)
    self.failIf(deadMiyagis > deadDaniels)
    self.failIf(deadSwordsmen > deadBowmen)
    self.failIf(deadSwordsmen > 100)
def main():
  unittest.main()

if __name__ == "__main__":
  main()
