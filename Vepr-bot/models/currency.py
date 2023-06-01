class Currency:

	def __init__(self):
		self.currency_name = " "
		self.id = 0

	@property
	def _currency_name(self):
		return self.currency_name

	@_currency_name.setter
	def _currency_name(self, value):
		self.currency_name = value



	@property
	def _id(self):
		return self.id

	@_id.setter
	def _id(self, value):
		self.id = value


	def get(self):
		currencyDict = self.__dict__
		del currencyDict['id']
		return currencyDict

	def set(self, currency_name, id):
		self.currency_name = currency_name
		self.id = id
		return self