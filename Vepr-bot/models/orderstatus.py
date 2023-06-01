import datetime


class Orderstatus:

	def __init__(self):
		self.date_status = datetime.datetime.now()
		self.order = 0
		self.status = 0
		self.id = 0

	@property
	def _date_status(self):
		return self.date_status

	@_date_status.setter
	def _date_status(self, value):
		self.date_status = value



	@property
	def _order(self):
		return self.order

	@_order.setter
	def _order(self, value):
		self.order = value



	@property
	def _status(self):
		return self.status

	@_status.setter
	def _status(self, value):
		self.status = value



	@property
	def _id(self):
		return self.id

	@_id.setter
	def _id(self, value):
		self.id = value


	def get(self):
		orderstatusDict = self.__dict__
		del orderstatusDict['id']
		orderstatusDict['idOrder'] = orderstatusDict.pop('order')
		orderstatusDict['idStatus'] = orderstatusDict.pop('status')
		return orderstatusDict

	def set(self, date_status, order, status, id):
		self.date_status = date_status
		self.order = order
		self.status = status
		self.id = id
		return self