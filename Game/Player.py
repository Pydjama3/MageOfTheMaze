class Player:
    def __init__(self, x=0, y=0, room_x=0, room_y=0, inventory=None):
        if inventory is None:
            inventory = []
        self.x = x
        self.y = y
        self.room_x = room_x
        self.room_y = room_y
        self.move_x = 0
        self.move_y = 0
        self.speed = 0

        self.inventory = inventory

    def set_speed(self, speed):
        self.speed = speed

    def move(self, direction):
        x, y = direction
        self.move_x += x
        self.move_y += y

    def block_move_x(self, x):
        if x > 0:
            self.move_x = min(self.move_x, x)
        else:
            self.move_x = max(self.move_x, x)

    def block_move_y(self, y):
        if y > 0:
            self.move_y = min(self.move_y, 0)
        else:
            self.move_y = max(self.move_y, 0)

    def apply_movement(self):
        self.x += self.move_x * self.speed
        self.y += self.move_y * self.speed
    
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
