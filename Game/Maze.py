from .Room import *

class Maze:
  def __init__(self, room_size) -> None:
    self.rooms = {}
    self.rooms_size = room_size

  def create_room(self, x, y):
    self.rooms[(x, y)] = Room.generate(x, y, self.rooms_size)

  def delete_room(self, x, y):
    del self.rooms[(x, y)]

  def get_rooms(self):
    return self.rooms
