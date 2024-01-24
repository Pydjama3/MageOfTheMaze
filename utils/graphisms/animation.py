import pygame.image

from utils.graphisms import Tileset


class Animation(Tileset):
    def __init__(self, file: str, n_frames: int, factor: float = 10) -> None:
        """
        Créé une Animation qu'un objet Animator pourra exécuter
        :param file: Chemin du fichier image source duquel les images de l'animatique seront extraites
        :param n_frames: Le nombre d'images qui composent l'animations
        :param factor: Par quel facteur la taille des images originales doit être multipliée
        """
        self.n_frames = n_frames

        super().__init__(file, factor=factor)
        self.size = self.rect.size[0]/n_frames, self.rect.size[1]

    def load_all(self) -> None:
        """
        Charge toutes les image automatiquement de l'animation à partir des paramètres donnés à la crétion de l'objet
        """
        for i in range(self.n_frames):
            self.load_frame(i, (i, 0))

    def load_frame(self, index: int, position: tuple[int, int], rotation: float = 0) -> None:
        """
        Charge une image de l'animation seule et lui assigne la clée <i>
        :param index: Clée de l'image
        :param position: Position sur l'image source
        :param rotation: Comment orienter l'image source
        """
        super().load_tile(index, position, rotation)

    def get_animation(self) -> list[pygame.surface.Surface]:
        """
        Retourne toute l'animation dans une liste ordonnée des clées
        :return: L'animation sous forme de liste de Surface
        """
        return [self.tile_repertoire.get(frame) for frame in sorted(self.tile_repertoire.keys())]

    def get_frame(self, index: int) -> pygame.surface.Surface:
        """
        Retourne l'image <i> de l'animation
        :param index: La clée de l'image
        :return: Une surface pygame
        """
        return super().get_texture(index)

    def get_frame_num(self) -> int:
        """
        Avoir le nombre de frame
        :return: ce nombre
        """
        return self.n_frames
