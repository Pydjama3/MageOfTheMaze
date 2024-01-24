import enum


class PlayerState(enum.Enum):
    IDLE = 0
    MOVING = 1
    FIGHTING = 2


class Player:
    def __init__(self, x: float = 0, y: float = 0, room_x: int = 0, room_y: int = 0, inventory: list = None) -> None:
        """
        Créer un objet de type Player avec une position définie
        :param x: la position dans la pièce
        :param y: "
        :param room_x: la pièce dans le labyrinthe
        :param room_y: "
        :param inventory: l'inventeur du joueur
        """
        if inventory is None:
            inventory = []
        self.x = x
        self.y = y
        self.room_x = room_x
        self.room_y = room_y

        self.speed = 0
        self.move_x = 0
        self.move_y = 0
        self.orientation = 1
        self.state = PlayerState.IDLE

        self.on_door = False

        self.inventory = inventory

    def set_speed(self, speed: float) -> None:
        """
        Définit la vitesse du joueur
        :param speed: la vitesse du joueur
        """
        self.speed = speed

    def move(self, direction: tuple) -> None:
        """
        Définit le déplacement du joueur par rapport au valeurs indiquées Ces valeurs ne seront pas forcment celles
        en vigueur après la mise à jour du joueur car elles peuvent être modifiées par un autre appel de cette
        fonction ou par block_move_x/y
        :param direction: la direction du mouvement sous forme (x, y)
        """
        x, y = direction
        self.move_x += x
        self.move_y += y

    def block_move_x(self, x: int) -> None:
        """
        Bloque le mouvement sur l'axe x :param x: si le signe de ce paramètre est le même que celui de la variation
        de mouvement sur cet axe, le mouvement est bloqué sur cet axe: si x=1 alors le mouvement positif est bloqué,
        et inversement si x=-1
        """
        if x > 0:
            self.move_x = min(self.move_x, 0)
        else:
            self.move_x = max(self.move_x, 0)

    def block_move_y(self, y: int) -> None:
        """
        Bloque le mouvement sur l'axe y :param y: si le signe de ce paramètre est le même que celui de la variation
        de mouvement sur cet axe, le mouvement est bloqué sur cet axe: si y=1 alors le mouvement positif est bloqué,
        et inversement si y=-1
        """
        if y > 0:
            self.move_y = min(self.move_y, 0)
        else:
            self.move_y = max(self.move_y, 0)

    def apply_movement(self) -> None:
        """
        Met à jour la position du joueur et son attétat par rapport aux appels des fonction move et block_move_x/y
        antèrieurs à l'appel de cette fonction
        """
        self.x += self.move_x * self.speed
        self.y += self.move_y * self.speed

        if self.move_x == 0 and self.move_y == 0:
            self.state = PlayerState.IDLE
        else:
            self.state = PlayerState.MOVING
            self.orientation = int(self.move_x/abs(self.move_x)) if self.move_x != 0 else self.orientation

    def reset_movement(self) -> None:
        """
        Réinitialise le mouvement du joueur et son état
        """
        self.state = PlayerState.IDLE

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

    def set_on_door(self, state):
        self.on_door = state
