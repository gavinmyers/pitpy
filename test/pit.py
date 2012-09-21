#!/usr/bin/env python

import pyglet
import unittest
from item import * 
from rules import *

class u(unittest.TestCase):
  def testTrue(self):
    self.failUnless(True)
  def testFalse(self):
    self.failIf(False)
  def testImport(self):
    item = Item('ID',0,0,0,0,1,1)
    self.failIf(item.icon == 5)
    self.failUnless(item.icon == 0)
  def testNewLevel(self):
    level = Level(25,25)
    self.failIf(level == None)
    self.failIf(level.items == None)
  def testNewWorld(self):
    world = World()
    self.failIf(world == None)
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
    for i in range(10000):
      if Chance.win(6,0,4,0): ic1 += 1
      if Chance.win(4,1,4,0): ic2 += 1
      if Chance.win(4,0,4,0): ic3 += 1
      if Chance.over(100,50): ic4 += 1
      if Chance.over(100,25): ic5 += 1
      if Chance.match(10,1):  ic6 += 1
    self.failIf(ic1 < 6000)
    self.failIf(ic2 > 5000)
    self.failIf(ic3 < 5000)
    self.failIf(ic4 < 4000 or ic4 > 6000)
    self.failIf(ic5 < 7250)
    self.failIf(ic6 > 1500)
def main():
  unittest.main()

if __name__ == "__main__":
  main()
