#!/usr/bin/env python

import pyglet
import unittest
from thing import * 
from rules import *
from attribute import *

class u(unittest.TestCase):
  def testTrue(self):
    self.failUnless(True)
  def testFalse(self):
    self.failIf(False)
  def testImport(self):
    item = Thing()
    self.failIf(item.icon == 5)
    self.failUnless(item.icon == 0)
    player = Player()
    self.failUnless(player.health == 0)
  def testRules(self):
    self.failUnless(Chance.over(0,-1) == True)
    self.failUnless(Chance.match(0,0) == True)
    self.failUnless(Chance.win(1,0,0,0) == True)
    ic1 = 0
    ic2 = 0
    ic3 = 0
    ic4 = 0
    ic5 = 0
    ic6 = 0
    ic7 = 0
    for i in range(10000):
      if Chance.win(6,0,4,0): ic1 += 1
      if Chance.win(4,1,4,0): ic2 += 1
      if Chance.win(4,0,4,0): ic3 += 1
      if Chance.over(100,50): ic4 += 1
      if Chance.over(100,25): ic5 += 1
      if Chance.match(10,1):  ic6 += 1
      ic7 += Chance.value(10)
    self.failIf(ic1 < 6000)
    self.failIf(ic2 > 5000)
    self.failIf(ic3 < 5000)
    self.failIf(ic4 < 4000 or ic4 > 6000)
    self.failIf(ic5 < 7250)
    self.failIf(ic6 > 1500)
    self.failIf(ic7 < 47000)
  def testBattle(self):
    miyagi = Player()
    miyagi.name = "Mr. Miyagi"
    miyagi.attributes = {} 
    miyagi.attributes["STR"] = Strength(4,0)
    miyagi.attributes["DEX"] = Dexterity(8,0)
    miyagi.attributes["KTE"] = Karate(8,0)
    miyagi.health = 16 
    daniel = Player()
    daniel.name = "Daniel"
    daniel.attributes = {} 
    daniel.attributes["STR"] = Strength(4,0)
    daniel.attributes["DEX"] = Dexterity(4,0)
    daniel.attributes["KTE"] = Karate(4,0)
    daniel.health = 16
    deadMiyagis = 0
    deadDaniels = 0
    for i in range(10000):
      daniel.attack(miyagi)
      miyagi.attack(daniel)
      if miyagi.health < 1: 
        deadMiyagis += 10 
        miyagi.health = 16
        daniel.health = 16
      if daniel.health < 1:
        deadDaniels += 1
        miyagi.health = 16
        daniel.health = 16
    self.failIf(deadMiyagis > deadDaniels)
def main():
  unittest.main()

if __name__ == "__main__":
  main()
