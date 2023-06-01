class Roleuser:

	def __init__(self):
		self.user = 0
		self.id = 0
		self.roles = 0

	@property
	def _user(self):
		return self.user

	@_user.setter
	def _user(self, value):
		self.user = value



	@property
	def _id(self):
		return self.id

	@_id.setter
	def _id(self, value):
		self.id = value



	@property
	def _roles(self):
		return self.roles

	@_roles.setter
	def _roles(self, value):
		self.roles = value


	def get(self):
		roleuserDict = self.__dict__
		del roleuserDict['id']
		roleuserDict['idUser'] = roleuserDict.pop('user')
		roleuserDict['idRoles'] = roleuserDict.pop('roles')
		return roleuserDict

	def set(self, user, id, roles):
		self.user = user
		self.id = id
		self.roles = roles
		return self