import random
from termcolor import cprint

from room import Office, Living_space
from person import Fellow, Staff


class Dojo(object):
    # Constructor
    def __init__(self):
        self.list_of_offices = []
        self.list_of_living_space = []
        self.list_of_fellows = []
        self.list_of_staff = []
        self.list_of_occupants = []

    def create_room(self, room_name, room_type):
        all_rooms = self.list_of_living_space + self.list_of_offices
        all_room_names = []
        for room in all_rooms:
            all_room_names.append(room.room_name)

        if room_name not in all_room_names:
            # create the room
            if room_type == "OFFICE":
                new_office = Office(room_name)
                self.list_of_offices.append(new_office)
                cprint("Office %s has been created successfully" % room_name,
                       "blue")
                return new_office

            elif room_type == "LIVING_SPACE":
                new_living_space = Living_space(room_name)
                self.list_of_living_space.append(new_living_space)
                cprint("Livingspace %s has been created successfully"
                       % room_name, "blue")
                return new_living_space
            else:
                cprint("Invalid room type", "red")
        else:
                cprint("Sorry. Room name %s already exists" % room_name, "red")
                return "Sorry. Room name %s already exists" % room_name

    def add_person(self, person_name, person_type, accommodation="NO"):
        all_people = self.list_of_fellows + self.list_of_staff
        all_people_names = []
        for people in all_people:
            all_people_names.append(people.person_name)

        if person_name not in all_people_names:

            if person_type == "STAFF":
                new_staff = Staff(person_name)
                self.list_of_staff.append(new_staff)
                # get a random room
                print("Staff %s has been added successfully" % person_name)
                available_offices = [office for office in
                                     self.list_of_offices if
                                     len(office.occupants) < office.space]
                if available_offices:
                    random_room = random.choice(available_offices)
            # add member to the occupants of the selected room
                    random_room.occupants.append(new_staff)
                    cprint("Staff %s has been added into %s"
                           % (new_staff.person_name, random_room.room_name)
                           , "red")
                else:
                    cprint("No offices available, You'll be \
                       added to a waiting list", "red")

                return new_staff

            elif person_type == "FELLOW":
                new_fellow = Fellow(person_name)
                self.list_of_fellows.append(new_fellow)
                cprint("Fellow %s has been succefully added." % person_name,
                       "blue")
                available_offices = [office for office in self.list_of_offices
                                     if len(office.occupants) < 6]
                if available_offices:
                    random_room = random.choice(available_offices)
                    random_room.occupants.append(new_fellow)
                    cprint("Fellow %s has been allocated  office %s "
                           % (new_fellow.person_name, random_room.room_name),
                           "blue")
                else:
                    cprint("No offices available, You'll be\
                       added to a waiting list", "blue")
                    return "No offices available, You'll be\
                       added to a waiting list"
            # Add a living room to a fellow
                if accommodation == "YES":
                    available_living_spaces = [living_space for living_space in
                                               self.list_of_living_space if
                                               len(living_space.occupants) < 4]
                    if available_living_spaces:
                        random_room = random.choice(available_living_spaces)
                        random_room.occupants.append(new_fellow)
                        cprint("Fellow %s has been allocated %s"
                               % (new_fellow.person_name,
                                  random_room.room_name), "blue")
                        return ("Fellow %s has been allocated %s"
                                % (new_fellow.person_name,
                                   random_room.room_name), "blue")
                    else:
                        cprint("No living space available, You'll be\
                     added to a waiting list", "blue")
                        return "No living space available, You'll be\
                     added to a waiting list"

                return new_fellow
            else:
                cprint("Person must be staff or fellow", "red")

        elif person_name in all_people_names:
                cprint("Sorry. Fellow %s already exists" % person_name, "red")
                return "Sorry. Fellow %s already exists" % person_name
