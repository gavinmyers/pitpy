#!/usr/bin/env python

import pyglet
import unittest
from item import Item 

class u(unittest.TestCase):
  def testTrue(self):
    self.failUnless(True)
  def testFalse(self):
    self.failIf(False)
  def testImport(self):
    item = Item('ID',0,0,0,0)

def main():
  unittest.main()

if __name__ == "__main__":
  main()
