class Order:

	def __init__(self):
		self.user = 0
		self.comment = " "
		self.id = 0
		self.total_price = 0

	@property
	def _total_price(self):
		return self.total_price

	@_total_price.setter
	def _total_price(self, value):
		self.total_price = value


	@property
	def _user(self):
		return self.user

	@_user.setter
	def _user(self, value):
		self.user = value



	@property
	def _comment(self):
		return self.comment

	@_comment.setter
	def _comment(self, value):
		self.comment = value



	@property
	def _id(self):
		return self.id

	@_id.setter
	def _id(self, value):
		self.id = value


	def get(self):
		orderDict = self.__dict__
		del orderDict['id']
		orderDict['idUser'] = orderDict.pop('user')
		return orderDict

	def set(self, user, comment, id, total_price):
		self.user = user
		self.comment = comment
		self.id = id
		self.total_price = total_price
		return self