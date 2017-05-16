class Room(object):
	def __init__(self,room_name,room_type,space):
		self.room_name = room_name
		self.room_type = room_type
		self.space = space

class Office(Room):
	def __init__(self,room_name,room_type = "office"):
		super(Office,self).__init__(room_name,room_type)

class Living_space(Room):
	def __init__(self,room_name,room_type= "Living_space"):
		super(Living_space, self).__init__(room_name,room_type)
				
new_living_space = Living_space("mt_kenya")
print(new_living_space.room_name)	