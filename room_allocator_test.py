from DOJO.dojo import Dojo
from FELLOW.fellow import Fellow
from LIVINGSPACE.livingspace import LivingSpace
from OFFICE.office import Office
from PERSON.person import Person
from STAFF.staff import Staff
from ROOM.room import Room
from room_allocator import InteractiveRoomAllocator
import unittest
from cmd import Cmd
from sqlalchemy import create_engine
from status import State
from sqlalchemy.orm import sessionmaker
import pickle
import sys
from io import StringIO


class CreateRoomTest(unittest.TestCase):
    def setUp(self):
        self.interactive_session = InteractiveRoomAllocator(Dojo())

    # Test interactive session inherits from CMD
    def test_interactive_session_inherits_Cmd(self):
        self.assertTrue(issubclass(InteractiveRoomAllocator, Cmd),
                        msg='InteractiveRoomAllocator class must inherit Cmd')

    # Test intro is correct
    def test_correct_intro(self):
        self.assertEqual(self.interactive_session.intro,
                         "\n\n>>>>>>>>>>>>>>>>>  Eugene's random room allocator for Andela  <<<<<<<<<<<<<<<<<<\n",
                         msg='Wrong intro')

    # Test prompt is correct
    def test_correct_prompt(self):
        self.assertEqual(self.interactive_session.prompt, "\nRoom_Allocator: ", msg='Wrong prompt')

    # Test create_room command creates a Room in some_dojo
    def test_create_room_creates_Room(self):
        arg = {'<room_type>': 'office', '<room_name>': ['Yellow']}

        # Unwrap the do_create_room function to pass arg directly to the function called by create_room command
        self.interactive_session.do_create_room.__wrapped__(self.interactive_session, arg)

        self.assertTrue(isinstance(self.interactive_session.andela_dojo['office_spaces'][arg['<room_name>'][0].lower()], Room),
                        msg='create_room command must create a Room')

    # Test create_room command creates an Office in some_dojo for type = 'office'
    def test_create_room_creates_Office(self):
        arg = {'<room_type>': 'office', '<room_name>': ['Yellow']}

        # Unwrap the do_create_room function to pass arg directly to the function called by create_room command
        self.interactive_session.do_create_room.__wrapped__(self.interactive_session, arg)

        self.assertTrue(
            isinstance(self.interactive_session.andela_dojo['office_spaces'][arg['<room_name>'][0].lower()], Office),
            msg='create_room command must create an Office for type equal to "office"')

    # Test create_room command creates a Living Space in some_dojo for type being 'living'
    def test_create_room_creates_LivingSpace(self):
        arg = {'<room_type>': 'living', '<room_name>': ['Purple']}

        # Unwrap the do_create_room function to pass arg directly to the function called by create_room command
        self.interactive_session.do_create_room.__wrapped__(self.interactive_session, arg)

        self.assertTrue(
            isinstance(self.interactive_session.andela_dojo['living_spaces'][arg['<room_name>'][0].lower()], LivingSpace),
            msg='create_room command must create a LivingSpace for type equal to "living"')

    def test_create_room_can_create_multiple_Office(self):
        arg = {'<room_type>': 'office', '<room_name>': ['Yellow', 'Black', 'Red']}

        # Unwrap the do_create_room function to pass arg directly to the function called by create_room command
        self.interactive_session.do_create_room.__wrapped__(self.interactive_session, arg)

        self.assertTrue(
            isinstance(self.interactive_session.andela_dojo['office_spaces'][arg['<room_name>'][0].lower()], Office),
            msg='create_room command must be able to create several Offices at once')
        self.assertTrue(
            isinstance(self.interactive_session.andela_dojo['office_spaces'][arg['<room_name>'][1].lower()], Office),
            msg='create_room command must be able to create several Offices at once')
        self.assertTrue(
            isinstance(self.interactive_session.andela_dojo['office_spaces'][arg['<room_name>'][2].lower()], Office),
            msg='create_room command must be able to create several Offices at once')

    def test_create_room_can_create_multiple_LivingSpace(self):
        arg = {'<room_type>': 'living', '<room_name>': ['Orange', 'Blue', 'Cream']}

        # Unwrap the do_create_room function to pass arg directly to the function called by create_room command
        self.interactive_session.do_create_room.__wrapped__(self.interactive_session, arg)

        self.assertTrue(
            isinstance(self.interactive_session.andela_dojo['living_spaces'][arg['<room_name>'][0].lower()], LivingSpace),
            msg='create_room command must be able to create several LivingSpaces at once')
        self.assertTrue(
            isinstance(self.interactive_session.andela_dojo['living_spaces'][arg['<room_name>'][1].lower()], LivingSpace),
            msg='create_room command must be able to create several LivingSpaces at once')
        self.assertTrue(
            isinstance(self.interactive_session.andela_dojo['living_spaces'][arg['<room_name>'][2].lower()], LivingSpace),
            msg='create_room command must be able to create several LivingSpaces at once')


