class Requisites:

	def __init__(self):
		self.requisites_name = " "
		self.id = 0
		self.requisites_value = " "
		self.mycompany = 0

	@property
	def _requisites_name(self):
		return self.requisites_name

	@_requisites_name.setter
	def _requisites_name(self, value):
		self.requisites_name = value



	@property
	def _id(self):
		return self.id

	@_id.setter
	def _id(self, value):
		self.id = value



	@property
	def _requisites_value(self):
		return self.requisites_value

	@_requisites_value.setter
	def _requisites_value(self, value):
		self.requisites_value = value



	@property
	def _mycompany(self):
		return self.mycompany

	@_mycompany.setter
	def _mycompany(self, value):
		self.mycompany = value


	def get(self):
		requisitesDict = self.__dict__
		del requisitesDict['id']
		requisitesDict['idMycompany'] = requisitesDict.pop('mycompany')
		return requisitesDict

	def set(self, requisites_name, id, requisites_value, mycompany):
		self.requisites_name = requisites_name
		self.id = id
		self.requisites_value = requisites_value
		self.mycompany = mycompany
		return self