#!/usr/bin/env python
'''

Usage:
    the-dojo create_room <room_type> <room_name>...
    the-dojo add_person <first_name> <second_name> <person_type> [--a='No']
    the-dojo (-i | --interactive)

Options:
    -i, --interactive  :  Interactive Mode

'''
import sys
import cmd
from docopt import docopt, DocoptExit
from pyfiglet import Figlet, figlet_format
from termcolor import colored, cprint

from dojo import Dojo


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


border = colored("*" * 20, 'cyan').center(80)


def introduction():
    print(border)
    cprint(figlet_format('Dojo', font='basic'),
           'blue', attrs=['bold'])
    print(__doc__)
    print(border)


class dojo_cmd(cmd.Cmd):

    dojo = Dojo()
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
            room_type = arg["<room_type>"].upper()
            self.dojo.create_room(room_name, room_type)

    @docopt_cmd
    def do_add_person(self, args):
        '''
        Usage: add_person <first_name> <second_name> <person_type> [--a='No']
        '''
        first_name = args["<first_name>"]
        second_name = args["<second_name>"]
        person_name = first_name + ' ' + second_name
        person_type = args["<person_type>"].upper()
        if args['--a']:
            accomodation = args['--a'].upper()

        else:
            accomodation = 'NO'
        self.dojo.add_person(person_name, person_type, accomodation)

    def do_quit(self, args):
        print("Bye!")
        exit()


if __name__ == '__main__':
    introduction()
    try:
        dojo_cmd().cmdloop()
    except:
        cprint('\t\t Exitting Dojo...', 'magenta')
        exit()
