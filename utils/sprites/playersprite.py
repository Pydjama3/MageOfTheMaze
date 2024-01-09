from utils.structures import GameSprite
from utils.graphisms.animation import Animation
from utils.graphisms.animator import Animator


class PlayerSprite(GameSprite):
    def __init__(self, rect, factor):
        player_idle = Animation('assets/raiders/Raider_3/Idle.png', 6, factor)
        player_moving = Animation('assets/raiders/Raider_3/Walk.png', 7, factor)
        player_attacking = Animation('assets/raiders/Raider_3/Attack_1.png', 5, factor)

        player_idle.load_all()
        player_moving.load_all()
        player_attacking.load_all()

        super().__init__("player", rect, Animator(.1), player_idle, player_moving, player_attacking)
