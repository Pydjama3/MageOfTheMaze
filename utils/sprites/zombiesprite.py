from utils.structures.gamesprite import GameSprite
from utils.graphisms.animation import Animation
from utils.graphisms.animator import Animator

class ZombieSprite(GameSprite):
    def __init__(self, rect, id_, factor):
        player_idle = Animation('/assets/zombies/Wild Zombie/Idle.png', 6, factor)
        player_moving = Animation('/assets/zombies/Wild Zombie/Walk.png', 7, factor)
        player_attacking = Animation('/assets/zombies/Wild Zombie/Attack_1.png', 5, factor)

        super().__init__("zombie_"+str(id_), rect, Animator(.2), player_idle, player_moving, player_attacking)
