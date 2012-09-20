#!/usr/bin/env python

import pyglet
import unittest

class u(unittest.TestCase):
  def testTrue(self):
    self.failUnless(True)
  def testFalse(self):
    self.failIf(False)

unittest.main()
