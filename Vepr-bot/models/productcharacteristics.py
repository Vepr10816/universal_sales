class Productcharacteristics:

	def __init__(self):
		self.product = 0
		self.characteristc_value = " "
		self.id = 0
		self.characteristics = 0

	@property
	def _product(self):
		return self.product

	@_product.setter
	def _product(self, value):
		self.product = value



	@property
	def _characteristc_value(self):
		return self.characteristc_value

	@_characteristc_value.setter
	def _characteristc_value(self, value):
		self.characteristc_value = value



	@property
	def _id(self):
		return self.id

	@_id.setter
	def _id(self, value):
		self.id = value



	@property
	def _characteristics(self):
		return self.characteristics

	@_characteristics.setter
	def _characteristics(self, value):
		self.characteristics = value


	def get(self):
		productcharacteristicsDict = self.__dict__
		del productcharacteristicsDict['id']
		productcharacteristicsDict['idProduct'] = productcharacteristicsDict.pop('product')
		productcharacteristicsDict['idCharacteristics'] = productcharacteristicsDict.pop('characteristics')
		return productcharacteristicsDict

	def set(self, product, characteristc_value, id, characteristics):
		self.product = product
		self.characteristc_value = characteristc_value
		self.id = id
		self.characteristics = characteristics
		return self