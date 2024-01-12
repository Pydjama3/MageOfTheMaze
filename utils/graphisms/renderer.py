import enum

import pygame.display
from pygame.locals import *
from pygame.sprite import Group

from Game.player import Player, PlayerState
from utils.sprites import PlayerSprite
from utils.sprites.zombiesprite import ZombieSprite


class Renderer:
    class Modes(enum.Enum):
        CENTERED = "centered"
        ABSOLUTE = "absolute"

    class Support(enum.Enum):
        SCREEN = "screen"
        MAIN = "main"
        LEFT = "left_pannel"
        RIGHT = "right_pannel"

    class Canva:
        def __init__(self, content: pygame.surface.Surface, display_mode, support=None, depth=0, position=(0, 0)):
            self.content = content
            self.display_mode = display_mode
            self.depth = depth
            self.position = position
            self.destination_support = support

    def __init__(self, screen: pygame.Surface, tileset):
        self.screen = screen
        self.tileset = tileset

        x, y = self.screen.get_size()
        self.main = pygame.Surface((y, y))

        self.window = self.screen.get_rect()
        self.player_size = self.main.get_size()[0] / 49 * 5, self.main.get_size()[0] / 49 * 5
        self.canvas = []
        self.all_sprites = Group()
        self.all_zombies = Group()

        self.player_sprite = PlayerSprite(Rect((0, 0), self.player_size), self.main.get_size()[1]/400)

        self.all_sprites.add(self.player_sprite)

    def render_tilemap(self, tilemap):
        m, n = tilemap.get_size()
        x, y = tilemap.get_tile_size()
        t_map = tilemap.get_map()
        image = pygame.Surface((m * x, n * y))

        for i in range(m):
            for j in range(n):
                tile = self.tileset.tile_repertoire[t_map[j, i]]
                image.blit(tile, (i * x, j * y))

        self.canvas.append(self.Canva(image, self.Modes.ABSOLUTE, self.Support.MAIN, -1, (0, 0)))

    def render_room(self, room):
        room_map = room.get_tile_map()
        self.render_tilemap(room_map)

    def render_player(self, player: Player):
        _, _, x, y = player.get_current()
        self.player_sprite.set_state(player.state)
        self.player_sprite.set_animator_settings(flip=((player.orientation-1) % 3, 0))
        if not self.player_sprite.update(x - self.player_size[0] // 2, y - self.player_size[1]):
            player.set_state(PlayerState.IDLE)
            self.player_sprite.set_state(player.state)
            self.player_sprite.update(x - self.player_size[0] // 2, y - self.player_size[1])
            

        player_surface = pygame.surface.Surface(self.player_size)
        pygame.draw.rect(player_surface, (255, 0, 0), (0, 0) + self.player_size)
        self.canvas.append(self.Canva(player_surface, self.Modes.ABSOLUTE, self.Support.MAIN, 1,
                                      position=(x, y)))

    def render_zombie(self, zombie):
        pass

    def update(self):
        self.screen.fill(Color(0, 0, 0))
        self.main.fill(Color(0, 0, 0))

        for canva in sorted(self.canvas, key=lambda c: c.depth):
            match canva.destination_support:
                case self.Support.SCREEN:
                    self.screen.blit(canva.content, canva.content.get_rect(
                        center=self.window.center) if canva.display_mode == self.Modes.CENTERED else canva.position)
                case self.Support.MAIN:
                    self.main.blit(canva.content, canva.content.get_rect(
                        center=self.main.get_rect().center) if canva.display_mode == self.Modes.CENTERED else canva.position)

        self.all_sprites.draw(self.main)

        self.screen.blit(self.main, self.main.get_rect(center=self.window.center))

        pygame.display.update()
        self.canvas = []
