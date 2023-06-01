class FinanceData:
    '''def __init__(self, id, operationName, description, operationDate, operationTotal, isDeleted, category):
        self.id = id
        self.operationName = operationName
        self.description = description
        self.operationDate = operationDate
        self.operationTotal = operationTotal
        self.isDeleted = isDeleted
        self.category = category

    def get(self):
        dict = self.__dict__
        del dict['id']
        dict['idCategory'] = dict.pop('category')
        return dict'''

    def __init__(self):
        self._operationName = ""
        self._description = ""

    @property
    def operationName(self):
        return self._operationName

    @operationName.setter
    def operationName(self, value):
        self._operationName = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
