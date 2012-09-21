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
    ic = 0
    for i in range(10000):
      if Chance.win(50,0,25,0):
        ic += 1
    self.failIf(ic < 6000)
def main():
  unittest.main()

if __name__ == "__main__":
  main()
