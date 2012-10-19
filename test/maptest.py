#!/usr/bin/env python

import pyglet
import unittest
from map import * 
from monster import *

class u(unittest.TestCase):
  def testSomething(self):
    diamond = Thing()
    diamond.style = "*"
    player = Monster()
    m = AsciiMap(10,5)
    m.tile(2,1).contents.append(diamond)
    m.tile(2,2).contents.append(player)
    m.draw() 

def main():
  unittest.main()

if __name__ == "__main__":
  main()
