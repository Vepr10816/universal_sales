class Characteristicsprevalues:

	def __init__(self):
		self.characteristic_value = " "
		self.prevalues = 0
		self.characteristics = 0
		self.id = 0

	@property
	def _characteristic_value(self):
		return self.characteristic_value

	@_characteristic_value.setter
	def _characteristic_value(self, value):
		self.characteristic_value = value



	@property
	def _prevalues(self):
		return self.prevalues

	@_prevalues.setter
	def _prevalues(self, value):
		self.prevalues = value



	@property
	def _characteristics(self):
		return self.characteristics

	@_characteristics.setter
	def _characteristics(self, value):
		self.characteristics = value



	@property
	def _id(self):
		return self.id

	@_id.setter
	def _id(self, value):
		self.id = value


	def get(self):
		characteristicsprevaluesDict = self.__dict__
		del characteristicsprevaluesDict['id']
		characteristicsprevaluesDict['idPrevalues'] = characteristicsprevaluesDict.pop('prevalues')
		characteristicsprevaluesDict['idCharacteristics'] = characteristicsprevaluesDict.pop('characteristics')
		return characteristicsprevaluesDict

	def set(self, characteristic_value, prevalues, characteristics, id):
		self.characteristic_value = characteristic_value
		self.prevalues = prevalues
		self.characteristics = characteristics
		self.id = id
		return self