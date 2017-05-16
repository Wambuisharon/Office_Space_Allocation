
class Room(object):
	def __init__(self,room_name,room_type, space):
		self.room_name = room_name
		self.room_type = room_type
		self.space = space
		self.occupants = []

class Office(Room):
	def __init__(self,room_name,room_type = "office",space = 6, occupants=[]):
		super(Office,self).__init__(room_name,room_type, space=6)

class Living_space(Room):
	def __init__(self,room_name,room_type= "Living_space",space = 4):
		super(Living_space, self).__init__(room_name,room_type, space=4)
				
