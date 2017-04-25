import unittest
from OFFICE.office import Office
from ROOM.room import Room


class OfficeTest(unittest.TestCase):

    def setUp(self):
        self.some_office = Office('Yellow')

    def test_Office_inherits_Room(self):
        self.assertTrue(issubclass(Office, Room), msg='Office is not inheriting from Room')

    def test_office_name(self):
        self.assertEqual(self.some_office.name, 'Grey', msg='Invalid office name')

    def test_office_type(self):
        self.assertEqual(self.some_office.type, 'office', msg='Office space type should office')

    def test_office_occupants_is_dictionary(self):
        self.assertEqual(type(self.some_office.occupants), dict, msg='Office space occupants is not a dictionary')

    def test_maximum_office_occupants(self):
        self.assertEqual(self.some_office.maximum_occupants, 6, msg='Wrong number of maximum office occupants')

    def test_office_occupants(self):
        self.assertEqual(type(self.some_office.occupants['staff']), dict, msg='Staff dictionary in occupants does not exist')
        self.assertEqual(type(self.some_office.occupants['fellow']), dict, msg='Living dictionary in occupants does not exist')