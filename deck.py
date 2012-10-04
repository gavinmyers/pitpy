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
    if(total < 5): total = 5
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
    if(len(cards) == 5): 
      self.rank(cards);
    elif(len(cards) > 5):
      hand = {}
      score = 0
      #wow, what a hack... 
      for i in range(31,2**len(cards)):
        pattern = []
        for j,s in enumerate(str(bin(i))):
          if s == "1":
            pattern.append(1)
          elif j > 1:
            pattern.append(0)
        if sum(pattern) == 5:
          possibleHand = []
          for j,s in enumerate(pattern):
            if s == 1:
              possibleHand.append(cards[j])
          if self.rank(possibleHand) > score:
            hand = possibleHand
            score = self.rank(possibleHand)
      self.rank(possibleHand)

  #this entire process needs to be reconsidered             
  def rank(self,cards):
    self.cards = cards 
    self.type = ""
    self.score = 0
    self.high = 0
    self.suits = []
    self.values = []
    self.flush = False
    self.straight = False
    for c in self.cards:
      self.suits.append(c.suit)
      self.values.append(c.value)
    self.values.sort()
    self.high = self.values[-1]
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
      self.score = 0.8 + (foc / 1000.0) + (filter (lambda a: a != foc, self.values)[0]  / 100000.0) 
    elif toc != 0 and pr1 != 0:
      self.type = "HOUSE"
      self.score = 0.7 + (toc / 1000.0) + (pr1 / 100000.0)
    elif toc != 0 :
      self.type = "THREE"
      remvs = (filter (lambda a: a != toc, self.values))
      remvs.sort() 
      self.score = 0.4 + (toc / 1000.0) + (remvs[-1] / 100000.0) 
    elif pr2 != 0:
      self.type = "DOUBLE"
      prs = [pr1,pr2]
      prs.sort()
      self.score = 0.3 + (prs[0] / 1000.0) 
      self.score += (prs[1] / 100000.0)
      remvs = (filter (lambda a: a != pr1 and a != pr2, self.values)) 
      remvs.sort()
      self.score += (remvs[-1] / 10000000.0)
    elif pr1 != 0:
      self.type = "PAIR"
      self.score = 0.2 + (pr1 / 1000.0) 
      remvs = (filter (lambda a: a != pr1, self.values)) 
      remvs.sort()
      self.score += (remvs[-1] / 100000.0)

    if len(set(self.suits)) == 1: 
      self.type = "FLUSH"
      self.flush = True 
      self.score = 0.6 + (self.high / 1000.0)

    grps = map(itemgetter(1),groupby(enumerate(self.values), lambda (i,x):i-x))
    if len(grps) == 1: 
      self.straight = True
    if len(grps) == 2 and 2 in self.values and 5 in self.values and 14 in self.values: 
      self.straight = True

    if self.straight == True and self.flush == True:
      self.type = "STRAIGHT-FLUSH"
      self.score = 0.9 + (self.high / 1000.0)
    elif self.straight == True:
      self.type = "STRAIGHT"
      self.score = 0.5 + (self.high / 1000.0)

    if self.score == 0: self.score = 0.1 + (self.high / 1000.0)
    return self.score
 
  def beats(self, hand):
    return self.score > hand.score
