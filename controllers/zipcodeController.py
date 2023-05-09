import views.windowView as windowView
from models.zipcodeModel import ZipCodes


class ZipCodeController:
    def __init__(self, data: ZipCodes):
        self.data = data

    def loads_zipcode(self):
        """Récupère toutes les données de la table T_Zipcode"""
        return self.data.loads_zipcode()

    def load_zipcode(self,index_zipCode):
        return self.data.load_zipcode(index_zipCode)
