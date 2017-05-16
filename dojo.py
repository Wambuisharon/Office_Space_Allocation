import random
from room import Office, Living_space
from person import Fellow, Staff

class Dojo(object):
    def __init__(self):
        self.list_of_offices = []
        self.list_of_living_space = []
        self.list_of_fellows = []
        self.list_of_staff = []
        self.list_of_occupants = []

    def create_room(self,room_name,room_type):
        if room_type == "Office":
            new_office = Office(room_name)
            self.list_of_offices.append(new_office)
            print("The office %s has been created successfully" % new_office.room_name)

        elif room_type == "Living_space":
            new_living_space= Living_space(room_name)
            self.list_of_living_space.append(new_living_space)
            print("This living room %s has been created successfully" % new_living_space.room_name)    

    def add_person(self,person_name,person_type, accommodation="No"):
        if person_type == "Staff":
            new_staff = Staff(person_name)
            self.list_of_staff.append(new_staff)
            # get a random room 
            random_room = random.choice(self.list_of_offices)
            # add member to the occupants of the selected room
            random_room.occupants.append(new_staff)
            print("This staff %s has been added successfully" % new_staff.person_name)  

        elif person_type == "Fellow":
            new_fellow = Fellow(person_name)
            self.list_of_fellows.append(new_fellow) 
            print("This fellow %s has been added successfully" % new_fellow.person_name)
            random_room = random.choice(self.list_of_offices)
            random_room.occupants.append(new_fellow)
            #Add a living room to a fellow
            if accommodation == "yes":
                random_room = random.choice(self.list_of_living_space)
                random_room.occupants.append(new_fellow)


