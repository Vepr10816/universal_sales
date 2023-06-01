class Datatype:

	def __init__(self):
		self.id = 0
		self.type_name = " "

	@property
	def _id(self):
		return self.id

	@_id.setter
	def _id(self, value):
		self.id = value



	@property
	def _type_name(self):
		return self.type_name

	@_type_name.setter
	def _type_name(self, value):
		self.type_name = value


	def get(self):
		datatypeDict = self.__dict__
		del datatypeDict['id']
		return datatypeDict

	def set(self, id, type_name):
		self.id = id
		self.type_name = type_name
		return self