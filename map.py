#!/usr/bin/env python
import os
from thing import Thing

class Map(object):
  def __init__(self,w,h):
    self.width = w
    self.height = h
    self.tiles = []
    for y in range(self.height):
      self.tiles.append([])
      for x in range(self.width): 
        self.tiles[y].append([])
        self.tiles[y][x] = Tile() 
  
  def tile(self,x,y):
    return self.tiles[y][x]

class Tile(Thing):
  def __init__(self):
    Thing.__init__(self)
    self.style = "O" 

class AsciiMap(Map):
  def __init__(self,w,h):
    Map.__init__(self,w,h)

  def draw(self):
    os.system('clear')
    for y in range(self.height):
      row = ""
      for x in range (self.width):
        row += self.tile(x,y).style
      print row 

