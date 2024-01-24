import pygame
from pygame.sprite import Sprite
from Game.player import PlayerState
from utils.graphisms.animation import Animation
from utils.graphisms.animator import Animator


class GameSprite(Sprite):
    def __init__(self, identity: str | object, rect: pygame.Rect, animator: Animator, idle: Animation,
                 moving: Animation, attack: Animation) -> None:
        """
        Crée un sprite générique avec un animateur et des animations pour les attaques, le mouvement et le repos.
        :param identity: Son identité (interne)
        :param rect: La taille de ce personnage
        :param animator: L'animateur qui gère ses animation
        :param idle: Animation de repos
        :param moving: Animation du mouvement
        :param attack: Animation de l'attaque
        """
        super().__init__()

        self.identity = identity
        self.rect = rect
        self.animator = animator
        self.idle = idle
        self.moving = moving
        self.attack = attack

        self.flip = (0, 0)  # = 1 -> towards right
        self.rotation = 0

        self.state_to_anim = {
            PlayerState.IDLE: self.idle,
            PlayerState.MOVING: self.moving,
            PlayerState.FIGHTING: self.attack
        }

        self.current_state = None
        self.set_state(PlayerState.IDLE)

        self.image = None

    def set_state(self, state: PlayerState) -> None:
        """
        Défini l'état actuel du sprite
        :param state: L'état appliqué
        """
        if state != self.current_state:
            self.animator.stop_animation()
            self.animator.start_animation(self.state_to_anim[state], state != PlayerState.FIGHTING)

        self.current_state = state

    def set_animator_settings(self, flip: tuple[int, int] = (0, 0), rotation: float = 0) -> None:
        """
        Définit les paramètres de l'image quand les animations sont jouées
        :param flip: Le retournement 4d de l'image (j'ai pas les mots sur le moment)
        :param rotation: La rotation de l'image
        """
        self.flip = flip
        self.rotation = rotation

    def update(self, x: float, y: float) -> pygame.Surface | None:
        """
        Met à jour la position du sprite pour qu'il soit plus tard affiché sur l'écran
        :param x: La position x
        :param y: La position y
        :return: L'image si elle existe sinon <None>
        """
        self.rect.x = x
        self.rect.y = y

        self.animator.set_settings(self.flip, self.rotation)
        self.image = self.animator.update()
        return self.image is not None
