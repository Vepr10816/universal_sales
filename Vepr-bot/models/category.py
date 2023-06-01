class Category:

	def __init__(self):
		self.category_name = " "
		self.mycompany = 0
		self.id = 0
		self.subcategoryList = []

	@property
	def _category_name(self):
		return self.category_name

	@_category_name.setter
	def _category_name(self, value):
		self.category_name = value



	@property
	def _mycompany(self):
		return self.mycompany

	@_mycompany.setter
	def _mycompany(self, value):
		self.mycompany = value



	@property
	def _id(self):
		return self.id

	@_id.setter
	def _id(self, value):
		self.id = value


	def get(self):
		categoryDict = self.__dict__
		del categoryDict['id']
		categoryDict['idMycompany'] = categoryDict.pop('mycompany')
		return categoryDict

	def set(self, category_name, mycompany, id, subcategoryList=None):
		self.category_name = category_name
		self.mycompany = mycompany
		self.id = id
		self.subcategoryList = subcategoryList
		return self