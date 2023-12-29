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
        self.maze.create_room(0, 0, set([(0, 1), (1, 0), (0, -1), (-1, 0)]))

        self.player = Player()
        self.player.set_speed(0.5)

        self.render = Renderer(self.screen, tileset)
        self.render.render_room(self.maze.get_room(0, 0))
        self.render.render_player(self.player)
        self.render.update()

        self.running = True

    def run(self):
        last_pos = self.player.get_current()
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            keys=pygame.key.get_pressed()
            if keys[K_s]:
                self.player.move((0, 1))
            elif keys[K_d]:
                self.player.move((1, 0))
            elif keys[K_z]:
                self.player.move((0, -1))
            elif keys[K_q]:
                self.player.move((-1, 0))

            

            if self.player.get_current() != last_pos:
                #print("-" * 30)
                last_pos = self.player.get_current()

                r_x, r_y, x, y = self.player.get_current()
                if self.maze.get_room(r_x, r_y) is None:
                    self.maze.create_room_safe(r_x, r_y)

                room = self.maze.get_room(r_x, r_y)
                w, h = room.get_size()
                t_x = x // w
                t_y = y // h
                
                neigh = [None] * 4
                neigh[0] = room.get_map().get_at_coord((t_x, t_y+1))
                neigh[1] = room.get_map().get_at_coord((t_x + 1, t_y))
                neigh[2] = room.get_map().get_at_coord((t_x, t_y-1))
                neigh[3] = room.get_map().get_at_coord((t_x - 1, t_y))
                
                if neigh[0].starts_with("water"):
                    self.player.block_move_y(1)
                if neigh[1].starts_with("water"):
                    self.player.block_move_x(1)
                if neigh[2].starts_with("water"):
                    self.player.block_move_y(-1)
                if neigh[3].starts_with("water"):
                    self.player.block_move_x(-1)
                
                self.render.render_room(self.maze.get_room(r_x, r_y))
                self.render.render_player(self.player)
                self.render.update()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
