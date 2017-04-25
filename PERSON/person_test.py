import unittest
from PERSON.person import Person


class PersonTest(unittest.TestCase):

    def setUp(self):

        self.some_fellow = Person('John', 'fellow')
        self.some_staff = Person('Mary', 'staff')

    def test_person_name(self):
        self.assertEqual(self.some_fellow.name, 'John', msg='Fellow name is wrong')
        self.assertEqual(self.some_staff.name, 'Mary', msg='Staff name is wrong')

    def test_person_type(self):

        self.assertEqual(self.some_fellow.type, 'fellow', msg='Fellow type should be fellow')
        self.assertEqual(self.some_staff.type, 'staff', msg='Staff type should be staff')
