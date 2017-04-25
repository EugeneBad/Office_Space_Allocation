from ROOM.room import Room


class LivingSpace(Room):
    def __init__(self, name):
        super().__init__('living', name)
