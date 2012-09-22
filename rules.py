#!/usr/bin/env python
import random

class Chance:
  @staticmethod
  def over(source, challenge):
    return random.randint(0,source) >= challenge

  @staticmethod
  def match(source, challenge):
    return random.randint(0,source) == challenge

  @staticmethod
  def win(s, sc, d, dc):
    sr = random.randint(0,s) - sc
    dr = random.randint(0,d) - dc 
    return sr >= dr

  @staticmethod
  def value(s):
    return random.randint(0,s)

class Interact:
  @staticmethod
  def attack(attacker, defender):
    attackStr = attacker.attributes["KTE"].value 
    defendStr = defender.attributes["DEX"].value
    if Chance.over(attackStr,defendStr):
      Interact.damage(defender,attacker.attribute["STR"])

  @staticmethod
  def damage(who, ammount):
    who.health -= ammount
