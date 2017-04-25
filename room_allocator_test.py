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
        self.interactive_session = InteractiveRoomAllocator(Dojo())

    # Test interactive session inherits from CMD
    def test_interactive_session_inherits_Cmd(self):
        self.assertTrue(issubclass(InteractiveRoomAllocator, Cmd),
                        msg='InteractiveRoomAllocator class must inherit Cmd')

    # Test intro is correct
    def test_correct_intro(self):
        self.assertEqual(self.interactive_session.intro, "\n\t\tEugene's random room allocator for Andela\n",
                         msg='Wrong intro')

    # Test prompt is correct
    def test_correct_prompt(self):
        self.assertEqual(self.interactive_session.prompt, "Room_Allocator: ", msg='Wrong prompt')

    # Test create_room command creates a Room in some_dojo
    def test_create_room_creates_Room(self):
        arg = {'<room_type>': 'office', '<room_name>': ['Yellow']}

        # Unwrap the do_create_room function to pass arg directly to the function called by create_room command
        self.interactive_session.do_create_room.__wrapped__(self.interactive_session, arg)

        self.assertTrue(isinstance(self.interactive_session.andela_dojo['office_spaces'][arg['<room_name>'][0]], Room),
                        msg='create_room command must create a Room')

    # Test create_room command creates an Office in some_dojo for type = 'office'
    def test_create_room_creates_Office(self):
        arg = {'<room_type>': 'office', '<room_name>': ['Yellow']}

        # Unwrap the do_create_room function to pass arg directly to the function called by create_room command
        self.interactive_session.do_create_room.__wrapped__(self.interactive_session, arg)

        self.assertTrue(isinstance(self.interactive_session.andela_dojo['office_spaces'][arg['<room_name>'][0]], Office),
                        msg='create_room command must create an Office for type equal to "office"')

    # Test create_room command creates a Living Space in some_dojo for type being 'living'
    def test_create_room_creates_LivingSpace(self):
        arg = {'<room_type>': 'living', '<room_name>': 'Purple'}

        # Unwrap the do_create_room function to pass arg directly to the function called by create_room command
        self.interactive_session.do_create_room.__wrapped__(self.interactive_session, arg)

        self.assertTrue(isinstance(self.interactive_session.andela_dojo['living_spaces'][arg['<room_name>']], LivingSpace),
                        msg='create_room command must create a LivingSpace for type equal to "living"')

    def test_create_room_can_create_multiple_Office(self):
        arg = {'<room_type>': 'office', '<room_name>': ['Yellow', 'Black', 'Red']}

        # Unwrap the do_create_room function to pass arg directly to the function called by create_room command
        self.interactive_session.do_create_room.__wrapped__(self.interactive_session, arg)

        self.assertTrue(isinstance(self.interactive_session.andela_dojo['office_spaces'][arg['<room_name>'][0]], Office),
                        msg='create_room command must be able to create several Offices at once')
        self.assertTrue(isinstance(self.interactive_session.andela_dojo['office_spaces'][arg['<room_name>'][1]], Office),
                        msg='create_room command must be able to create several Offices at once')
        self.assertTrue(isinstance(self.interactive_session.andela_dojo['office_spaces'][arg['<room_name>'][2]], Office),
                        msg='create_room command must be able to create several Offices at once')
