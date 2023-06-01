class Selectedproductcharacteristics:

	def __init__(self):
		self.id = 0
		self.productcharacteristics = 0
		self.selectedproduct = 0

	@property
	def _id(self):
		return self.id

	@_id.setter
	def _id(self, value):
		self.id = value



	@property
	def _productcharacteristics(self):
		return self.productcharacteristics

	@_productcharacteristics.setter
	def _productcharacteristics(self, value):
		self.productcharacteristics = value



	@property
	def _selectedproduct(self):
		return self.selectedproduct

	@_selectedproduct.setter
	def _selectedproduct(self, value):
		self.selectedproduct = value


	def get(self):
		selectedproductcharacteristicsDict = self.__dict__
		del selectedproductcharacteristicsDict['id']
		selectedproductcharacteristicsDict['idProductcharacteristics'] = selectedproductcharacteristicsDict.pop('productcharacteristics')
		selectedproductcharacteristicsDict['idSelectedproduct'] = selectedproductcharacteristicsDict.pop('selectedproduct')
		return selectedproductcharacteristicsDict

	def set(self, id, productcharacteristics, selectedproduct):
		self.id = id
		self.productcharacteristics = productcharacteristics
		self.selectedproduct = selectedproduct
		return self