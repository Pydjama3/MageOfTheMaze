class Player:
    def __init__(self, x=0, y=0, room_x=0, room_y=0, inventory=None):
        if inventory is None:
            inventory = []
        self.x = x
        self.y = y
        self.room_x = room_x
        self.room_y = room_y

        self.inventory = inventory

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
