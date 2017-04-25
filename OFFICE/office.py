from ROOM.room import Room


class Office(Room):
    def __init__(self, name):
        super().__init__('office', name)