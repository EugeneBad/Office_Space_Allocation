=====================
Features and Commands
=====================

Room_Allocator is designed as an easy to use program with multiple features accessible via a simple command line interface.
The functionality of each feature is initiated by typing out a command with it's necessary arguments; and the rest is handled
internally.

Creating Rooms
##############

This is perhaps the first feature one would use!
It is implemented using the **create_room** command. Usage information is available by typing:
::

    help create_room

as shown below:

.. image:: images/create_help.png
    :width: 500px
    :align: center
    :height: 130px
    :alt: alternate text

The *room_type* argument can either be 'living' for living spaces or 'office' for an office space.

The *room_name* is as it says is the room's name!

.. note::  The inputs are case insensitive..

Hitting enter will create the desired room as shown below:

.. image:: images/create_room.png
    :width: 500px
    :align: center
    :height: 130px
    :alt: alternate text

.. warning::  The program rejects duplicate room names of the same type..

Other features include:
    * Persons with unallocated office space can be reallocated when new office is created.
    * Fellows with unallocated living space can be reallocated when new living space is created.

Adding Persons
##############

This feature allows the user to add persons fellows or staff to the system.
It is implemented using the **add_person** command. Usage information is available by typing:
::

    help add_person

as shown below:

.. image:: images/add_help.png
    :width: 500px
    :align: center
    :height: 130px
    :alt: alternate text

The *first_name* and *last_name* arguments are the person's first and last names respectively.

The *Fellow_or_Staff* argument defines wehther the person being added is a fellow or staff.
This determines whether or not the person can be assigned a living space.

The *wants_accommodation* argument is for fellows to choose whether they want a living space or not. The default is 'no'.

.. note::  The inputs are also case insensitive..

If the usage is adhered to, hitting enter will add the person as shown below:

.. image:: images/add_person.png
    :width: 500px
    :align: center
    :height: 130px
    :alt: alternate text

Other features include:
    * People with the same names can not conflict.
    * Fellow will be unallocated if he wants a living room and non is available.
    * Fellow or Staff will be unallocated if an office is unavailable.

Printing Room Occupants
#######################

This feature is implemented using the **print_room** command. Usage information is available by typing:
::

    help print_room

as shown below:

.. image:: images/print_room_help.png
    :width: 500px
    :align: center
    :height: 130px
    :alt: alternate text

The *room_name* argument corresponds to the room whose occupants are to be printed.

.. note::  The input is case insensitive..

Hitting enter will print the desired room's occupants as shown below:

.. image:: images/print_room.png
    :width: 500px
    :align: center
    :height: 130px
    :alt: alternate text


Printing Room Allocations
#########################

This feature is implemented using the **print_allocations** command. Usage information is available by typing:
::

    help print_allocations

as shown below:

.. image:: images/print_allocations_help.png
    :width: 500px
    :align: center
    :height: 130px
    :alt: alternate text

The *output* argument corresponds to the name of the .txt file to which the room allocations can be printed if the
user desires.

Hitting enter will print the allocations for all the rooms in the system as shown below:

.. image:: images/print_allocations.png
    :width: 500px
    :align: center
    :height: 130px
    :alt: alternate text


Printing UnAllocated
####################

When either a living space or office is unavailable, persons who are added remain unassigned rooms and thus this feature allows
the user to view the persons who are unallocated living spaces (for fellows) and office spaces (both staff and fellows).
This feature is accessed by using the **print_unallocated** command. Usage information can be obtain via:
::

    help print_unallocated

as shown below:

.. image:: images/print_unallocated_help.png
    :width: 500px
    :align: center
    :height: 130px
    :alt: alternate text

The *output* argument corresponds to the name of the .txt file to which the information can be printed if the
user desires.

Hitting enter will print all unallocated persons in the system as shown below:

.. image:: images/print_unallocated.png
    :width: 500px
    :align: center
    :height: 130px
    :alt: alternate text


Reallocating Person
###################

This feature allows a user to reallocate a person from one room to another using the person's id. This is achieved using
the **reallocate_person** command. Usage information can be obtain via:
::

    help reallocate_person

as shown below:

.. image:: images/reallocate_person_help.png
    :width: 500px
    :align: center
    :height: 130px
    :alt: alternate text

The *person_identifier* argument corresponds to the person who is to be relocated.

The *new_room_name* argument corresponds to the room to which he is to be relocated

.. warning::  A person can only be moved from one office to another or from one living space to another! Only if it has space..

.. warning:: Staff cannot be relocated to living spaces..

Hitting enter will relocate the person to the desired room as shown below:

.. image:: images/reallocate_person.png
    :width: 1050px
    :align: center
    :height: 170px
    :alt: alternate text


Loading People
##############

This feature allows a user to load a text file and add all the people in it at once. This is achieved using
the **load_people** command. Usage information can be obtain via:
::

    help load_people

as shown below:

.. image:: images/load_people_help.png
    :width: 500px
    :align: center
    :height: 130px
    :alt: alternate text

The *load_file* argument specifies the name of the file from which to load people.

Sample file:

.. image:: images/sample_file.png
    :width: 450px
    :align: center
    :height: 170px
    :alt: alternate text

Hitting enter will add all the persons as shown:

.. image:: images/load_people.png
    :width: 850px
    :align: center
    :height: 200px
    :alt: alternate text


Saving an Interactive Session
#############################

This feature allows a user save their current interaction with the program to be retrieved at a later time. This is achieved using
the **save_state** command. Usage information can be obtain via:
::

    help save_state

as shown below:

.. image:: images/save_state_help.png
    :width: 450px
    :align: center
    :height: 170px
    :alt: alternate text

The *output* argument specifies the name of the current session.

.. warning:: Specifying an existent name will cause that session to be overwritten..

Loading an Interactive Session
##############################

This feature allows a user to reload their previously saved interaction with the program.
This is achieved using the **load_state_state** command. Usage information can be obtain via:
::

    help save_state

as shown below:

.. image:: images/load_state_help.png
    :width: 450px
    :align: center
    :height: 170px
    :alt: alternate text

The *output* argument specifies the name of the session to be retrieved.

