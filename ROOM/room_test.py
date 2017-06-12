from ROOM.room import Room
import unittest


class RoomTest(unittest.TestCase):

    def setUp(self):
        self.office = Room('office', 'Grey')
        self.living = Room('living', 'White')

    def test_room_name(self):
        self.assertEqual(self.office.name, 'Grey', msg='Invalid office name')
        self.assertEqual(self.living.name, 'White', msg='Invalid living space name')

    def test_room_type(self):
        self.assertEqual(self.office.type, 'office', msg='Office space type should office')
        self.assertEqual(self.living.type, 'living', msg='Living space type should living')

    def test_room_occupants_is_dictionary(self):
        self.assertEqual(type(self.office.occupants), dict, msg='Office space occupants is not a dictionary')
        self.assertEqual(type(self.living.occupants), dict, msg='Living space occupants is not a dictionary')

    def test_maximum_room_occupants(self):
        self.assertEqual(self.office.maximum_occupants, 6, msg='Wrong number of maximum office occupants')
        self.assertEqual(self.living.maximum_occupants, 4, msg='Wrong number of maximum office occupants')

    def test_office_occupants(self):
        self.assertEqual(type(self.office.occupants['Staff']), dict, msg='Staff dictionary in occupants does not exist')
        self.assertEqual(type(self.office.occupants['Fellows']), dict, msg='Living dictionary in occupants does not '
                                                                           'exist')