"""

Usage:
    Room_Allocator:
    Room_Allocator: (-h | --help | --version)

"""
import cmd
from docopt import docopt
import sys
from DOJO.dojo import Dojo
from FELLOW.fellow import Fellow
from LIVINGSPACE.livingspace import LivingSpace
from OFFICE.office import Office
from STAFF.staff import Staff
import pickle
from docopt_decorator import docopt_cmd
import random


class InteractiveRoomAllocator(cmd.Cmd):
    intro = "\n\n>>>>>>>>>>>>>>>>>>>Eugene's random room allocator for Andela<<<<<<<<<<<<<<<<<<<<\n"
    prompt = "Room_Allocator: "
    file = None

    def __init__(self, dojo_object):
        super().__init__()
        self.andela_dojo = dojo_object

    # Create the Dojo object.

    # Function to implement the CLI command create_room.
    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        counter = 0
        #  Check if room is an office.
        if arg['<room_type>'] == 'office':

            #  Add it as a value to the office_spaces dictionary in andela_dojo.
            for each_office in arg['<room_name>']:

                self.andela_dojo['office_spaces'][each_office] = Office(each_office)

                print('An office called {} has been successfully created!'.format(arg['<room_name>'][counter]))
                counter += 1

        #  Check if room is a living space.
        if arg['<room_type>'] == 'living':

            #  Add it as a value to the living_spaces dictionary in andela_dojo.
            for each_living_space in arg['<room_name>']:
                self.andela_dojo['living_spaces'][each_living_space] = LivingSpace(each_living_space)

                print('A living space called {} has been successfully created!'.format(arg['<room_name>'][counter]))
                counter += 1

    # Function to implement the CLI command add_person.
    @docopt_cmd
    def do_add_person(self, arg):
        """Usage:
        add_person <person_name> <Fellow_or_Staff> [<wants_accommodation>]"""

        # Check if person is staff and wants accommodation.
        if arg['<Fellow_or_Staff>'] == 'Staff' and arg['<wants_accommodation>'] == 'Y':
            print('Staff cannot be allocated living spaces')

        # Randomly select an office from the office_spaces dictionary in andela_dojo,
        # store it in random_office variable
        office_list = [office for office in self.andela_dojo['office_spaces'].values() if len(office.occupants) < 7]

        if len(office_list) > 0:
            random_office_index = random.randint(0, len(office_list)-1)
            random_office = office_list[random_office_index]

        if len(office_list) == 0:
            random_office = None

        # Randomly select a living space from the living_spaces dictionary in andela_dojo,
        # store it in random_living_space variable
        living_space_list = [living_space for living_space in self.andela_dojo['living_spaces'].values() if len(living_space.occupants) < 5]

        if len(living_space_list) > 0:
            random_living_space_index = random.randint(0, len(living_space_list)-1)
            random_living_space = living_space_list[random_living_space_index]

        if len(living_space_list) == 0:
            random_living_space = None

        # If staff entry is valid, add person to Staff dictionary in the occupants attribute of the random_office
        if arg['<Fellow_or_Staff>'] == 'Staff' and arg['<wants_accommodation>'] != 'Y':

            if random_office is not None:
                random_office.occupants['Staff'][arg['<person_name>']] = Staff(arg['<person_name>'])

                print('Staff {} has been added successfully!'.format(arg['<person_name>']))
                print('{} has been given office: {}'.format(arg['<person_name>'], random_office.name))

            if random_office is None:
                self.andela_dojo['unallocated']['Office'][arg['<person_name>']] = Staff(arg['<person_name>'])
                print('Staff {} has unallocated Office Space'.format(arg['<person_name>']))

        # If fellow wants accommodation:
        if arg['<Fellow_or_Staff>'] == 'Fellow' and arg['<wants_accommodation>'] == 'Y':

            if random_living_space is not None:

                # Add Fellow to Fellow dictionary in the occupants attribute of the random_random_living_space
                random_living_space.occupants[arg['<person_name>']] = Fellow(arg['<person_name>'], 'Y')

                print('Fellow {} has been added successfully!'.format(arg['<person_name>']))
                print('{} has been given living space: {}'.format(arg['<person_name>'], random_living_space.name))

            if random_living_space is None:
                self.andela_dojo['unallocated']['Living_Space'][arg['<person_name>']] = Fellow(arg['<person_name>'], 'Y')
                print('Fellow {} has unallocated Living Space'.format(arg['<person_name>']))

            if random_office is None:
                self.andela_dojo['unallocated']['Office'][arg['<person_name>']] = Fellow(arg['<person_name>'], 'Y')
                print('Fellow {} has unallocated Office Space'.format(arg['<person_name>']))

            if random_office is not None:

                # Add Fellow to Fellow dictionary in the occupants attribute of the random_random_living_space
                random_office.occupants['Fellows'][arg['<person_name>']] = Fellow(arg['<person_name>'], 'Y')

        # If fellow does not want accommodation:
        if arg['<Fellow_or_Staff>'] == 'Fellow' and arg['<wants_accommodation>'] != 'Y':

            if random_office is not None:
                # Add Fellow to Fellow dictionary in the occupants attribute of the random_office
                random_office.occupants['Fellows'][arg['<person_name>']] = Fellow(arg['<person_name>'], 'N')

                print('Fellow {} has been added successfully!'.format(arg['<person_name>']))
                print('{} has been given office: {}'.format(arg['<person_name>'], random_office.name))

            if random_office is None:
                self.andela_dojo['unallocated']['Office'][arg['<person_name>']] = Fellow(arg['<person_name>'], 'N')
                print('Fellow {} has unallocated Office Space'.format(arg['<person_name>']))

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('\n\t\t****************Good Bye****************')
        exit()

    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""

        try:
            room_requested = self.andela_dojo['living_spaces'][arg]

            print('Fellows in living space: {}'.format(arg))
            print('----------------------------------------')

            if len(room_requested.occupants) > 0:
                for Fellows in room_requested.occupants.values():

                    print(Fellows.name)
                print('\n')
            else:
                print('None\n')

        except KeyError:
            print("Living space with such name does not exist\n")

        try:
            room_requested = self.andela_dojo['office_spaces'][arg]

            print('Staff in office space: {}'.format(arg))
            print('----------------------------------------')
            if len(room_requested.occupants['Staff']) > 0:
                for Staff in room_requested.occupants['Staff'].values():
                    print(Staff.name)
                print('\n')
            else:
                print('None\n')
            print('Fellows in office space: {}'.format(arg))
            if len(room_requested.occupants['Staff']) > 0:
                for Fellows in room_requested.occupants['Fellows'].values():
                    print(Fellows.name)
                print('\n')
            else:
                print('None\n')

        except KeyError:
            print("Office space with such name does not exist\n")

    def do_print_allocations(self, arg):
        """Usage: print_allocations [<output>]"""

        living_spaces = self.andela_dojo['living_spaces']
        office_spaces = self.andela_dojo['office_spaces']

        if arg == 'Y':

            output = open("E:\have_allocations.txt", "w+")
        else:
            print('Dear')
            output = None

        for living_space in living_spaces.values():
            print('Fellows in living space: {}'.format(living_space.name), file=output, flush=True)
            print('----------------------------------------', file=output, flush=True)

            if len(living_space.occupants.values()) > 0:
                for Fellows in living_space.occupants.values():
                    print(Fellows.name + ', ', file=output, flush=True)
                print('\n', file=output, flush=True)
            else:
                print('None\n', file=output, flush=True)

        for office_space in office_spaces.values():

            print('Occupants of office space: {}'.format(office_space.name), file=output, flush=True)
            print('----------------------------------------', file=output, flush=True)

            if len(office_space.occupants['Fellows'].values()) > 0:
                for Fellows in office_space.occupants['Fellows'].values():
                    print(Fellows.name + ', ', file=output, flush=True)
            else:
                print('No Fellows', file=output, flush=True)

            if len(office_space.occupants['Staff'].values()):
                for Staff in office_space.occupants['Staff'].values():
                    print(Staff.name + ', ', file=output, flush=True)
            else:
                print('No Staff', file=output, flush=True)

            if arg == 'Y':

                output.close()

    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [<output>] """

        unallocated_office_space = self.andela_dojo['unallocated']['Office']
        unallocated_living_space = self.andela_dojo['unallocated']['Living_Space']

        if arg == 'Y':
            output = open("E:\have_no_allocations.txt", "w+")
        else:
            output = None

        print('\nPersons with unallocated living space:', file=output, flush=True)
        print('----------------------------------------', file=output, flush=True)

        if len(unallocated_living_space.values()) > 0:
            for Person in unallocated_living_space.values():
                print(Person.name, end=', ', file=output, flush=True)
            print('\n', file=output, flush=True)
        else:
            print('None\n', file=output, flush=True)

        print('\nPersons with unallocated office space:', file=output, flush=True)
        print('----------------------------------------', file=output, flush=True)

        if len(unallocated_office_space.values()) > 0:
            for Person in unallocated_office_space.values():
                print(Person.name, end=', ', file=output, flush=True)
            print('\n', file=output, flush=True)
        else:
            print('None\n', file=output, flush=True)

    def do_load_state(self, arg):
        """Usage load_state [<output>] """
        pass

    def do_save_state(self, arg):
        """Usage: load_state [<output>]"""
        with open("status.pickle", "wb") as status:
            pickle.dump(self.andela_dojo(), status, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    opt = docopt(__doc__, sys.argv[1:])
    InteractiveRoomAllocator(Dojo()).cmdloop()