class AddPersonTest(unittest.TestCase):
    def setUp(self):
        self.interactive_session = InteractiveRoomAllocator(Dojo())

    def test_unallocated_Person(self):
        arg = {'<first_name>': 'Aretha', '<last_name>': 'Franklin', '<Fellow_or_Staff>': 'Staff', '<wants_accommodation>': 'N'}
        some_guy = 'Aretha Franklin'

        # Unwrap the do_create_room function to pass arg directly to the function called by create_room command
        self.interactive_session.do_add_person.__wrapped__(self.interactive_session, arg)

        self.assertTrue(
            isinstance(self.interactive_session.andela_dojo['unallocated']['Office'][some_guy.lower()], Person),
            msg='add_person command must create Person with unallocated office if their is no free office space')

        arg = {'<first_name>': 'Thelonius', '<last_name>': 'Monk', '<Fellow_or_Staff>': 'Fellow', '<wants_accommodation>': 'Y'}
        other_guy = 'Thelonius Monk'

        # Unwrap the do_create_room function to pass arg directly to the function called by create_room command
        self.interactive_session.do_add_person.__wrapped__(self.interactive_session, arg)

        self.assertTrue(
            isinstance(self.interactive_session.andela_dojo['unallocated']['Living_Space'][other_guy.lower()],
                       Person),
            msg='add_person command must create Person with unallocated living space if their is no free living space')

    def test_staff_is_allocated_office(self):
        arg_person = {'<first_name>': 'John', '<last_name>': 'Hopkins', '<Fellow_or_Staff>': 'Staff', '<wants_accommodation>': 'N'}
        person_name = 'John Hopkins'

        arg_office = {'<room_type>': 'office', '<room_name>': ['Orange']}

        self.interactive_session.do_create_room.__wrapped__(self.interactive_session, arg_office)

        self.interactive_session.do_add_person.__wrapped__(self.interactive_session, arg_person)

        self.assertTrue(isinstance(
            self.interactive_session.andela_dojo['office_spaces'][arg_office['<room_name>'][0].lower()].occupants['Staff'][person_name.lower()], Staff),
            msg='add_person command must create Staff and assign them an office.')

    def test_fellow_is_allocted_office_and_living_space_when_desired(self):
        arg_person = {'<first_name>': 'Larry', '<last_name>': 'King', '<Fellow_or_Staff>': 'Fellow', '<wants_accommodation>': 'Y'}
        person_name = 'Larry King'

        arg_office = {'<room_type>': 'office', '<room_name>': ['Orange']}
        arg_living = {'<room_type>': 'living', '<room_name>': ['Black']}

        self.interactive_session.do_create_room.__wrapped__(self.interactive_session, arg_office)
        self.interactive_session.do_create_room.__wrapped__(self.interactive_session, arg_living)

        self.interactive_session.do_add_person.__wrapped__(self.interactive_session, arg_person)

        self.assertTrue(isinstance(
            self.interactive_session.andela_dojo['office_spaces'][arg_office['<room_name>'][0].lower()].occupants['Fellows'][person_name.lower()], Fellow),
            msg='add_person command must create Fellow and assign them an office and living room if they wish.')

    def test_fellow_is_allocated_office_if_living_space_not_desired(self):
        arg_person = {'<first_name>': 'Larry', '<last_name>': 'King', '<Fellow_or_Staff>': 'Fellow',
                      '<wants_accommodation>': None}
        person_name = 'Larry King'

        arg_office = {'<room_type>': 'office', '<room_name>': ['Orange']}

        self.interactive_session.do_create_room.__wrapped__(self.interactive_session, arg_office)

        self.interactive_session.do_add_person.__wrapped__(self.interactive_session, arg_person)

        self.assertTrue(isinstance(
            self.interactive_session.andela_dojo['office_spaces'][arg_office['<room_name>'][0].lower()].occupants[
                'Fellows'][person_name.lower()], Fellow),
            msg='add_person command must create Fellow and assign them an office and living room if they wish.')


