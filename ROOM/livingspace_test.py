import unittest
from ROOM.room import Room, LivingSpace


class LivingSpaceTest(unittest.TestCase):

    def setUp(self):
        self.some_living_space = LivingSpace('Yellow')

    def test_LivingSpace_inherits_Room(self):
        self.assertTrue(issubclass(LivingSpace, Room), msg='LivingSpace is not inheriting from Room')

    def test_living_space_name(self):
        self.assertEqual(self.some_living_space.name, 'Yellow', msg='Invalid living space name')

    def test_living_space_type(self):
        self.assertEqual(self.some_living_space.type, 'living', msg='Living space type should be living')

    def test_living_space_occupants_is_dictionary(self):
        self.assertEqual(type(self.some_living_space.occupants), dict, msg='Living space occupants is not a dictionary')

    def test_maximum_living_sapce_occupants(self):
        self.assertEqual(self.some_living_space.maximum_occupants, 4, msg='Wrong number of maximum living space '
                                                                          'occupants')

    def test_living_space_occupants(self):
        self.assertEqual(type(self.some_living_space.occupants), dict, msg='No occupants dictionary in LivingSpace '
'class ')