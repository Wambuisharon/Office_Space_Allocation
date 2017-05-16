class Person(object):
	def __init__(self,person_name,person_type):
		self.person_name = person_name
		self.person_type = person_type

class Fellow(Person):
	def __init__(self,person_name,person_type = "fellow"):
		super(Fellow,self).__init__(person_name,person_type)

class Staff(Person):
	def __init__(self,staff_name,staff_type = "staff"):
		super(Staff, self).__init__(staff_name,staff_type)
				
new_fellow = Fellow("Sharon")
print(new_fellow.person_name)		
		