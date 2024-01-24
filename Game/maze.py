from utils import Tileset
from .room import *


class Maze:
    def __init__(self, room_size: tuple[int, int], tileset: Tileset) -> None:
        """
        Créer un labyrinthe custom avec aucune piève
        :param room_size: La taille de la salle en (x, y)
        :param tileset: Les textures utilisées
        """
        self.rooms = {}
        self.rooms_size = room_size
        self.tileset = tileset

    def create_room(self, x: int, y: int, exits: set) -> None:
        """
        Créé une nouvelle pièce aux coordonnées données
        :param x:
        :param y:
        :param exits: Les sorties de la nouvelle pièce
        """
        self.rooms[(x, y)] = generate(x, y, self.rooms_size, self.tileset, exits)
    
    def create_room_safe(self, x: int, y: int) -> None:
        """
        Créé une nouvelle pièce aux coordonnées données en tenant en compte les pièces voisines et les portes existantes
        :param x:
        :param y:
        """
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
        self.rooms[(x, y)] = generate(x, y, self.rooms_size, self.tileset, exits)

    def get_neighbours(self, coords: tuple[int, int]) -> list:
        """
        Obtenir les voisins dirrectement attenant à une pièce aux coordonnées données 
        :param coords: x, y
        :return: La lists des pièces voisines dans l'ordre [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
        """
        x, y = coords

        neighbours = []
        neighbours.append(((x, y + 1), self.rooms.get((x, y + 1), None)))
        neighbours.append(((x + 1, y), self.rooms.get((x + 1, y), None)))
        neighbours.append(((x, y - 1), self.rooms.get((x, y - 1), None)))
        neighbours.append(((x - 1, y), self.rooms.get((x - 1, y), None)))

        return neighbours

    def get_room(self, x: int, y: int) -> Room | None:
        """
        Obtenir la pièce aux coordonnées données
        :param x: 
        :param y: 
        :return: La pièce sous forme de l'objet Room si elle existe sinon None
        """
        return self.rooms.get((x, y), None)
      
    def delete_room(self, x: int, y: int) -> None:
        """
        Supprime une pièce du labyrinthe
        :param x: 
        :param y: 
        """
        del self.rooms[(x, y)]
