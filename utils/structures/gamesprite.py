from pygame.sprite import Sprite
from Game.player import PlayerState
from utils.graphisms.animation import Animation
from utils.graphisms.animator import Animator


class GameSprite(Sprite):
    def __init__(self, identity, rect, animator: Animator, idle: Animation, moving: Animation, attack: Animation):
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

    def set_state(self, state):
        if state != self.current_state:
            self.animator.stop_animation()
            self.animator.start_animation(self.state_to_anim[state], state != PlayerState.FIGHTING)

        self.current_state = state

    def set_animator_settings(self, flip=(0, 0), rotation=0):
        self.flip = flip
        self.rotation = rotation

    def update(self, x, y):
        self.rect.x = x
        self.rect.y = y

        self.animator.set_settings(self.flip, self.rotation)
        self.image = self.animator.update()
        return self.image is not None
