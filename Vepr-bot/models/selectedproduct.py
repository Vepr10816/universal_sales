class Selectedproduct:

	def __init__(self):
		self.product_quantity = 0
		self.product = 0
		self.id = 0

	@property
	def _product_quantity(self):
		return self.product_quantity

	@_product_quantity.setter
	def _product_quantity(self, value):
		self.product_quantity = value



	@property
	def _product(self):
		return self.product

	@_product.setter
	def _product(self, value):
		self.product = value



	@property
	def _id(self):
		return self.id

	@_id.setter
	def _id(self, value):
		self.id = value


	def get(self):
		selectedproductDict = self.__dict__
		del selectedproductDict['id']
		selectedproductDict['idProduct'] = selectedproductDict.pop('product')
		return selectedproductDict

	def set(self, product_quantity, product, id):
		self.product_quantity = product_quantity
		self.product = product
		self.id = id
		return self