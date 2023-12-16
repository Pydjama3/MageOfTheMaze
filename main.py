import sys
import colorama
from wfc import Wave, State, Rule
from utils import Tileset, Tilemap
import pygame
from pygame.locals import *

# Initializing Pygame modules
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400, 300))

# Initializing RGB Color
color = (126, 182, 178)

# Changing surface color
surface.fill(color)
pygame.display.flip()


grass = State(
    "grass",
    Rule(
        lambda x, y : {
            (x+1, y+1): ["dirt", "stone", "water", "grass", "path"],
            (x-1, y+1): ["dirt", "stone", "water", "grass", "path"],
            (x-1, y-1): ["dirt", "stone", "water", "grass", "path"],
            (x+1, y-1): ["dirt", "stone", "water", "grass", "path"],
            (x, y-1): ["dirt", "stone", "water", "grass", "path"],
            (x, y+1): ["dirt", "stone", "water", "grass", "path"],
            (x+1, y): ["dirt", "stone", "water", "grass", "path"],
            (x-1, y): ["dirt", "stone", "water", "grass", "path"]
        }
    )
)

dirt = State(
    "dirt",
    Rule(
        lambda x, y: {
          (x+1, y+1): ["dirt", "stone", "water", "grass", "path"],
          (x-1, y+1): ["dirt", "stone", "water", "grass", "path"],
          (x-1, y-1): ["dirt", "stone", "water", "grass", "path"],
          (x+1, y-1): ["dirt", "stone", "water", "grass", "path"],
          (x, y-1): ["dirt", "stone", "water", "grass", "path"],
          (x, y+1): ["dirt", "stone", "water", "grass", "path"],
          (x+1, y): ["dirt", "stone", "water", "grass", "path"],
          (x-1, y): ["dirt", "stone", "water", "grass", "path"]
        }
    )
)

stone = State(
    "stone",
    Rule(
        lambda x, y : {
          (x+1, y+1): ["dirt", "stone", "water", "grass"],
          (x-1, y+1): ["dirt", "stone", "water", "grass"],
          (x-1, y-1): ["dirt", "stone", "water", "grass"],
          (x+1, y-1): ["dirt", "stone", "water", "grass"],
          (x, y-1): ["dirt", "stone", "water", "grass",],
          (x, y+1): ["dirt", "stone", "water", "grass",],
          (x+1, y): ["dirt", "stone", "water", "grass",],
          (x-1, y): ["dirt", "stone", "water", "grass",]
        }
    )
)

water = State(
    "water",
    Rule(
        lambda x, y : {
          (x+1, y+1): ["dirt", "stone", "water", "grass"],
          (x-1, y+1): ["dirt", "stone", "water", "grass"],
          (x-1, y-1): ["dirt", "stone", "water", "grass"],
          (x+1, y-1): ["dirt", "stone", "water", "grass"],
          (x, y-1): ["dirt", "stone", "water", "grass"],
          (x, y+1): ["dirt", "stone", "water", "grass"],
          (x+1, y): ["dirt", "stone", "water", "grass"],
          (x-1, y): ["dirt", "stone", "water", "grass"]
        }
    )
)

path = State(
  "path",
  Rule(
    lambda x, y : {
      (x+1, y+1): ["dirt", "stone", "water", "grass"],
      (x-1, y+1): ["dirt", "stone", "water", "grass"],
      (x-1, y-1): ["dirt", "stone", "water", "grass"],
      (x+1, y-1): ["dirt", "stone", "water", "grass"],
      (x, y-1): [ "water", "grass", "path"],
      (x, y+1): [ "water", "grass", "path"],
      (x+1, y): [ "water", "grass", "path"],
      (x-1, y): ["water", "grass", "path"]
    }
  )
)

cmap = {
    "water": colorama.Fore.BLUE,
    "grass": colorama.Fore.GREEN,
    "dirt": colorama.Fore.WHITE,
    "stone": colorama.Fore.LIGHTBLACK_EX,
    "lava": colorama.Fore.RED,
    "path": colorama.Fore.YELLOW
}

file = 'assets/ground.png'
"""
class Game:
    W = 640
    H = 240
    SIZE = W, H

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(Game.SIZE)
        pygame.display.set_caption("Pygame Tiled Demo")
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
  landscape_wave = Wave(
      (10, 10),
      [grass, stone, path, water]
  )
  landscape = landscape_wave.collapse()

  for row in landscape:
      for item in row:
          print(cmap[item.state.name]+ cmap[item.state.name] + "█" + colorama.Fore.RESET, end="")
      print()


  game = Game()
  game.run()"""