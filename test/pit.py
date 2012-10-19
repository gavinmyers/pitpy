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
  def testTrue(self):
    self.failUnless(True)
  def testFalse(self):
    self.failIf(False)
  def testImport(self):
    item = Thing()
    self.failIf(item.icon == 5)
    self.failUnless(item.icon == 0)
    player = Monster()
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
  def test7Card(sefl):
    deck = Deck()
    deck.draw(7)
  def testCards(self):
    straightflushes = []
    flushes = []
    straights = []
    focs = [] 
    houses = [] 
    tocs = []
    doubles = [] 
    pairs = []
    highs = []
    deck = Deck()
    for i in range(20000):
      self.failUnless(len(deck.cards) == 52)
      hand = deck.draw(5)
      if hand.type == "STRAIGHT-FLUSH": 
        straightflushes.append(hand) 
      elif hand.type == "FLUSH": flushes.append(hand) 
      elif hand.type == "STRAIGHT": straights.append(hand)
      elif hand.type == "FOUR": focs.append(hand) 
      elif hand.type == "THREE": tocs.append(hand) 
      elif hand.type == "HOUSE": houses.append(hand) 
      elif hand.type == "DOUBLE": doubles.append(hand) 
      elif hand.type == "PAIR": pairs.append(hand)
      else : highs.append(hand) 
    #print "STRAIGHT-FLUSH " + str(len(straightflushes))
    #print "FOUR " + str(len(focs))
    #print "HOUSE " + str(len(houses))
    #print "FLUSH " + str(len(flushes))
    #print "STRAIGHT " + str(len(straights))
    #print "THREE " + str(len(tocs))
    #print "DOUBLE " + str(len(doubles))
    #print "PAIR " + str(len(pairs))
    self.failIf(len(pairs) < len(doubles) < len(tocs) < len(straights) < len(flushes) < len(houses) < len(focs) < len(straightFlushes))
def main():
  unittest.main()

if __name__ == "__main__":
  main()
