import  unittest
from OFFICE.office import Office
from ROOM.room import Room

class OfficeTest(unittest.TestCase):

    def setUp(self):
        some_office = Office('Yellow')

    def test_Office_inherits_Room(self):
        self.assertTrue(issubclass(Office, Room), msg='Office is not inheriting from Room')

    