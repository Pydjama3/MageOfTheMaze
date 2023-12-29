import pygame
from pygame.locals import *

from Game import Room, Player, Maze
from utils import *
from Game.Constants import all_textures_rep, texture_to_coordinates
from utils.graphisms.renderer import Renderer

file = 'assets/textures.png'


class Game:
    W = 1400
    H = 700
    SIZE = W, H

    def __init__(self):
        pygame.init()
        self.size = pygame.display.get_desktop_sizes()
        self.screen = pygame.display.set_mode(self.SIZE)
        pygame.display.set_caption("ELIAS CAN CODE!!!")

        tileset = Tileset('./assets/textures.png', size=(7, 7))
        for texture in all_textures_rep:
            check = texture.split("_")
            if len(check) > 2:
                rotation = int(check[-1])
                first_part = "_".join(check[0:-1])
                tileset.load_tile(texture, texture_to_coordinates.get(first_part), rotation)
            else:
                tileset.load_tile(texture, texture_to_coordinates.get(texture))
        print(tileset)

        self.maze = Maze((7, 7), tileset)
        self.maze.create_room_safe(0, 0)

        self.player = Player()

        self.render = Renderer(self.screen, tileset)
        self.render.render_room(self.maze.get_room(0, 0))
        self.render.update()

        self.running = True

    def run(self):
        last_pos = self.player.get_current()
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

                if event.type == KEYDOWN:
                    if event.key == K_z:
                        r_x, r_y, _, _ = self.player.get_current()
                        self.player.change_room(r_x, r_y+1)
                    elif event.key == K_d:
                        r_x, r_y, _, _ = self.player.get_current()
                        self.player.change_room(r_x+1, r_y)
                    elif event.key == K_s:
                        r_x, r_y, _, _ = self.player.get_current()
                        self.player.change_room(r_x, r_y-1)
                    elif event.key == K_q:
                        r_x, r_y, _, _ = self.player.get_current()
                        self.player.change_room(r_x-1, r_y)

            if self.player.get_current() != last_pos:
                print("-" * 30)
                last_pos = self.player.get_current()

                r_x, r_y, _, _ = self.player.get_current()
                if self.maze.get_room(r_x, r_y) is None:
                    self.maze.create_room_safe(r_x, r_y)

                self.render.render_room(self.maze.get_room(r_x, r_y))
                self.render.update()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
