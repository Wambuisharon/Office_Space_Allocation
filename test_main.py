import unittest
from main import Dojo


class TestCreateRoom(unittest.TestCase):

    #Create office test
    def test_create_office_successfully(self):
        my_class_instance = Dojo()
        initial_room_count = len(my_class_instance.list_of_offices)
        lion_office = my_class_instance.create_office("lion", "office")
        self.assertTrue(lion_office)
        new_room_count = len(my_class_instance.office)
        self.assertEqual(new_office_count - initial_office_count, 1)

    def test_office_with_similar_names(self):
        initial_room_count = len(self.dojo.list_of_offices)
        self.dojo.create_office("OFFICE", "test_office")
        new_room_count = len(self.dojo.list_of_offices)
        self.assertEquals(new_office_count, initial_office_count)

    #Create living room test
    def test_create_living_space_successfully(self):
        my_class_instance= Dojo()
        initial_livingspace_count = len(my_class_instance.list_of_living_space)
        Mt_Kenya = my_class_instance.create_living_Space("Mt_Kenya","living_Space")
        self.assertTrue(Mt_Kenya)
        new_room_count = Len(my_class_instance.living_Space)
        self.assertEqual(new_living_space_count - initial_living_space_count, 1)

    def test_living_room_with_similar_names(self):
        my_class_instance = len(self.dojo.list_of_living_space)
        self.dojo.create_living_Space("LIVING-SPACE","test_living_space")
        new_room_count = len(self.Dojo.list_of_living_space)
        self.assertEquals(new_living_space_count, initial_living_space_count)

    #Create staff test 
    def test_add_staff(self):
        my_class_instance = Dojo()
        initial_staff_count = len(my_class_instance.list_of_staff)
        Kariuki = my_class_instance.add_staff("Kariuki","Staff")
        self.assertTrue(Kariuki)
        add_staff_count = len(my_class_instance.add_staff)
        self.assertEquals(new_staff_count - initial_staff_count, 1)

    def test_staff_with_similar_names(self):
        my_class_instance = len(self.dojo.list_of_staff)
        self.dojo.add_staff("Mukami","Staff")
        new_Staff = len(self.Dojo.list_of_staff)
        self.assertEquals(new_staff_count,initial_staff_count)
    def test_cannt_be_staff_and_fellow_cocurrently(self):
        pass 

    #Create fellow test
    def test_add_fellow(self):
        my_class_instance = Dojo()
        initial_fellow_count = len(my_class_instance.list_of_staff)
        Moses = my_class_instance.add_fellow("Moses","fellow")
        self.assertTrue(Kariuki)
        add_staff_count = len(my_class_instance.add_staff)
        self.assertEquals(new_fellow_count - initial_fellow_count, 1)

    def test_fellow_with_similar_names(self):
        my_class_instance = len(self.dojo.list_of_fellow)
        self.dojo.add_fellow("Jacob","Fellow")
        new_fellow = len(self.Dojo.list_of_fellow)
        self.assertEquals(new_fellow,initial_fellow_count)
    def test_cannt_be_fellow_and_staff_cocurrently(self):
           pass

if __name__ == '__main__':
	unittest.main()