from utils.structures.gamesprite import GameSprite
from utils.graphisms.animation import Animation
from utils.graphisms.animator import Animator

class ZombieSprite(GameSprite):
    def __init__(self, rect, id_, factor):
        zombie_idle = Animation('assets/zombies/Wild Zombie/Idle.png', 9, factor)
        zombie_moving = Animation('assets/zombies/Wild Zombie/Walk.png', 10, factor)
        zombie_attacking = Animation('assets/zombies/Wild Zombie/Attack_1.png', 4, factor)

        zombie_idle.load_all()
        zombie_moving.load_all()
        zombie_attacking.load_all()

        super().__init__("zombie_"+str(id_), rect, Animator(.2), zombie_idle, zombie_moving, zombie_attacking)
