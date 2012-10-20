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
    bigrock = Thing()
    bigrock.height=2
    bigrock.width=2
    bigrock.style="#"
    m = AsciiMap(10,5)
    m.tile(2,1).contents.append(diamond)
    m.tile(2,2).contents.append(player)
    m.tile(3,3).contents.append(bigrock)
    m.tile(3,4).contents.append(bigrock)
    m.tile(4,4).contents.append(bigrock)
    m.tile(4,3).contents.append(bigrock)
    m.draw() 

def main():
  unittest.main()

if __name__ == "__main__":
  main()
