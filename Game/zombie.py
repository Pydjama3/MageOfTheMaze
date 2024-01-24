import enum


class ZombieState(enum.Enum):
    IDLE = 0
    MOVING = 1
    FIGHTING = 2


class Zombie:

    def __init__(self, x: float = 0, y: float = 0, inventory: list = None) -> None:
        """
        Similairement à Player, cette classe gère le déplacement et les actions des zombies
        ATTENTION: cette classe est en cours de développement et n'est pas du tout opérationnelle
        :param x: la position du zombie dans la pièce
        :param y: "
        :param inventory: l'inventaire du zombie
        """
        if inventory is None:
            inventory = []
        self.x = x
        self.y = y

        self.speed = 0
        self.move_x = 0
        self.move_y = 0
        self.orientation = 1
        self.state = ZombieState.IDLE

        self.inventory = inventory

    def set_speed(self, speed):
        self.speed = speed

    def move(self, direction):
        x, y = direction
        self.move_x += x
        self.move_y += y

    def block_move_x(self, x):
        if x > 0:
            self.move_x = min(self.move_x, 0)
        else:
            self.move_x = max(self.move_x, 0)

    def block_move_y(self, y):
        if y > 0:
            self.move_y = min(self.move_y, 0)
        else:
            self.move_y = max(self.move_y, 0)

    def apply_movement(self):
        self.x += self.move_x * self.speed
        self.y += self.move_y * self.speed

        if self.move_x == 0 and self.move_y == 0:
            self.state = ZombieState.IDLE
        else:
            self.state = ZombieState.MOVING
            self.orientation = int(self.move_x/abs(self.move_x)) if self.move_x != 0 else self.orientation

    def reset_movement(self):
        self.state = ZombieState.IDLE

        self.move_x = 0
        self.move_y = 0
    
    def change_room(self, x, y):
        self.room_x = x
        self.room_y = y

    def get_current(self):
        return self.room_x, self.room_y, self.x, self.y

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def print_inventory(self):
        print(self.inventory)

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state
