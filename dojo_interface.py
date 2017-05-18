#!/usr/bin/env python
'''

Usage:
    the-dojo create_room <room_type> <room_name>...
    the-dojo add_person <person_name> <person_type> <accommodation>
    the-dojo (-i | --interactive)

Options:
    -i, --interactive  :  Interactive Mode

'''
import sys
import cmd
from docopt import docopt, DocoptExit
from dojo import Dojo

dojo = Dojo()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class dojo_cmd(cmd.Cmd):

    intro = "Dojo"
    prompt = "the_dojo>> "
    file = None
    print(__doc__)

    @docopt_cmd
    def do_create_room(self, arg):
        '''
        Usage: create_room <room_type> <room_name>...
        '''
        for name in arg["<room_name>"]:
            room_name = name
            room_type = arg["<room_type>"]
            dojo.create_room(room_name, room_type)

    @docopt_cmd
    def do_add_person(self, arg):
        '''
        Usage: add_person <person_name> <person_type> [<accommodation>]
        '''
        if arg["<accommodation>"] == "Y" and arg["<person_type>"] == "Fellow":
            person_name = arg["<person_name>"]
            person_type = arg["<person_type>"]
            dojo.add_person(person_name, person_type, accommodation="yes")
        else:
            person_name = arg["<person_name>"]
            person_type = arg["<person_type>"]
            dojo.add_person(person_name, person_type)

    def do_quit(self, args):
        print("Bye!")
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    dojo_cmd().cmdloop()

print(opt)
