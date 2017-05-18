import random
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
            if room_type == "Office":
                new_office = Office(room_name)
                self.list_of_offices.append(new_office)
                print("Office %s has been created successfully" % room_name)
                return new_office

            elif room_type == "Living_space":
                new_living_space = Living_space(room_name)
                self.list_of_living_space.append(new_living_space)
                print("Livingspace %s has been created successfully"
                      % room_name)
                return new_living_space

        elif room_name in all_room_names:
            return "Sorry. Room %s already exists" % room_name

    def add_person(self, person_name, person_type, accommodation="No"):
        if person_type == "Staff":
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
                print("Staff %s has been added into %s "
                      % (new_staff.person_name, random_room.room_name))
            else:
                print("No offices available, You'll be \
                       added to a waiting list")

            return new_staff

        elif person_type == "Fellow":
            new_fellow = Fellow(person_name)
            self.list_of_fellows.append(new_fellow)
            print("Fellow %s has been succefully added." % person_name)
            available_offices = [office for office in self.list_of_offices
                                 if len(office.occupants) < 6]
            if available_offices:
                random_room = random.choice(available_offices)
                random_room.occupants.append(new_fellow)
                print ("Fellow %s has been allocated  office %s "
                       % (new_fellow.person_name, random_room.room_name))
            else:
                return "No offices available, You'll be\
                 added to a waiting list"
            # Add a living room to a fellow
            if accommodation == "yes":
                available_living_spaces = [living_space for living_space in
                                           self.list_of_living_space if
                                           len(living_space.occupants) < 4]
                if available_living_spaces:
                    random_room = random.choice(available_living_spaces)
                    random_room.occupants.append(new_fellow)
                    print ("Fellow %s has been allocated %s"
                           % (new_fellow.person_name, random_room.room_name))
                else:
                    return "No living space available, You'll be\
                     added to a waiting list"

            return new_fellow

        else:

            return "We ran into an error"
