import pygame
import numpy as np
from Game.Constants import *

class Tilemap:
    def __init__(self, tileset, size=(10, 20), tile_size=(7*10, 7*10)):

        self.size = size
        self.tile_size = tile_size
        self.tileset = tileset
        self.map = np.zeros(size, dtype=int)

    def set_zero(self):
        self.map = np.zeros(self.size, dtype=int)

    def set_random(self, repertoire):
        n = len(self.tileset.tile_repertoire)
        self.map = np.random.choice(repertoire, size=self.size)

    def set_index(self, index):
        self.map = np.full(self.map.size, index, dtype=str)

    def set_wfc(self, ):
        landscape_wave = Wave(self.size, [
            grass,
            water_straight_0,
            water_straight_90,
            water_elbow_0,
            water_elbow_90,
            water_elbow_180,
            water_elbow_270,
            path_straight_0,
            path_straight_90,
            path_elbow_0,
            path_elbow_90,
            path_elbow_180,
            path_elbow_270,
            stone,
            lava,
            dirt
        ])

        self.map = np.array([[item.state.name for item in row] for row in landscape_wave.collapse()])

    def set_at_ccoords(self, coords, name):
        self.map[coords] = name

    def get_at_coord(self, coords):
        x, y = coords
        return self.map[x, y]

    def get_map(self):
        return self.map

    def get_tileset(self):
        return self.tileset

    def get_size(self):
        return self.size

    def get_tile_size(self):
        return self.tile_size

    def __str__(self):
        return f'{self.__class__.__name__} {self.size}'
