class Room:
    def __init__(self, type, name):
        self.type = type
        self.name = name

        if self.type == 'living':
            self.occupants = {}
            self.maximum_occupants = 4

        if self.type == 'office':
            self.occupants = {'Staff': {}, 'Fellows': {}}
            self.maximum_occupants = 6


class Office(Room):
    def __init__(self, name):
        super().__init__('office', name)


class LivingSpace(Room):
    def __init__(self, name):
        super().__init__('living', name)
