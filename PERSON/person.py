class Person:
    def __init__(self, name, type):
        self.name = name
        self.type = type


class Staff(Person):
    def __init__(self, name):
        super().__init__(name, 'staff')


class Fellow(Person):
    def __init__(self, name, accommodation):
        super().__init__(name, 'fellow')
        self.accommodation = accommodation