class PrintRoomTest(unittest.TestCase):
    def setUp(self):
        self.interactive_session = InteractiveRoomAllocator(Dojo())

        self.original_print = sys.stdout



        arg_fellow = {'<first_name>': 'Larry', '<last_name>': 'King', '<Fellow_or_Staff>': 'Fellow',
                      '<wants_accommodation>': 'Y'}

        arg_staff = {'<first_name>': 'Jimmy', '<last_name>': 'Kimmel', '<Fellow_or_Staff>': 'staff',
                     '<wants_accommodation>': None}

        arg_office = {'<room_type>': 'office', '<room_name>': ['Orange']}
        arg_living = {'<room_type>': 'living', '<room_name>': ['Black']}

        self.interactive_session.do_create_room.__wrapped__(self.interactive_session, arg_office)
        self.interactive_session.do_create_room.__wrapped__(self.interactive_session, arg_living)

        self.interactive_session.do_add_person.__wrapped__(self.interactive_session, arg_fellow)
        self.interactive_session.do_add_person.__wrapped__(self.interactive_session, arg_staff)

    def test_print_room_prints_room_occupants(self):

        sys.stdout = StringIO()
        self.test_print = sys.stdout

        self.interactive_session.do_print_room.__wrapped__(self.interactive_session, 'black')

        output = "Fellows in living space: Black\n" \
                 "----------------------------------------\n" \
                 "Larry king\n\n\n" \
                 "Office space with such name does not exist\n\n"

        self.assertEqual(self.test_print.getvalue(), output, msg='Print_room not printing correct information')
        sys.stdout = self.original_print

    def test_print_for_non_existent_room(self):

        sys.stdout = StringIO()
        self.test_print = sys.stdout

        self.interactive_session.do_print_room.__wrapped__(self.interactive_session, 'blue')

        output = "Living space with such name does not exist\n\nOffice space with such name does not exist\n\n"
        self.assertEqual(self.test_print.getvalue(), output, msg="Print_room does not give correct output for non-existent rooms")

        sys.stdout = self.original_print

    def test_print_for_office_allocations(self):
        sys.stdout = StringIO()
        self.test_print = sys.stdout

        self.interactive_session.do_print_room.__wrapped__(self.interactive_session, 'orange')

        output = "Living space with such name does not exist\n\n" \
                 "Staff in office space: Orange\n" \
                 "----------------------------------------\n" \
                 "Jimmy kimmel\n\n\n" \
                 "Fellows in office space: Orange\n" \
                 "Larry king\n\n\n"
        self.assertEqual(self.test_print.getvalue(), output, msg="Print_room does not give correct output for offices")

        sys.stdout = self.original_print


class PrintAllocationsTest(unittest.TestCase):
    def setUp(self):
        self.interactive_session = InteractiveRoomAllocator(Dojo())

        self.original_print = sys.stdout

        arg_fellow = {'<first_name>': 'Larry', '<last_name>': 'King', '<Fellow_or_Staff>': 'Fellow',
                      '<wants_accommodation>': 'Y'}

        arg_staff = {'<first_name>': 'Jimmy', '<last_name>': 'Kimmel', '<Fellow_or_Staff>': 'staff',
                     '<wants_accommodation>': None}

        arg_office = {'<room_type>': 'office', '<room_name>': ['Orange']}
        arg_living = {'<room_type>': 'living', '<room_name>': ['Black']}

        self.interactive_session.do_create_room.__wrapped__(self.interactive_session, arg_office)
        self.interactive_session.do_create_room.__wrapped__(self.interactive_session, arg_living)

        self.interactive_session.do_add_person.__wrapped__(self.interactive_session, arg_fellow)
        self.interactive_session.do_add_person.__wrapped__(self.interactive_session, arg_staff)

    def test_printed_allocations(self):
        sys.stdout = StringIO()
        test_print = sys.stdout

        self.interactive_session.do_print_allocations.__wrapped__(self.interactive_session, {"<output>": None})
        output = "Fellows in living space: Black\n" \
                 "----------------------------------------\n" \
                 "Larry king, \n\n\n" \
                 "Occupants of office space: Orange\n" \
                 "----------------------------------------\n" \
                 "Larry king, Jimmy kimmel, \n\n"
        self.assertEqual(test_print.getvalue(), output, msg="Print_allocations gives incorrect output")
        sys.stdout = self.original_print


