#!/usr/bin/env python

import random
from itertools import *
from operator import *

suits = ["HEART","SPADE","CLUB","DIAMOND"]

class Deck:
  def __init__(self,decks=1):
    self.index = 0
    self.cards = []
    for v in suits:
      for i in range(2,15):
        card = Card(v,i)
        self.cards.append(card)
    random.shuffle(self.cards) 

  def draw(self,total):
    if(total > 5): total = 5
    if(self.index + total > 52): 
      self.index = 0
      random.shuffle(self.cards)
    hand = self.cards[self.index:self.index+total]
    self.index += total
    return Hand(hand)

class Card:
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value

class Hand:
  def __init__(self, cards):
    self.cards = cards 
    self.type = ""
    self.score = 0
    self.suits = []
    self.values = []
    self.flush = False
    self.straight = False
    for c in self.cards:
      self.suits.append(c.suit)
      self.values.append(c.value)
    self.values.sort()

    foc = 0
    toc = 0
    pr1 = 0
    pr2 = 0
    for c in self.values:
      if self.values.count(c) == 4: foc = c
      if self.values.count(c) == 3: toc = c
      if self.values.count(c) == 2 and pr1 == 0: pr1 = c
      if self.values.count(c) == 2 and pr1 != 0 and pr1 != c: pr2 = c
    if foc != 0:
      self.type="FOUR"
    elif toc != 0 and pr1 != 0:
      self.type = "HOUSE"
    elif toc != 0 :
      self.type = "THREE"
    elif pr2 != 0:
      self.type = "DOUBLE"
    elif pr1 != 0:
      self.type = "PAIR"

    if len(set(self.suits)) == 1: 
      self.flush = True 

    grps = map(itemgetter(1),groupby(enumerate(self.values), lambda (i,x):i-x))
    if len(grps) == 1: 
      self.straight = True
    if len(grps) == 2 and 2 in self.values and 5 in self.values and 14 in self.values: 
      self.straight = True

    if self.straight == True and self.flush == True:
      self.type = "STRAIGHT-FLUSH"
    elif self.flush == True:
      self.type = "FLUSH"
    elif self.straight == True:
      self.type = "STRAIGHT"
