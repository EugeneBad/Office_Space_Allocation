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

from docopt_decorator import docopt_cmd
import random


class InteractiveRoomAllocator(cmd.Cmd):
    intro = "\n\t\tEugene's random room allocator for Andela\n"
    prompt = "Room_Allocator: "
    file = None

    def __init__(self, dojo_object):
        super().__init__()
        self.andela_dojo = dojo_object

    # Create the Dojo object.

    # Function to implement the CLI command create_room.
    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>"""

        #  Check if room is an office.
        if arg['<room_type>'] == 'office':

            #  Add it as a value to the office_spaces dictionary in andela_dojo.
            self.andela_dojo['office_spaces'][arg['<room_name>']] = Office(arg['<room_name>'])

            print('An office called {} has been successfully created!'.format(arg['<room_name>']))

        #  Check if room is a living space.
        if arg['<room_type>'] == 'living':

            #  Add it as a value to the living_spaces dictionary in andela_dojo.
            self.andela_dojo['living_spaces'][arg['<room_name>']] = LivingSpace(arg['<room_name>'])

            print('A living space called {} has been successfully created!'.format(arg['<room_name>']))

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
        office_list = [office for office in self.andela_dojo['office_spaces'].values()]
        random_office_index = random.randint(0, len(office_list)-1)
        random_office = office_list[random_office_index]

        # Randomly select a living space from the living_spaces dictionary in andela_dojo,
        # store it in random_living_space variable
        living_space_list = [living_space for living_space in self.andela_dojo['living_spaces'].values()]
        random_living_space_index = random.randint(0, len(living_space_list)-1)
        random_living_space = living_space_list[random_living_space_index]

        # If staff entry is valid, add person to Staff dictionary in the occupants attribute of the random_office
        if arg['<Fellow_or_Staff>'] == 'Staff' and arg['<wants_accommodation>'] != 'Y':
            random_office.occupants['Staff'][arg['<person_name>']] = Staff(arg['<person_name>'])

            print('Staff {} has been added successfully!'.format(arg['<person_name>']))
            print('{} has been given office: {}'.format(arg['<person_name>'], random_office.name))

        # If fellow wants accommodation:
        if arg['<Fellow_or_Staff>'] == 'Fellow' and arg['<wants_accommodation>'] == 'Y':

            # Add Fellow to Fellow dictionary in the occupants attribute of the random_office
            random_office.occupants['Fellows'][arg['<person_name>']] = Fellow(arg['<person_name>'], 'Y')

            # Add Fellow to Fellow dictionary in the occupants attribute of the random_random_living_space
            random_living_space.occupants[arg['<person_name>']] = Fellow(arg['<person_name>'], 'Y')

            print('Fellow {} has been added successfully!'.format(arg['<person_name>']))
            print('{} has been given office: {}'.format(arg['<person_name>'], random_office.name))
            print('{} has been given living space: {}'.format(arg['<person_name>'], random_living_space.name))

        # If fellow does not want accommodation:
        if arg['<Fellow_or_Staff>'] == 'Fellow' and arg['<wants_accommodation>'] != 'Y':

            # Add Fellow to Fellow dictionary in the occupants attribute of the random_office
            random_office.occupants['Fellows'][arg['<person_name>']] = Fellow(arg['<person_name>'], 'N')

            print('Fellow {} has been added successfully!'.format(arg['<person_name>']))
            print('{} has been given office: {}'.format(arg['<person_name>'], random_office.name))

if __name__ == '__main__':
    opt = docopt(__doc__, sys.argv[1:])
    InteractiveRoomAllocator(Dojo()).cmdloop()
