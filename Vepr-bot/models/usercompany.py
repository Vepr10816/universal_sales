class Usercompany:

	def __init__(self):
		self.user = 0
		self.id = 0
		self.mycompany = 0

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
	def _mycompany(self):
		return self.mycompany

	@_mycompany.setter
	def _mycompany(self, value):
		self.mycompany = value


	def get(self):
		usercompanyDict = self.__dict__
		del usercompanyDict['id']
		usercompanyDict['idUser'] = usercompanyDict.pop('user')
		usercompanyDict['idMycompany'] = usercompanyDict.pop('mycompany')
		return usercompanyDict

	def set(self, user, id, mycompany):
		self.user = user
		self.id = id
		self.mycompany = mycompany
		return self