"""

Usage:
    Room_Allocator:
    Room_Allocator: (-h | --help | --version)

"""
import cmd
from docopt import docopt
import sys
from docopt_decorator import docopt_cmd
# Class importations
from DOJO.dojo import Dojo
from FELLOW.fellow import Fellow
from LIVINGSPACE.livingspace import LivingSpace
from OFFICE.office import Office
from STAFF.staff import Staff

import random
# Importations for database
import pickle
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from status import State
from sqlalchemy.orm import sessionmaker


# Main class called to maintain interactive session
class InteractiveRoomAllocator(cmd.Cmd):
    intro = "\n\n>>>>>>>>>>>>>>>>>  Eugene's random room allocator for Andela  <<<<<<<<<<<<<<<<<<\n"
    prompt = "\nRoom_Allocator: "
    file = None

    # Class takes in a Dojo object to work with
    def __init__(self, dojo_object):
        super().__init__()
        self.andela_dojo = dojo_object

    # Function to implement the CLI command create_room.
    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        counter = 0

        #  Check if room is an office.
        if arg['<room_type>'].lower() == 'office':

            #  Loop through each office that has been entered.
            for each_office in arg['<room_name>']:

                # Check if the office already exists.
                if arg['<room_name>'][counter].lower() in self.andela_dojo['office_spaces']:
                    print('An office called {} already exits'.format(arg['<room_name>'][counter].capitalize()))
                    counter += 1
                    continue

                self.andela_dojo['office_spaces'][each_office.lower()] = Office(each_office.lower())

                print('An office called {} has been successfully created!'.format(arg['<room_name>'][counter].capitalize()))

                counter += 1
                # After office has been created, populate the list of people without offices.
                officeless_people = self.andela_dojo['unallocated']['Office'].values()
                people_reallocated_offices = []

                # Loop through each person without an office and add them to the newly created office
                for person in officeless_people:
                    if len(people_reallocated_offices) < 6:
                        if person.type.lower() == 'staff':

                            self.andela_dojo['office_spaces'][each_office.lower()].occupants['Staff'][person.name.lower()] = \
                                Staff(person.name.lower())

                            people_reallocated_offices.append(person.name.lower())

                            print('Staff {} has been successfully moved'
                                  ' to the new office: {}'.format(person.name.capitalize(), each_office.capitalize()))

                        if person.type.lower() == 'fellow':

                            self.andela_dojo['office_spaces'][each_office.lower()].occupants['Fellows'][person.name.lower()] = \
                                Fellow(person.name.lower(), person.accommodation)

                            people_reallocated_offices.append(person.name.lower())

                            print('Fellow {} has been successfully moved '
                                  'to the new office: {}'.format(person.name.capitalize(), each_office.capitalize()))

                # After person is added to the new office, remove them from list of people unallocated offices
                for person in people_reallocated_offices:
                    del self.andela_dojo['unallocated']['Office'][person]

        # Check if room is a living space.
        if arg['<room_type>'].lower() == 'living':

            #  Loop through all the living spaces that have been entered.
            for each_living_space in arg['<room_name>']:

                # Check if living space already exists.
                if arg['<room_name>'][counter].lower() in self.andela_dojo['living_spaces']:
                    print('A living space called {} already exits'.format(arg['<room_name>'][counter].capitalize()))
                    counter += 1
                    continue

                self.andela_dojo['living_spaces'][each_living_space.lower()] = LivingSpace(each_living_space.lower())

                print('A living space called {} has been successfully created!'.format(arg['<room_name>'][counter]))
                counter += 1

                # Populate list of fellow without living spaces.
                living_spaceless_fellows = self.andela_dojo['unallocated']['Living_Space'].values()
                fellows_reallocated_living_spaces = []

                # Loop through each fellow and add them to the newly created room.
                for fellow in living_spaceless_fellows:
                    if len(fellows_reallocated_living_spaces) < 4:
                        self.andela_dojo['living_spaces'][each_living_space.lower()].occupants[fellow.name.lower()] = \
                            Fellow(fellow.name.lower(), fellow.accommodation)

                        fellows_reallocated_living_spaces.append(fellow.name.lower())

                        print('Fellow {} has been successfully moved'
                              ' to the new living space: {}'.format(fellow.name.capitalize(), each_living_space.capitalize()))

                # After fellow has been added to the new living space, remove them
                # from list of people unallocated living spaces
                for fellow in fellows_reallocated_living_spaces:
                    del self.andela_dojo['unallocated']['Living_Space'][fellow]

    # Function to implement the CLI command add_person.
    @docopt_cmd
    def do_add_person(self, arg):
        """Usage:
        add_person <first_name> <last_name> <Fellow_or_Staff> [<wants_accommodation>]"""

        person_name = arg['<first_name>'] + ' ' + arg['<last_name>']

        # Check if person is staff and wants accommodation.
        if arg['<Fellow_or_Staff>'].lower() == 'staff' and arg['<wants_accommodation>'] == 'Y':
            print('Staff cannot be allocated living spaces')

        # Randomly select an office from the office_spaces dictionary in andela_dojo,
        # store it in random_office variable
        office_list = [office for office in self.andela_dojo['office_spaces'].values()
                       if (len(office.occupants['Staff']) + len(office.occupants['Fellows'])) < 6]

        if len(office_list) > 0:
            random_office_index = random.randint(0, len(office_list) - 1)
            random_office = office_list[random_office_index]

        if len(office_list) == 0:
            random_office = None

        # Randomly select a living space from the living_spaces dictionary in andela_dojo,
        # store it in random_living_space variable
        living_space_list = [living_space for living_space in self.andela_dojo['living_spaces'].values() if
                             len(living_space.occupants) < 4]

        if len(living_space_list) > 0:
            random_living_space_index = random.randint(0, len(living_space_list) - 1)
            random_living_space = living_space_list[random_living_space_index]

        if len(living_space_list) == 0:
            random_living_space = None

        # If staff entry is valid, add person to Staff dictionary in the occupants attribute of the random_office
        if arg['<Fellow_or_Staff>'].lower() == 'staff' and str(arg['<wants_accommodation>']).lower() != 'y':

            if random_office is not None:
                random_office.occupants['Staff'][person_name.lower()] = Staff(person_name.lower())

                print('\n\tStaff {} has been added successfully!'.format(person_name))
                print('\t{} has been given office: {}'.format(person_name, random_office.name))

            if random_office is None:
                self.andela_dojo['unallocated']['Office'][person_name.lower()] = Staff(person_name.lower())
                print('\n\tStaff {} has unallocated Office Space'.format(person_name))

        # If fellow wants accommodation:
        if arg['<Fellow_or_Staff>'].lower() == 'fellow' and str(arg['<wants_accommodation>']).lower() == 'y':

            if random_living_space is not None:  # If living space is available

                # Add Fellow to Fellow dictionary in the occupants attribute of the random_random_living_space
                random_living_space.occupants[person_name.lower()] = Fellow(person_name.lower(), 'Y')

                print('\n\tFellow {} has been added successfully!'.format(person_name))
                print('\t{} has been given living space: {}'.format(person_name, random_living_space.name))

            if random_living_space is None:  # If living space is not available
                self.andela_dojo['unallocated']['Living_Space'][person_name.lower()] = Fellow(person_name.lower(), 'Y')
                print('\n\tFellow {} has unallocated Living Space'.format(person_name))

            if random_office is None:  # If office space is not available
                self.andela_dojo['unallocated']['Office'][person_name.lower()] = Fellow(person_name.lower(), 'Y')
                print('\n\tFellow {} has unallocated Office Space'.format(person_name))

            if random_office is not None:  # If office space is  available

                # Add Fellow to Fellow dictionary in the occupants attribute of the random_random_living_space
                random_office.occupants['Fellows'][person_name.lower()] = Fellow(person_name.lower(), 'Y')
                print('\n\t{} has been given office space: {}'.format(person_name, random_office.name))

        # If fellow does not want accommodation:
        if arg['<Fellow_or_Staff>'].lower() == 'fellow' and str(arg['<wants_accommodation>']).lower() != 'y':

            if random_office is not None:
                # Add Fellow to Fellow dictionary in the occupants attribute of the random_office
                random_office.occupants['Fellows'][person_name.lower()] = Fellow(person_name.lower(), 'N')

                print('\n\tFellow {} has been added successfully!'.format(person_name))
                print('\t{} has been given office: {}'.format(person_name, random_office.name))

            if random_office is None:
                self.andela_dojo['unallocated']['Office'][person_name.lower()] = Fellow(person_name.lower(), 'N')
                print('\n\tFellow {} has unallocated Office Space'.format(person_name))

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('\n\t\t****************Good Bye****************')
        exit()

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""

        try:  # When living space exists
            room_requested = self.andela_dojo['living_spaces'][arg['<room_name>'].lower()]

            print('Fellows in living space: {}'.format(arg['<room_name>'].capitalize()))
            print('----------------------------------------')

            if len(room_requested.occupants) > 0:  # If room has people in it
                for Fellows in room_requested.occupants.values():
                    print(Fellows.name.capitalize())
                print('\n')
            else:  # If room is empty
                print('None\n')

        except KeyError:  # When living space does not exist
            print("Living space with such name does not exist\n")

        try:  # When office does not exist
            room_requested = self.andela_dojo['office_spaces'][arg['<room_name>'].lower()]

            print('Staff in office space: {}'.format(arg['<room_name>'].capitalize()))
            print('----------------------------------------')
            if len(room_requested.occupants['Staff']) > 0:  # If room has staff
                for Staff in room_requested.occupants['Staff'].values():
                    print(Staff.name.capitalize())
                print('\n')

            else:  # If room has no staff
                print('None\n')

            print('Fellows in office space: {}'.format(arg['<room_name>'].capitalize()))

            if len(room_requested.occupants['Fellows']) > 0:
                for Fellows in room_requested.occupants['Fellows'].values():
                    print(Fellows.name.capitalize())
                print('\n')
            else:
                print('None\n')

        except KeyError:  # When office does not exist
            print("Office space with such name does not exist\n")

    # Prints room allocations to screen or file.
    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [<output>]"""

        living_spaces = self.andela_dojo['living_spaces']
        office_spaces = self.andela_dojo['office_spaces']

        try:  # When an output file is desired

            if arg['<output>'].lower() == 'y':

                output = open("E:\have_allocations.txt", "w+")
            else:

                output = None

        except (KeyError, AttributeError):
            output = None

        # Go through each living space in the andela dojo
        for living_space in living_spaces.values():
            print('Fellows in living space: {}'.format(living_space.name.capitalize()), file=output, flush=True)
            print('----------------------------------------', file=output, flush=True)

            # Print the name of each occupant if the room is not empty
            if len(living_space.occupants.values()) > 0:
                for Fellows in living_space.occupants.values():
                    print(Fellows.name.capitalize(), end=', ', file=output, flush=True)
                print('\n', file=output, flush=True)

            else:  # When room is empty
                print('None\n', file=output, flush=True)

        # Go through each office space in the andela dojo
        for office_space in office_spaces.values():

            print('\nOccupants of office space: {}'.format(office_space.name.capitalize()), file=output, flush=True)
            print('----------------------------------------', file=output, flush=True)

            if len(office_space.occupants['Fellows'].values()) > 0:
                for Fellows in office_space.occupants['Fellows'].values():
                    print(Fellows.name.capitalize(), end=', ', file=output, flush=True)
            else:
                print('No Fellows', file=output, flush=True)

            if len(office_space.occupants['Staff'].values()):
                for Staff in office_space.occupants['Staff'].values():
                    print(Staff.name.capitalize(), end=', ', file=output, flush=True)
                print('\n')
            else:
                print('No Staff\n', file=output, flush=True)

        if output is not None:  # Hahahahaha

            output.close()
        return None  # For testing purposes

    # Works the same as print_allocation, same comments apply.
    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [<output>] """

        unallocated_office_space = self.andela_dojo['unallocated']['Office']
        unallocated_living_space = self.andela_dojo['unallocated']['Living_Space']

        try:

            if arg['<output>'].lower() == 'y':

                output = open("have_no_allocations.txt", "w+")
            else:

                output = None
        except (KeyError, AttributeError):
            output = None

        print('\nPersons with unallocated living space:', file=output, flush=True)
        print('----------------------------------------', file=output, flush=True)

        if len(unallocated_living_space.values()) > 0:
            for Person in unallocated_living_space.values():
                print(Person.name.capitalize(), end=', ', file=output, flush=True)
            print('\n', file=output, flush=True)
        else:
            print('None\n', file=output, flush=True)

        print('\nPersons with unallocated office space:', file=output, flush=True)
        print('----------------------------------------', file=output, flush=True)

        if len(unallocated_office_space.values()) > 0:
            for Person in unallocated_office_space.values():
                print(Person.name.capitalize(), end=', ', file=output, flush=True)
            print('\n', file=output, flush=True)
        else:
            print('None\n', file=output, flush=True)

        return None

    # Loads interactive state from the database
    @docopt_cmd
    def do_load_state(self, arg):
        """Usage: load_state [<output>] """

        # Create an engine to link to the database
        engine = create_engine('sqlite:///interactive_status.db', echo=False)

        # Create a session
        Session = sessionmaker(bind=engine)

        session = Session()

        # Try/Except block to determine if session has been specified, defaults to 'default'.
        try:
            state = arg['<output>'].lower()

        except (KeyError, AttributeError):
            state = 'default'

        for back in session.query(State).filter(State.state_name == state):
            requested_state = pickle.loads(back.state_file)

        # Reload the interactive session with retrieved object as self.andela_dojo
        print('Exiting........')

        self.andela_dojo = requested_state

    # Save interactive state to database
    @docopt_cmd
    def do_save_state(self, arg):
        """Usage: load_state [<output>] """
        # Open a file to store the dojo object.
        with open("status.pickle", "wb") as status:
            pickle.dump(self.andela_dojo, status, protocol=pickle.HIGHEST_PROTOCOL)  # Write the current object to it.

        # Convert the file into a binary object.
        with open("status.pickle", 'rb') as status_file:
            status_bin = status_file.read()

        # Create engine to talk to database
        status_engine = create_engine('sqlite:///interactive_status.db', echo=False)
        Base = declarative_base()
        Base.metadata.create_all(status_engine)

        try:  # Try if session name is provided
            saved_state = State(state_name=arg['<output>'].lower(), state_file=status_bin)  # Create entry in table

        except (KeyError, AttributeError):
            saved_state = State(state_name='default', state_file=status_bin)  # Create entry in table

        # Create session to talk to database
        some_session = sessionmaker(bind=status_engine)
        session = some_session()

        session.add(saved_state)  # Add session
        session.commit()  # Commit session
        print('\n\tSave complete')

    @docopt_cmd
    def do_load_people(self, arg):
        """Usage: load_people"""

        # Open the file to be loaded using a 'with' statement to ensure file is automatically closed.
        with open("load_file.txt", 'r') as file:

            # Read the file line by line extracting out details of person to be added.
            for line in file:

                person_details = line.rstrip().split(' ')

                person_first_name = person_details[0]
                person_last_name = person_details[1]
                person_type = person_details[2]

                # Call the do_add_person method to add each person in the file.
                try:
                    person_accommodation = person_details[3]

                    self.do_add_person.__wrapped__(self, {'<first_name>': person_first_name,
                                                          '<last_name>': person_last_name,
                                                          '<Fellow_or_Staff>': person_type,
                                                          '<wants_accommodation>': person_accommodation})
                except IndexError:

                    self.do_add_person.__wrapped__(self, {'<first_name>': person_first_name,
                                                          '<last_name>': person_last_name,
                                                          '<Fellow_or_Staff>': person_type,
                                                          '<wants_accommodation>': None})

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person <person_identifier> <new_room_name>"""

        if arg['<new_room_name>'].lower() in self.andela_dojo['living_spaces']:

            for living_space in list(self.andela_dojo['living_spaces'].values()):

                person_name = arg['<person_identifier>'].lower().replace('-', ' ')

                if person_name in living_space.occupants:

                    new_room = self.andela_dojo['living_spaces'][arg['<new_room_name>'].lower()]

                    if len(new_room.occupants) < 5:
                        new_room.occupants[person_name] = living_space.occupants[person_name]

                    del living_space.occupants[person_name]

                    print('Fellow {} has been successfully reallocated from living space {} to living space {}'.format(
                        person_name.capitalize(), living_space.name, new_room.name))
                    break

        elif arg['<new_room_name>'].lower() in self.andela_dojo['office_spaces']:

            for office_space in list(self.andela_dojo['office_spaces'].values()):

                person_name = arg['<person_identifier>'].replace('-', ' ').lower()
                new_room = self.andela_dojo['office_spaces'][arg['<new_room_name>'].lower()]

                if person_name in office_space.occupants['Staff']:

                    if len(new_room.occupants) < 7:
                        new_room.occupants['Staff'][person_name] = office_space.occupants['Staff'][person_name]

                    del office_space.occupants['Staff'][person_name]

                    print('Staff {} has been successfully reallocated from office space: {} to office space: {}'.format(
                        person_name.capitalize(), office_space.name, new_room.name))
                    break

                elif person_name in office_space.occupants['Fellows']:

                    if len(new_room.occupants) < 7:
                        new_room.occupants['Fellows'][person_name] = office_space.occupants['Fellows'][person_name]

                    del office_space.occupants['Fellows'][person_name]

                    print(
                        'Fellow {} has been successfully reallocated from office space: {} to office space: {}'.format(
                            person_name.capitalize(), office_space.name, new_room.name))
                    break
        else:
            print('Invalid Room Name or Person ID.')
            print('Use print_allocations command for help')


if __name__ == '__main__':
    opt = docopt(__doc__, sys.argv[1:])
    InteractiveRoomAllocator(Dojo()).cmdloop()
