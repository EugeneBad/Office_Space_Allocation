"""

Usage:
    Room_Allocator:
    Room_Allocator: (-h | --help | --version)

"""

import cmd
from docopt import docopt, DocoptExit
import sys


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

andela_dojo = Dojo()

class InteractiveRoomAllocator(cmd.Cmd):
    intro = "Eugene's random room allocator for Andela"
    prompt = "Room_Allocator: "
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>"""

        if arg['<room_type>'] == 'office':
            andela_dojo[arg['<room_name>']] = Office(arg['<room_name>'])

        if arg['<room_type>'] == 'living':
            andela_dojo[arg['<room_name>']] = Room('living', arg['<room_name>'])

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage:
        add_person <person_name> <FELLOW|STAFF> [wants_accommodation=Y/N]
        Options:
        wants_accommodation=Y/N  Yes(Y) if Fellow opts for accommodation, No(N) otherwise. [default: N]"""

        if arg['<FELLOW|STAFF>'] == 'Staff' and arg['wants_accommodation'] == 'Y':
            print('Staff cannot be allocated living spaces')


        pass


opt = docopt(__doc__, sys.argv[1:])
InteractiveRoomAllocator().cmdloop()
