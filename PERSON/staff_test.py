import unittest
from PERSON.person import Person, Staff


class StaffTest(unittest.TestCase):

    def setUp(self):
        self.some_staff = Staff('Maria')

    def test_Staff_inherits_Person(self):
        self.assertTrue(issubclass(Staff, Person), msg='Staff should inherit Person')

    def test_Staff_type(self):
        self.assertEqual(self.some_staff.type, 'staff', msg='Staff type should be staff')

    def test_Staff_name(self):
        self.assertEqual(self.some_staff.name, 'Maria', msg='Staff name is wrong')