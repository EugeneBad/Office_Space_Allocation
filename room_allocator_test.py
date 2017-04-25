from DOJO.dojo import Dojo
from FELLOW.fellow import Fellow
from LIVINGSPACE.livingspace import LivingSpace
from OFFICE.office import Office
from PERSON.person import Person
from ROOM.room import Room
from room_allocator import InteractiveRoomAllocator
import unittest
from cmd import Cmd


class CreateRoomTest(unittest.TestCase):
    def setUp(self):
        self.some_dojo = Dojo()
        self.interactive_session = InteractiveRoomAllocator(self.some_dojo)


    # Test interactive session inherits from CMD
    def test_interactive_session_inherits_Cmd(self):
        self.assertTrue(issubclass(InteractiveRoomAllocator, Cmd), msg='InteractiveRoomAllocator class must inherit Cmd')

    # Test intro is correct
    def test_correct_intro(self):
        self.assertEqual(self.interactive_session.intro, "\n\t\tEugene's random room allocator for Andela\n", msg='Wrong intro')

    # Test prompt is correct
    def test_correct_prompt(self):
        self.assertEqual(self.interactive_session.prompt, "Room_Allocator: ", msg='Wrong prompt')

