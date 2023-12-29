import numpy as np
from random import randint
from math import sin, cos, radians

from utils import Tilemap
from .Constants import *


class Room:
    def __init__(self, x, y, exits, room_size=(7, 7)):
        self.x = x
        self.y = y
        self.room_size = room_size
        self.items = []
        self.exits = exits
        self.visited = False
        self.generated = False
        self.visited_by = []
        self.map = np.array([])

    @staticmethod
    def generate(x, y, room_size, tileset, exits=None):
        if exits is None:
            exits = set()
        for i in range(0, 360, 90):
            if randint(0, 1) == 0:
                exits.add((int(cos(radians(i))), int(sin(radians(i)))))

        room = Room(x, y, exits, room_size)

        tile_map = Tilemap(tileset, room_size, tileset.get_real_size())
        tile_map.set_wfc()

        w, h = room_size
        w = w - 1
        h = h - 1
        for ex, ey in exits:
            tile_map.set_at_ccoords((int((ex*w/2) + w/2), int((ey*h/2) + h/2)), "door")

        room.set_map(tile_map)

        return room

    def set_map(self, _map):
        self.map = _map

    def get_map(self) -> np.array:
        return self.map

    def get_exits(self):
        return self.exits
