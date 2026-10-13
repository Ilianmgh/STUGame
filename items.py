import numpy as np
import time
import pygame

item_list = []
character_list = []
enemies_list = []

class Character :
  def __init__ (self, x, y, v_x, v_y, s_x, s_y) :
    self.coor = np.array([x, y])
    self.spawn_coor = (x, y)
    self.vel = np.array([v_x, v_y])
    self.size = np.array([s_x, s_y])

    self.vivant = True
    
    self.sprite = pygame.Rect(
      self.coor[0],
      self.coor[1],
      self.size[0],
      self.size[1]
    )

    character_list.append(self)
  
  def death (self) :
    self.vivant = False
    self.vel = np.array([0, 0])
    self.temps_mort = time.time()
  
  def respawn (self) :
    self.vivant = True

    for i in range(2) :
      self.coor[i] = self.spawn_coor[i]

  def movement (self) :
    for i in range(2) :
      self.coor[i] += self.vel[i]
    self.sprite.x = self.coor[0]
    self.sprite.y = self.coor[1]


class Player (Character) :
  def __init__ (self) :
    super().__init__(40, 40, 0, 0, 40, 70)
    self.au_sol = False
    self.acceleration = 10
    self.shoot = False
    self.slash = False
    self.color = "BLEU"
  
  def move (self, dir) :
    if self.vel[0] < 5 and self.vel[0] > -5 :
      self.vel[0] += self.acceleration * dir * 0.1
    if dir == 0 :
      self.vel[0] = 0
    self.movement()
  
  def jump (self) :
    self.vel[1] -= self.acceleration * 1.5
    self.au_sol = False
  
  def mort (self) :
    self.death()
    self.coor[1] = 1000

class Monster (Character) :
  def __init__ (self) :
    super().__init__(800, 490, -5, 0, 60, 60)
    self.color = "ROUGE"

    enemies_list.append(self)


class Platform :
  def __init__ (self, x, y, s_x, s_y) :
    self.coor = np.array([x, y])

    self.plat = pygame.Rect(
      self.coor[0],
      self.coor[1],
      s_x,
      s_y
    )

    item_list.append(self)

class Sol (Platform) :
  def __init__ (self) :
    super().__init__(0, 550, 800, 50)
    self.color = "VERT"

class Platforme (Platform) :
  def __init__ (self, x, y) :
    super().__init__(x, y, 200, 20)
    self.color = "MARRON"

class Weapons :
  def __init__ (self, s_x, s_y, player : Player) :
    self.size = np.array([s_x, s_y])
    self.diff = s_x
    self.player = player
    self.coor = np.array([
      player.coor[0] + self.diff,
      player.coor[1] + (player.size[1] - self.size[1]) / 2
    ])

    self.weapon = pygame.Rect(self.coor[0],
      self.coor[1],
      self.size[0],
      self.size[1]
    )

class Knife (Weapons) :
  def __init__ (self, player : Player) :
    super().__init__(40, 20, player)
    self.color = "VIOLET"

  def slash (self) :
    pass