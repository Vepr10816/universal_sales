class Prevalues:

	def __init__(self):
		self.characteristics = 0
		self.pre_value = " "
		self.id = 0



	@property
	def _characteristics(self):
		return self.characteristics

	@_characteristics.setter
	def _characteristics(self, value):
		self.characteristics = value



	@property
	def _pre_value(self):
		return self.pre_value

	@_pre_value.setter
	def _pre_value(self, value):
		self.pre_value = value



	@property
	def _id(self):
		return self.id

	@_id.setter
	def _id(self, value):
		self.id = value


	def get(self):
		prevaluesDict = self.__dict__
		del prevaluesDict['id']
		prevaluesDict['idCharacteristics'] = prevaluesDict.pop('characteristics')
		return prevaluesDict

	def set(self, characteristics, pre_value, id):
		self.characteristics = characteristics
		self.pre_value = pre_value
		self.id = id
		return self