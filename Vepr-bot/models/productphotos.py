class Productphotos:

	def __init__(self):
		self.product = 0
		self.url_photo = " "
		self.photo_name = " "
		self.id = 0

	@property
	def _product(self):
		return self.product

	@_product.setter
	def _product(self, value):
		self.product = value



	@property
	def _url_photo(self):
		return self.url_photo

	@_url_photo.setter
	def _url_photo(self, value):
		self.url_photo = value

	@property
	def _photo_name(self):
		return self.photo_name

	@_photo_name.setter
	def _photo_name(self, value):
		self.photo_name = value



	@property
	def _id(self):
		return self.id

	@_id.setter
	def _id(self, value):
		self.id = value


	def get(self):
		productphotosDict = self.__dict__
		del productphotosDict['id']
		productphotosDict['idProduct'] = productphotosDict.pop('product')
		return productphotosDict

	def set(self, product, url_photo, id, photo_name):
		self.product = product
		self.url_photo = url_photo
		self.photo_name = photo_name
		self.id = id
		return self