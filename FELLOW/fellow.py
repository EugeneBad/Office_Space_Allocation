from PERSON.person import Person


class Fellow(Person):
    def __init__(self, name, accommodation):
        super().__init__(name, 'fellow')
        self.accommodation = accommodation
