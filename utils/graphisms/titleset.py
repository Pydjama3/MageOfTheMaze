import pygame


class Tileset:

    def __init__(self, file, size=(7, 7), margin=0, spacing=0, factor=10):
        self.file = file
        self.size = size
        self.margin = margin
        self.spacing = spacing
        self.factor = factor
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.tile_repertoire = {}

    def load_tile(self, name, position, rotation=0):
        if name not in self.tile_repertoire.keys():
            x, y = position
            tile = pygame.Surface(self.size)
            tile.blit(self.image, (0, 0), (x * self.size[0], y * self.size[1], *self.size))
            bigger = pygame.transform.scale_by(tile, self.factor)
            rotated = pygame.transform.rotate(bigger, rotation)
            self.tile_repertoire[name] = rotated
        else:
            raise ValueError("This index has already been assigned")

    def get_texture(self, name):
        return self.tile_repertoire.get(name, None)

    def get_size(self):
        return self.size

    def get_real_size(self):
        return self.size[0]*self.factor, self.size[1]*self.factor

    def get_repertoire(self):
        return list(self.tile_repertoire.keys())

    def __str__(self):
        return f'{self.__class__.__name__} file:{self.file} tile:{self.size}'
