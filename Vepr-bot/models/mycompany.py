class Mycompany:

    def __init__(self):
        self.id = 0
        self.url_logo = " "
        self.description = " "
        self.company_name = " "
        self.logo_name = " "

    @property
    def _id(self):
        return self.id

    @_id.setter
    def _id(self, value):
        self.id = value

    @property
    def _url_logo(self):
        return self.url_logo

    @_url_logo.setter
    def _url_logo(self, value):
        self.url_logo = value

    @property
    def _logo_name(self):
        return self.logo_name

    @_logo_name.setter
    def _logo_name(self, value):
        self.logo_name = value

    @property
    def _description(self):
        return self.description

    @_description.setter
    def _description(self, value):
        self.description = value

    @property
    def _company_name(self):
        return self.company_name

    @_company_name.setter
    def _company_name(self, value):
        self.company_name = value

    def get(self):
        mycompanyDict = self.__dict__
        del mycompanyDict['id']
        return mycompanyDict

    def set(self, id, url_logo, description, company_name, logo_name):
        self.id = id
        self.url_logo = url_logo
        self.description = description
        self.company_name = company_name
        self.logo_name = logo_name
        return self
