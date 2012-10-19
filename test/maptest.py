#!/usr/bin/env python

import pyglet
import unittest
from map import * 

class u(unittest.TestCase):
  def testSomething(self):
    m = AsciiMap(10,5)
    m.tile(2,1).style = "*"
    m.draw() 

def main():
  unittest.main()

if __name__ == "__main__":
  main()
