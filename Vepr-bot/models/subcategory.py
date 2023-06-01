class Subcategory:

	def __init__(self):
		self.category = 0
		self.subcategory_name = " "
		self.id = 0
		self.productList = []

	@property
	def _category(self):
		return self.category

	@_category.setter
	def _category(self, value):
		self.category = value



	@property
	def _subcategory_name(self):
		return self.subcategory_name

	@_subcategory_name.setter
	def _subcategory_name(self, value):
		self.subcategory_name = value



	@property
	def _id(self):
		return self.id

	@_id.setter
	def _id(self, value):
		self.id = value


	def get(self):
		subcategoryDict = self.__dict__
		del subcategoryDict['id']
		subcategoryDict['idCategory'] = subcategoryDict.pop('category')
		return subcategoryDict

	def set(self, category, subcategory_name, id, productList=None):
		self.category = category
		self.subcategory_name = subcategory_name
		self.id = id
		self.productList = productList
		return self