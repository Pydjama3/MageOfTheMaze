import pygame
from pygame.locals import *


class Tileset:

    def __init__(self, file: str, size: tuple[int, int] = (7, 7), margin: int = 0, spacing: int = 0, factor: float = 10) -> None:
        """
        Créer un nouveau set de textures avec <file> pour source
        :param file: La source
        :param size: La taille des textures
        :param margin: L'écart entre le bord et les textures
        :param spacing: L'espace entre les textures
        :param factor: La facteur d'agrandissement des textures
        """
        self.file = file
        self.size = size
        self.margin = margin
        self.spacing = spacing
        self.factor = factor
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.tile_repertoire = {}

    def load_tile(self, name: object, position: tuple, rotation: float = 0) -> None:
        """
        Charge une texture individuellement et lui assigne <name> dans le dictionnaire
        :param name: L'id de la texture
        :param position: La position de la texture sur l'image source
        :param rotation: La rotation de la texture après chargement
        :raises ValueError:
        """
        if name not in self.tile_repertoire.keys():
            x, y = position
            tile = pygame.Surface(self.size, SRCALPHA)
            tile.blit(self.image, (0, 0), (x * self.size[0], y * self.size[1], *self.size))
            bigger = pygame.transform.scale_by(tile, self.factor)
            rotated = pygame.transform.rotate(bigger, rotation)
            self.tile_repertoire[name] = rotated
        else:
            raise ValueError("This index has already been assigned")

    def get_texture(self, name: object) -> pygame.Surface | None:
        """
        Retourne la texture individuelle assignée au nom
        :param name: L'id de la texture
        :return: La texture ou None si elle n'existe pas
        """
        return self.tile_repertoire.get(name, None)

    def get_size(self) -> tuple[int, int]:
        """
        Obtenir la taille des textures
        :return: La taille des textures
        """
        return self.size

    def get_real_size(self) -> tuple[float, float]:
        """
        Obtenir la taille réelle des txtures (avec leur facteur multiplicateur)
        :return: La taille réelle
        """
        return self.size[0]*self.factor, self.size[1]*self.factor

    def get_repertoire(self) -> list[object]:
        """
        Obtenir la liste complète des ids des textures
        :return: La liste
        """
        return list(self.tile_repertoire.keys())

    def __str__(self):
        return f'{self.__class__.__name__} file:{self.file} tile:{self.size}'
