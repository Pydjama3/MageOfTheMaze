import pygame.display
from pygame.locals import *
from .tilemap import Tilemap


class Renderer:
    def __init__(self, screen, tileset):
        self.screen = screen
        self.tileset = tileset

    def render_tilemap(self, tilemap: Tilemap):
        m, n = tilemap.get_size()
        x, y = tilemap.get_tile_size()
        t_map = tilemap.get_map()
        image = pygame.Surface((m*x, n*y))

        for i in range(m):
            for j in range(n):
                tile = self.tileset.tile_repertoire[t_map[i, j]]
                image.blit(tile, (j * x, i * y))

        self.screen.blit(image, (0, 0))

    def render_room(self, room):
        room_map = room.get_map()
        self.render_tilemap(room_map)

    def update(self):
        pygame.display.update()



