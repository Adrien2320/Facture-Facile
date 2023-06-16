import views.windowView as windowView
from models.companyModel import MyCompanys

class CompanyContoller:

    def __init__(self, data: MyCompanys):
        self.data = data

    def add_company(self,name :str,address :str,postalCode :int,numberPhone:str,emil:str,tva:str,accountNumber:str):
        if (name!=""and address!=""and postalCode!=""and tva!=""and accountNumber!=""):
            self.data.add_myCompany(name,address,postalCode,numberPhone,emil,tva,accountNumber)
            windowView.Window.show_message_success("Les données ont bien été enregistré.")
        else:
            windowView.Window.show_message_failure("Veuillez remplire les données")

    def modif_company(self,name :str,address :str,postalCode :int,numberPhone:str,emil:str,tva:str,accountNumber:str,old_name:str):
        if (name != "" and address != "" and postalCode != "" and tva != "" and accountNumber != ""):
            self.data.modif_myCompany(name,address,postalCode,numberPhone,emil,tva,accountNumber,old_name)
            windowView.Window.show_message_success("Les données ont bien été modifier.")
        else:
            windowView.Window.show_message_failure("Veuillez remplire les données")
    def load_company(self):
        return self.data.load_myCompany()
