class Roles:

	def __init__(self):
		self.id = 0
		self.role_name = " "

	@property
	def _id(self):
		return self.id

	@_id.setter
	def _id(self, value):
		self.id = value



	@property
	def _role_name(self):
		return self.role_name

	@_role_name.setter
	def _role_name(self, value):
		self.role_name = value


	def get(self):
		rolesDict = self.__dict__
		del rolesDict['id']
		return rolesDict

	def set(self, id, role_name):
		self.id = id
		self.role_name = role_name
		return self