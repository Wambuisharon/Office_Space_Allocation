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
        test_create_office = self.dojo.create_room("Lion", "Office")
        self.assertIn(test_create_office,self.dojo.list_of_offices)

    def test_office_allocation(self):
        test_office_allocation = self.dojo.add_person("John Doe", "Fellow")
        self.assertIn(test_office_allocation, self.dojo.list_of_offices[0].occupants)
        
    def test_create_living_space_successfully(self):
        test_create_living_space = self.dojo.create_room("Mt_Kenya", "Living_space")
        self.assertIn(test_create_living_space,self.dojo.list_of_living_space)
        
    def test_add_fellow(self):
        test_add_fellow = self.dojo.add_person("Washera", "Fellow")
        self.assertIn(test_add_fellow,self.dojo.list_of_fellows)
       
    def test_add_staff(self):
        test_add_staff = self.dojo.add_person("Office", "Staff")
        self.assertIn(test_add_staff,self.dojo.list_of_staff)

    def test_office_with_similar_names(self):
        test_office_with_similar_names = self.dojo.create_room("Spire", "Office")
        self.assertIn(test_office_with_similar_names, "Sorry. Room Spire already exists")
        
    #Create living room test
    
    def test_living_room_with_similar_names(self):
        test_living_room_with_similar_names = self.dojo.create_room("Tent", "Living_space")
        self.assertIn(test_living_room_with_similar_names,"Sorry. Room Tent already exists" )

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