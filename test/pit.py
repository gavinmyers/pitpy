#!/usr/bin/env python

import pyglet
import unittest
from item import * 

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
def main():
  unittest.main()

if __name__ == "__main__":
  main()
