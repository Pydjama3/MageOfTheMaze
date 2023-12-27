import pygame
import numpy as np


class Tilemap:
  W = 640
  H = 240
  SIZE = W, H
  def __init__(self, tileset, size=(10, 20), rect=None):
    pygame.init()
    self.screen = pygame.display.set_mode(self.SIZE)
    pygame.display.set_caption("Pygame Tiled Demo")
    
    self.size = size
    self.tileset = tileset
    self.map = np.zeros(size, dtype=int)

    h, w = self.size
    self.image = pygame.Surface((7 * w, 7 * h))
    if rect:
      self.rect = pygame.Rect(rect)
    else:
      self.rect = self.image.get_rect()

  def render(self):
    m, n = self.map.shape
    for i in range(m):
      for j in range(n):
        tile = self.tileset.tiles[self.map[i, j]]
        self.image.blit(tile, (j * 7, i * 7))
    self.image.blit(self.image, self.rect)
    pygame.display.update()

  def set_zero(self):
    self.map = np.zeros(self.size, dtype=int)
    print(self.map)
    print(self.map.shape)
    self.render()

  def set_random(self):
    n = len(self.tileset.tiles)
    self.map = np.random.randint(n, size=self.size)
    print(self.map)
    self.render()

  def __str__(self):
    return f'{self.__class__.__name__} {self.size}'
