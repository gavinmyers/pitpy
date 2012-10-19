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
  def testBattle(self):
    bowman = Monster()
    bowman.name = "Bow Man"
    bowman.weapon = ProjectileWeapon()
    bowman.attributes = {}
    bowman.attributes[Strength] = Strength(0,0)
    bowman.attributes[Bow] = Bow(100,0)  
    bowman.attributes[Dexterity] = Dexterity(250,0)
    bowman.health = 16

    swordsman = Monster()
    swordsman.name = "Swords Guy"
    swordsman.weapon = BladeWeapon()
    swordsman.attributes = {}
    swordsman.attributes[Strength] = Strength(0,0)
    swordsman.attributes[Sword] = Sword(100,0)  
    swordsman.attributes[Dexterity] = Dexterity(250,0)
    swordsman.health = 16

    miyagi = Monster()
    miyagi.name = "Mr. Miyagi"
    miyagi.weapon = MartialArts()
    miyagi.attributes = {} 
    miyagi.attributes[Strength] = Strength(250,0)
    miyagi.attributes[Dexterity] = Dexterity(250,0)
    miyagi.attributes[Karate] = Karate(250,0)
    miyagi.health = 16 

    daniel = Monster()
    daniel.name = "Daniel"
    daniel.weapon = MartialArts()
    daniel.attributes = {} 
    daniel.attributes[Strength] = Strength(100,0)
    daniel.attributes[Dexterity] = Dexterity(100,0)
    daniel.attributes[Karate] = Karate(100,0)
    daniel.health = 16
    deadMiyagis = 0
    deadDaniels = 0
    deadSwordsmen = 0
    deadBowmen = 0
    for i in range(2500):
      swordsman.attack(bowman)
      if bowman.health < 1: 
        deadBowmen += 1 
        bowman.health = 16
        swordsman.health = 16
      bowman.attack(swordsman)
      if swordsman.health < 1:
        deadSwordsmen += 1
        bowman.health = 16
        swordsman.health = 16

      daniel.attack(miyagi)
      if miyagi.health < 1: 
        deadMiyagis += 1 
        miyagi.health = 16
        daniel.health = 16
      miyagi.attack(daniel)
      if daniel.health < 1:
        deadDaniels += 1
        miyagi.health = 16
        daniel.health = 16
    #print str(deadMiyagis) + " vs " + str(deadDaniels)
    #print str(deadBowmen) + " vs " + str(deadSwordsmen)
    self.failIf(deadMiyagis > deadDaniels)
    self.failIf(deadSwordsmen > deadBowmen)
    self.failIf(deadSwordsmen > 100)
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
