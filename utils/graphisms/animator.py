import time

import pygame

from utils import Animation


class Animator:
    def __init__(self, delay: float) -> None:
        self.n_frames = None
        self.loop = None
        self.animation = None
        self.delay = delay
        self.current_frame = 0
        self.last_update = 0
        self.running = False
        self.flip = 0, 0
        self.rotation = 0

    def update(self) -> pygame.surface.Surface | None:
        """
        Met à jour l'image actuelle de l'animation et retourne cette nouvelle image (dépendant du temps)
        :return: L'image si la transition est possible sinon None
        """
        if not self.running:
            return None

        if time.time() - self.last_update >= self.delay:
            self.last_update = time.time()
            self.current_frame = (self.current_frame + 1) % self.n_frames

            if not self.loop and self.current_frame == 0:
                self.stop_animation()
                return None

        f_x, f_y = self.flip
        return pygame.transform.rotate(pygame.transform.flip(self.animation.get_frame(self.current_frame), f_x, f_y), self.rotation)

    def start_animation(self, animation: Animation, loop: bool = False, at: int = 0) -> None:
        """
        Démarre le chrono de l'animation renseignée dans la fonction.
        :param animation: L'animation à démarrer
        :param loop: Si l'animation est un boucle
        :param at: L'index de départ
        """
        self.animation = animation
        self.loop = loop
        self.n_frames = animation.get_frame_num()

        self.running = True
        self.current_frame = at
        self.last_update = time.time()

    def stop_animation(self) -> None:
        """
        Arrête l'animation
        """
        self.running = False

    def is_animated(self) -> bool:
        """
        Savoir si l'animateur gère une animation
        :return: Vrai si une animation est en cours d'éxécution sinon, faux
        """
        return self.running

    def reset_settings(self) -> None:
        """
        Remet à jour les paramètres de rotation et les retournements horizontaux et verticaux de l'animation
        """
        self.flip = 0, 0
        self.rotation = 0

    def set_settings(self, flip: tuple[int, int] = (0, 0), rotation: float = 0) -> None:
        """
        Met à jour les paramètres de rendu de l'animation
        :param flip: (x, y) sont des booléens numériques (0 ou 1) avec x/y qui définit si l'image est retourné sur l'axe horizontal/vertical
        :param rotation: Si l'image est retournée d'un angle en degrés
        """
        self.flip = flip
        self.rotation = rotation
