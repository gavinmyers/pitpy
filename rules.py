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

class Combat(object):
  @staticmethod
  def attack(a,d):
    aw = a.weapon
    av = aw.attack(a)
    dw = d.weapon
    dv = dw.defend(d)
    if Chance.win(av,0,dv,0):
      damage = aw.damage(a)
      d.damage(damage)
      if d.health < 0: d.die()
