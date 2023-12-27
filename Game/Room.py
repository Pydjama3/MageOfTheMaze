from wfc import Wave, State, Rule
import colorama
from .Constants import *


class Room:
  def __init__(self, x, y, room_size):
    self.x = x
    self.y = y
    self.room_size = room_size
    self.items = []
    self.exits = []
    self.visited = False
    self.generated = False
    self.visited_by = []
    self.map = []

  @staticmethod
  def generate(x, y, room_size):
    room = Room(x, y, room_size)

    landscape_wave = Wave(room_size, [grass, stone, path, water])
    room.set_map(landscape_wave.collapse())

    return room

  def set_map(self, map):
    self.map = map

  def get_map(self):
    return self.map
