import colorama
from wfc import Wave, State, Rule
import pygame
from pygame.locals import *
from Game import *
from utils import *

file = 'assets/textures.png'

class Game:
  W = 21
  H = 21
  SIZE = W, H

  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode(Game.SIZE)
    pygame.display.set_caption("ELIAS CAN'T CODE!!!")
    self.running = True

  def run(self):
    while self.running:
      for event in pygame.event.get():
        if event.type == QUIT:
          self.running = False

        elif event.type == KEYDOWN:
          if event.key == K_l:
            self.load_image(file)

    pygame.quit()

  def load_image(self, file):
    self.file = file
    self.image = pygame.image.load(file)
    self.rect = self.image.get_rect()

    self.screen = pygame.display.set_mode(self.rect.size)
    pygame.display.set_caption(f'size:{self.rect.size}')
    self.screen.blit(self.image, self.rect)
    pygame.display.update()


if __name__ == "__main__":
  tileset = Tileset('./assets/textures.png', size=(7, 7))
  print(tileset)
  tilemap = Tilemap(tileset)
  tilemap.set_random()
  
