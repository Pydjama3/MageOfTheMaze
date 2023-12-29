from .Room import *


class Maze:
    def __init__(self, room_size, tileset) -> None:
        self.rooms = {}
        self.rooms_size = room_size
        self.tileset = tileset

    def create_room_safe(self, x, y):
        neighbours = self.get_neighbours((x, y))
        print(x, y)
        print(neighbours)

        exits = set()
        for coords, neighbour in neighbours:
            if neighbour is not None:
                nx, ny = coords
                if (-nx, -ny) in neighbour.get_exits():
                    exits.add(coords)

        print(exits)
        self.rooms[(x, y)] = Room.generate(x, y, self.rooms_size, self.tileset, exits)

    def get_neighbours(self, coords):
        x, y = coords

        neighbours = []
        neighbours.append(((x, y + 1), self.rooms.get((x, y + 1), None)))
        neighbours.append(((x + 1, y), self.rooms.get((x + 1, y), None)))
        neighbours.append(((x, y - 1), self.rooms.get((x, y - 1), None)))
        neighbours.append(((x - 1, y), self.rooms.get((x - 1, y), None)))

        return neighbours

    def get_room(self, x, y):
        return self.rooms.get((x, y), None)
    def delete_room(self, x, y):
        del self.rooms[(x, y)]

    def get_rooms(self):
        return self.rooms
