import unittest

from dojo import Dojo


class TestCreateRoom(unittest.TestCase):

    def setUp(self):
        self.dojo = Dojo()
        self.dojo.create_room("Spire", "OFFICE")
        self.dojo.create_room("Tent", "LIVING_SPACE")

    # Create office test
    def test_create_office_successfully(self):
        test_create_office = self.dojo.create_room("LION", "OFFICE")
        self.assertIn(test_create_office, self.dojo.list_of_offices)

    def test_office_allocation(self):
        test_office_allocation = self.dojo.add_person("John Doe", "FELLOW")
        all_occupants = []
        for room in self.dojo.list_of_offices:
            for person in room.occupants:
                all_occupants.append(person)
        self.assertIn(test_office_allocation,
                      all_occupants)

    def test_create_living_space_successfully(self):
        test_create_living_space = \
            self.dojo.create_room("Mt_Kenya", "LIVING_SPACE")
        self.assertIn(test_create_living_space, self.dojo.list_of_living_space)

    def test_add_fellow(self):
        test_add_fellow = self.dojo.add_person("Washera", "FELLOW")
        self.assertIn(test_add_fellow, self.dojo.list_of_fellows)

    def test_add_staff(self):
        test_add_staff = self.dojo.add_person("Dudhd", "STAFF")
        self.assertIn(test_add_staff, self.dojo.list_of_staff)

    def test_office_with_similar_names(self):
        test_office_with_similar_names = self.dojo.create_room("Spire",
                                                               "OFFICE")
        self.assertEquals(test_office_with_similar_names,
                          "Sorry. Room Spire already exists")

    def test_living_room_with_similar_names(self):
        test_living_room_with_similar_names = \
            self.dojo.create_room("Tent", "LIVING_SPACE")
        self.assertEquals(test_living_room_with_similar_names,
                          "Sorry. Room Tent already exists")

    def test_living_space_allocation(self):
        test_living_space_allocation = \
            self.dojo.add_person("John Doe1", "FELLOW", accommodation="YES")
        all_occupants = []
        for room in self.dojo.list_of_living_space:
            for person in room.occupants:
                all_occupants.append(person)
        self.assertIn(test_living_space_allocation,
                      "Fellow John Doe1 has been allocated Tent")

    def test_create_living_space_with_an_exist_office_name(self):
        self.dojo.create_room("Tsavo", "OFFICE")
        new_tsavo = self.dojo.create_room("Tsavo", "LIVING_SPACE")
        self.assertEquals("Sorry. Room Tsavo already exists", new_tsavo)


if __name__ == '__main_':
    unittest.main()
