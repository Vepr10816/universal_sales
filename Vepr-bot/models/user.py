class User:

	def __init__(self):
		self.access_token = " "
		self.refresh_token = " "
		self.salt = " "
		self.hash_password = " "
		self.tg = " "
		self.email = " "
		self.id = 0
		self.middle_name = " "
		self.last_name = " "
		self.user_name = " "
		self.first_name = " "

	@property
	def _access_token(self):
		return self.access_token

	@_access_token.setter
	def _access_token(self, value):
		self.access_token = value



	@property
	def _refresh_token(self):
		return self.refresh_token

	@_refresh_token.setter
	def _refresh_token(self, value):
		self.refresh_token = value



	@property
	def _salt(self):
		return self.salt

	@_salt.setter
	def _salt(self, value):
		self.salt = value



	@property
	def _hash_password(self):
		return self.hash_password

	@_hash_password.setter
	def _hash_password(self, value):
		self.hash_password = value



	@property
	def _tg(self):
		return self.tg

	@_tg.setter
	def _tg(self, value):
		self.tg = value



	@property
	def _email(self):
		return self.email

	@_email.setter
	def _email(self, value):
		self.email = value



	@property
	def _id(self):
		return self.id

	@_id.setter
	def _id(self, value):
		self.id = value



	@property
	def _middle_name(self):
		return self.middle_name

	@_middle_name.setter
	def _middle_name(self, value):
		self.middle_name = value



	@property
	def _last_name(self):
		return self.last_name

	@_last_name.setter
	def _last_name(self, value):
		self.last_name = value



	@property
	def _user_name(self):
		return self.user_name

	@_user_name.setter
	def _user_name(self, value):
		self.user_name = value



	@property
	def _first_name(self):
		return self.first_name

	@_first_name.setter
	def _first_name(self, value):
		self.first_name = value


	def get(self):
		userDict = self.__dict__
		del userDict['id']
		userDict['idTg'] = userDict.pop('tg')
		return userDict

	def set(self, access_token, refresh_token, salt, hash_password, tg, email, id, middle_name, last_name, user_name, first_name):
		self.access_token = access_token
		self.refresh_token = refresh_token
		self.salt = salt
		self.hash_password = hash_password
		self.tg = tg
		self.email = email
		self.id = id
		self.middle_name = middle_name
		self.last_name = last_name
		self.user_name = user_name
		self.first_name = first_name
		return self