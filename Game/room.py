import numpy as np
from random import randint
from math import sin, cos, radians

from utils import Tilemap, Tileset
from .constants import *


class Room:
    def __init__(self, x: int, y: int, exits: set | list, room_size: tuple[int, int] = (7, 7)) -> None:
        """
        Génère "manuellement" une pièce avec les paramètres donnés
        :param x: la position de la pièce dans le labyrinthe auquel elle est assignée
        :param y: "
        :param exits: les sorties de la pièce
        :param room_size: la taille de la pièce
        """
        self.x = x
        self.y = y
        self.room_size = room_size
        self.items = []
        self.exits = exits
        self.visited = False
        self.generated = False
        self.visited_by = []
        self.map = None

    def set_map(self, _map: np.ndarray) -> None:
        self.map = _map

    def get_tile_map(self) -> Tilemap | None:
        return self.map

    def get_exits(self) -> set | list:
        return self.exits

    def get_size(self):
        return self.room_size


def generate(x: int, y: int, room_size: tuple[int, int], tileset: Tileset, exits: object = None) -> Room:
    """
    Génère de façon automatique une pièce en utilisant la génération de terrain WFC
    ATTENTION: contient des bugs
    :param x: la position de la pièce dans le labyrinthe
    :param y: "
    :param room_size: la taille de la pièce
    :param tileset: les textures utilisées
    :param exits: les portes par défaut de la pièce
    :return: la pièce générée sous forme de l'objet Room
    """
    if exits is None:
        exits = set()
    for i in range(0, 360, 90):
        if randint(0, 1) == 0:
            exits.add((int(cos(radians(i))), int(sin(radians(i)))))

    room = Room(x, y, exits, room_size)

    tile_map = Tilemap(tileset, room_size)
    tile_map.set_wfc()

    w, h = room_size
    w = w - 1
    h = h - 1
    for ex, ey in exits:
        tile_map.set_at_coords((int((ex * w / 2) + w / 2), int((ey * h / 2) + h / 2)), "door")

    room.set_map(tile_map)

    return room
