class Status:

	def __init__(self):
		self.status_name = " "
		self.id = 0

	@property
	def _status_name(self):
		return self.status_name

	@_status_name.setter
	def _status_name(self, value):
		self.status_name = value



	@property
	def _id(self):
		return self.id

	@_id.setter
	def _id(self, value):
		self.id = value


	def get(self):
		statusDict = self.__dict__
		del statusDict['id']
		return statusDict

	def set(self, status_name, id):
		self.status_name = status_name
		self.id = id
		return self