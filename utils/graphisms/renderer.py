import enum

import pygame.display

from Game.player import Player


class Renderer:
    class Modes(enum.Enum):
        CENTERED = "centered"
        ABSOLUTE = "absolute"

    class Canva:
        def __init__(self, content: pygame.surface.Surface, display_mode, depth=0, position=(0, 0)):
            self.content = content
            self.display_mode = display_mode
            self.depth = depth
            self.position = position

    def __init__(self, screen: pygame.Surface, tileset):
        self.screen = screen
        self.tileset = tileset

        self.window = self.screen.get_rect()
        self.canvas = []

    def render_tilemap(self, tilemap):
        m, n = tilemap.get_size()
        x, y = tilemap.get_tile_size()
        t_map = tilemap.get_map()
        image = pygame.Surface((m*x, n*y))

        for i in range(m):
            for j in range(n):
                tile = self.tileset.tile_repertoire[t_map[i, j]]
                image.blit(tile, (j * x, i * y))

        self.canvas.append(self.Canva(image, self.Modes.CENTERED, -1))

    def render_room(self, room):
        room_map = room.get_tile_map()
        self.render_tilemap(room_map)

    def render_player(self, player: Player):
        _, _, x, y = player.get_current()
        player = pygame.surface.Surface((50, 50))
        pygame.draw.rect(player, (255, 0, 0), (0, 0, 50, 50))
        self.canvas.append(self.Canva(player, self.Modes.ABSOLUTE, 1, position=(x, y)))

    def update(self):
        for canva in sorted(self.canvas, key=lambda c: c.depth):
            self.screen.blit(canva.content, canva.content.get_rect(center=self.window.center) if canva.display_mode == self.Modes.CENTERED else canva.position)

        pygame.display.update()



