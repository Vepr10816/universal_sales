class Addresses:

	def __init__(self):
		self.id = 0
		self.address_name = " "
		self.mycompany = 0

	@property
	def _id(self):
		return self.id

	@_id.setter
	def _id(self, value):
		self.id = value



	@property
	def _address_name(self):
		return self.address_name

	@_address_name.setter
	def _address_name(self, value):
		self.address_name = value



	@property
	def _mycompany(self):
		return self.mycompany

	@_mycompany.setter
	def _mycompany(self, value):
		self.mycompany = value


	def get(self):
		addressesDict = self.__dict__
		del addressesDict['id']
		addressesDict['idMycompany'] = addressesDict.pop('mycompany')
		return addressesDict

	def set(self, id, address_name, mycompany):
		self.id = id
		self.address_name = address_name
		self.mycompany = mycompany
		return self