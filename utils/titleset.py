import pygame


class Tileset:

  def __init__(self, files, size=(7, 7), margin=1, spacing=1):
    self.files = files
    self.size = size
    self.margin = margin
    self.spacing = spacing
    self.image = pygame.image.load(file)
    self.rect = self.image.get_rect()
    self.tiles = []
    self.load()

  def load(self):
    self.files = []
    for file in self.files:
      img = pygame.image.load(file)

      tile = pygame.Surface(self.size)
      tile.blit(img, (0, 0), (0, 0, *self.size))
      self.tiles.append(tile)

  def __str__(self):
    return f'{self.__class__.__name__} tile:{self.size}'
