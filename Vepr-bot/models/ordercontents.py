class Ordercontents:

	def __init__(self):
		self.order = 0
		self.selectedproduct = 0
		self.id = 0

	@property
	def _order(self):
		return self.order

	@_order.setter
	def _order(self, value):
		self.order = value



	@property
	def _selectedproduct(self):
		return self.selectedproduct

	@_selectedproduct.setter
	def _selectedproduct(self, value):
		self.selectedproduct = value



	@property
	def _id(self):
		return self.id

	@_id.setter
	def _id(self, value):
		self.id = value


	def get(self):
		ordercontentsDict = self.__dict__
		del ordercontentsDict['id']
		ordercontentsDict['idOrder'] = ordercontentsDict.pop('order')
		ordercontentsDict['idSelectedproduct'] = ordercontentsDict.pop('selectedproduct')
		return ordercontentsDict

	def set(self, order, selectedproduct, id):
		self.order = order
		self.selectedproduct = selectedproduct
		self.id = id
		return self