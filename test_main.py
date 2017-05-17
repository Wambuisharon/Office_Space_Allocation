import unittest

from dojo import Dojo
from room import Office, Living_space
from person import Fellow, Staff

class TestCreateRoom(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()
        self.dojo.create_room("Spire", "Office")
        self.dojo.create_room("Tent", "Living_space")
        

    #Create office test
    def test_create_office_successfully(self):
        initial_room_count = len(self.dojo.list_of_offices)
        self.dojo.create_room("Lion", "Office")
        new_room_count = len(self.dojo.list_of_offices)
        self.assertGreater(new_room_count,initial_room_count)

    def test_create_living_space_successfully(self):
        initial_room_count = len(self.dojo.list_of_living_space)
        self.dojo.create_room("Mt_Kenya", "Living_room")
        new_room_count = len(self.dojo.list_of_living_space)
        self.assertGreater(new_room_count,initial_room_count)

    def test_add_fellow(self):
        initial_fellow_count = len(self.dojo.list_of_fellows)
        self.dojo.add_person("Washera", "Fellow")
        new_fellow_count= len(self.dojo.list_of_fellows)
        self.assertGreater(new_fellow_count,initial_fellow_count)
    def test_add_staff(self):
        initial_staff_count = len(self.dojo.list_of_staff)
        self.dojo.add_person("Claudine", "Staff")
        new_staff_count = len(self.dojo.list_of_staff) 
        self.assertGreater(new_staff_count,initial_staff_count)   

    def test_office_with_similar_names(self):
        initial_office_count = len(self.dojo.list_of_offices)
        self.dojo.create_room("Office", "test_office")
        new_office_count= len(self.dojo.list_of_offices)
        self.assertEquals(new_office_count, initial_office_count)

    #Create living room test
    def test_create_living_space_successfully(self):
        initial_living_space_count = len(self.dojo.list_of_living_space)
        self.dojo.create_room("Kenya","Living_space")
        new_living_space_count = len(self.dojo.list_of_living_space)
        self.assertGreater(new_living_space_count,initial_living_space_count)

    def test_living_room_with_similar_names(self):
        initial_living_space_count= len(self.dojo.list_of_living_space)
        self.dojo.create_room("Living_space","test_living_space")
        new_living_space_count = len(self.dojo.list_of_living_space)
        self.assertEquals(new_living_space_count, initial_living_space_count)


    def test_office_allocation(self):
        test_fellow = self.dojo.add_person("John Doe", "Fellow")
        self.assertIn(test_fellow, self.dojo.list_of_offices[0].occupants)
        

    def test_living_space_allocation(self):
        test_fellow = self.dojo.add_person("John Doe1", "Fellow", accommodation="yes")
        self.assertIn(test_fellow, self.dojo.list_of_living_space[0].occupants)

    def test_create_living_space_with_an_exist_office_name(self):
        self.dojo.create_room("Tsavo", "Living_space")
        new_tsavo = self.dojo.create_room("Tsavo", "Living_space")
        self.assertEquals("Sorry. Room Tsavo already exists", new_tsavo)




if __name__ == '__main__':
	unittest.main()