class SaveStateTest(unittest.TestCase):
    def setUp(self):
        self.interactive_session = InteractiveRoomAllocator(Dojo())

    def test_data_saved_by_save_state(self):
        self.interactive_session.do_save_state.__wrapped__(self.interactive_session, {})

        engine = create_engine('sqlite:///interactive_status.db', echo=False)
        Session = sessionmaker(bind=engine)

        session = Session()

        for back in session.query(State).filter(State.state_name == 'learn'):
            requested_state = pickle.loads(back.state_file)

            self.assertTrue(isinstance(requested_state, Dojo), msg='save_state does not save the dojo object ')


class PrintUnallocatedTest(unittest.TestCase):
    def setUp(self):
        self.interactive_session = InteractiveRoomAllocator(Dojo())

        self.original_print = sys.stdout

        self.arg_fellow = {'<first_name>': 'Larry', '<last_name>': 'King', '<Fellow_or_Staff>': 'Fellow',
                      '<wants_accommodation>': 'Y'}

    def test_print_unallocated_living_space(self):

        self.interactive_session.do_add_person.__wrapped__(self.interactive_session, self.arg_fellow)

        sys.stdout = StringIO()
        test_print = sys.stdout

        self.interactive_session.do_print_unallocated.__wrapped__(self.interactive_session, {'<output>': None})

        output = "\nPersons with unallocated living space:\n" \
                 "----------------------------------------\n" \
                 "Larry king, \n\n" \
                 "\nPersons with unallocated office space:\n" \
                 "----------------------------------------\n" \
                 "Larry king, \n\n"

        self.assertEqual(test_print.getvalue(), output, msg='print_unallocated command is malfunctioning')
        sys.stdout = self.original_print


class LoadStateTest(unittest.TestCase):
    def setUp(self):
        self.interactive_session = InteractiveRoomAllocator(Dojo())

        arg_office = {'<room_type>': 'office', '<room_name>': ['Orange']}
        self.interactive_session.do_create_room.__wrapped__(self.interactive_session, arg_office)
        self.interactive_session.do_save_state.__wrapped__(self.interactive_session, {'<output>': 'test_run'})

    def test_load_state(self):

        self.assertTrue(len(self.interactive_session.andela_dojo['office_spaces']) == 1,
                        msg='Object has not been saved before resetting')

        self.interactive_session = InteractiveRoomAllocator(Dojo())

        self.assertTrue(len(self.interactive_session.andela_dojo['office_spaces']) == 0,
                        msg='Object has not been reset')
        
        self.interactive_session.do_load_state.__wrapped__(self.interactive_session, {'<output>': 'test_run'})

        self.assertTrue(len(self.interactive_session.andela_dojo['office_spaces']) == 1,
                        msg='Object not reloaded after being reset')


class LoadPeopleTest(unittest.TestCase):
    def setUp(self):
        self.interactive_session = InteractiveRoomAllocator(Dojo())

    def test_load_people(self):
        self.interactive_session.do_load_people.__wrapped__(self.interactive_session, {})

        self.assertTrue(len(self.interactive_session.andela_dojo['unallocated']['Office']) == 7,
                        msg='load_people failed to load people into offices')

        self.assertTrue(len(self.interactive_session.andela_dojo['unallocated']['Living_Space']) == 4,
                        msg='load_people failed to load people into living spaces')




if __name__ == '__main__':
    unittest.main()
