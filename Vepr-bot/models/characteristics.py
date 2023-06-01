class Characteristics:

	def __init__(self):
		self.datatype = 0
		self.id = 0
		self.characteristic_name = " "
		self.subcategory = 0
		self.preValuesList = []
		self.selectable = False

	@property
	def _selectable(self):
		return self.selectable

	@_selectable.setter
	def _selectable(self, value):
		self.selectable = value

	@property
	def _datatype(self):
		return self.datatype

	@_datatype.setter
	def _datatype(self, value):
		self.datatype = value



	@property
	def _id(self):
		return self.id

	@_id.setter
	def _id(self, value):
		self.id = value



	@property
	def _characteristic_name(self):
		return self.characteristic_name

	@_characteristic_name.setter
	def _characteristic_name(self, value):
		self.characteristic_name = value



	@property
	def _subcategory(self):
		return self.subcategory

	@_subcategory.setter
	def _subcategory(self, value):
		self.subcategory = value


	def get(self):
		characteristicsDict = self.__dict__
		del characteristicsDict['id']
		characteristicsDict['idDatatype'] = characteristicsDict.pop('datatype')
		characteristicsDict['idSubcategory'] = characteristicsDict.pop('subcategory')
		return characteristicsDict

	def set(self, datatype, characteristic_name, id, subcategory, selectable, preValuesList=None,):
		self.datatype = datatype
		self.characteristic_name = characteristic_name
		self.id = id
		self.subcategory = subcategory
		self.preValuesList = preValuesList
		self.selectable = selectable
		return self