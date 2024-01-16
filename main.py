import pygame
from pygame.locals import *

from Game import (Player, Maze, DIST_TO_NEXT_TILE, ALL_TEXTURES_REP, TEXTURE_TO_COORDINATES, BLOCKED_TILES, ROOM_SIZE,
                  TILE_SIZE, PLAYER_SPEED_FACTOR, TILES_TEXTURES, PlayerState, MAIN_THEME)
from utils import *
from utils.graphisms.renderer import Renderer


class Game:
    def __init__(self):
        pygame.init()
        self.size = pygame.display.get_desktop_sizes()[-1]
        self.screen = pygame.display.set_mode(self.size)  # (0, 0), FULLSCREEN)
        pygame.display.set_caption("Mage of the Maze - Chaotic Studio - Louis and Florence")

        pygame.mixer.init()
        pygame.mixer.music.load(MAIN_THEME)
        pygame.mixer.music.play(-1)

        tileset = Tileset(TILES_TEXTURES, size=TILE_SIZE, factor=self.size[1] / (ROOM_SIZE[0] * TILE_SIZE[0]))
        for texture in ALL_TEXTURES_REP:
            check = texture.split("_")
            if len(check) > 2:
                rotation = int(check[-1])
                first_part = "_".join(check[0:-1])
                tileset.load_tile(texture, TEXTURE_TO_COORDINATES.get(first_part), rotation)
            else:
                tileset.load_tile(texture, TEXTURE_TO_COORDINATES.get(texture))
        print(tileset)

        self.maze = Maze(ROOM_SIZE, tileset)
        self.maze.create_room(0, 0, {(0, 1), (1, 0), (0, -1), (-1, 0)})
        room = self.maze.get_room(0, 0)

        self.player = None
        r_map = room.get_tile_map().get_map()
        
        for i in range(len(r_map)):
            for j in range(len(r_map[i])):
                if r_map[i][j] == "door":
                    self.player = Player(j*(self.size[1]/ROOM_SIZE[0]), i*(self.size[1]/ROOM_SIZE[1]))
                    break
        
        # self.player = Player(7, 229)
        self.player.set_speed(self.size[1]*PLAYER_SPEED_FACTOR)

        self.renderer = Renderer(self.screen, tileset)
        self.renderer.render_room(self.maze.get_room(0, 0))
        self.renderer.render_player(self.player)
        self.renderer.update()

        self.zombies = []
        

        self.running = True

    def run(self):
        while self.running:
            has_moved = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                if event.type == MOUSEBUTTONDOWN:
                    self.player.set_state(PlayerState.FIGHTING)

            if self.player.get_state() != PlayerState.FIGHTING:
                self.player.reset_movement()
                keys = pygame.key.get_pressed()
                if keys[K_s]:
                    self.player.move((0, 1))
                    has_moved = True
                if keys[K_d]:
                    self.player.move((1, 0))
                    has_moved = True
                if keys[K_z]:
                    self.player.move((0, -1))
                    has_moved = True
                if keys[K_q]:
                    self.player.move((-1, 0))
                    has_moved = True
                elif keys[K_ESCAPE]:
                    self.running = False

            r_x, r_y, x, y = self.player.get_current()
            if has_moved:
                if self.maze.get_room(r_x, r_y) is None:
                    self.maze.create_room_safe(r_x, r_y)

                room = self.maze.get_room(r_x, r_y)
                w, h = room.get_tile_map().get_real_size()
                w_tiles, h_tiles = room.get_size()

                t_x = (x / w) * w_tiles
                t_y = (y / h) * h_tiles
                print(t_x, t_y)
                print(t_y-DIST_TO_NEXT_TILE < 0, t_x-DIST_TO_NEXT_TILE < 0)
                print("-"*30)

                neigh = [""] * 4
                neigh[0] = room.get_tile_map().get_at_coord((int(t_x), int(t_y - DIST_TO_NEXT_TILE)), "").split("_")[0]
                neigh[1] = room.get_tile_map().get_at_coord((int(t_x + DIST_TO_NEXT_TILE), int(t_y)), "").split("_")[0]
                neigh[2] = room.get_tile_map().get_at_coord((int(t_x), int(t_y + DIST_TO_NEXT_TILE)), "").split("_")[0]
                neigh[3] = room.get_tile_map().get_at_coord((int(t_x - DIST_TO_NEXT_TILE), int(t_y)), "").split("_")[0]

                if neigh[0] in BLOCKED_TILES or t_y-DIST_TO_NEXT_TILE < 0:
                    self.player.block_move_y(-1)
                if neigh[1] in BLOCKED_TILES:
                    self.player.block_move_x(1)
                if neigh[2] in BLOCKED_TILES:
                    self.player.block_move_y(1)
                if neigh[3] in BLOCKED_TILES or t_x-DIST_TO_NEXT_TILE < 0:
                    self.player.block_move_x(-1)

                self.player.apply_movement()

            self.renderer.render_room(self.maze.get_room(r_x, r_y))
            self.renderer.render_player(self.player)

            self.renderer.update()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
