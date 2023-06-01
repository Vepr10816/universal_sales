class Product:

    def __init__(self):
        self.description = " "
        self.product_price = 0
        self.product_name = " "
        self.currency = 0
        self.subcategory = 0
        self.id = 0
        self.productPhotosList = []
        self.productCharacteristicsList = []

    @property
    def _description(self):
        return self.description

    @_description.setter
    def _description(self, value):
        self.description = value

    @property
    def _product_price(self):
        return self.product_price

    @_product_price.setter
    def _product_price(self, value):
        self.product_price = value

    @property
    def _product_name(self):
        return self.product_name

    @_product_name.setter
    def _product_name(self, value):
        self.product_name = value

    @property
    def _currency(self):
        return self.currency

    @_currency.setter
    def _currency(self, value):
        self.currency = value

    @property
    def _subcategory(self):
        return self.subcategory

    @_subcategory.setter
    def _subcategory(self, value):
        self.subcategory = value

    @property
    def _id(self):
        return self.id

    @_id.setter
    def _id(self, value):
        self.id = value

    def get(self):
        productDict = self.__dict__
        del productDict['id']
        productDict['idCurrency'] = productDict.pop('currency')
        productDict['idSubcategory'] = productDict.pop('subcategory')
        return productDict

    def set(self, subcategory, id, product_name, description, product_price, currency,
            productPhotosList=None, productCharacteristicsList=None):
        self.subcategory = subcategory
        self.id = id
        self.product_name = product_name
        self.description = description
        self.product_price = product_price
        self.currency = currency
        self.productPhotosList = productPhotosList
        self.productCharacteristicsList = productCharacteristicsList
        return self
