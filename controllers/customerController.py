import views.windowView as windowView
from models.customerModel import Customers


class CustomerController:
    def __init__(self, data: Customers):
        self.data = data

    def new_customer(
        self,
        nameCustomer: str,
        firstNameCustomer: str,
        addressCustomer: str,
        postalCodeCustomer: int,
        typeCustomer: str,
        numberTvaCustomer: str,
        emailCustomer: str,
        phoneCustomer: str,
    ):
        """Créer un nouveau client"""
        if (
            nameCustomer != ""
            and addressCustomer != ""
            and postalCodeCustomer != ""
            and typeCustomer != ""
        ):
            self.data.new_customer(
                nameCustomer,
                firstNameCustomer,
                addressCustomer,
                postalCodeCustomer,
                typeCustomer,
                numberTvaCustomer,
                emailCustomer,
                phoneCustomer,
            )
            windowView.Window.show_message_success("Le client a bien été enregistré.")
        else:
            windowView.Window.show_message_failure("Veuillez remplire les données")

    def load_customers(self):
        result = self.data.load_customers()
        return result

    def load_customer(self, id_customer):
        """Rècupère un èlèment de la table client"""
        return self.data.load_customer(id_customer)

    def delete_item(self, id_customer: int):
        """Supprime un client de la base de donnée"""
        if id_customer != "":
            self.data.delete_item(id_customer)
            windowView.Window.show_message_success("Le client a bien été supprimé.")
        else:
            windowView.Window.show_message_failure("Veuillez remplire les données")

    def modif_item(
        self,
        idCustomer: int,
        nameCustomer: str,
        firstNameCustomer: str,
        addressCustomer: str,
        postalCodeCustomer: int,
        typeCustomer: str,
        numberTvaCustomer: str,
        emailCustomer: str,
        phoneCustomer: str,
    ):
        """Modifie un article dans la table T_items"""
        if (
            idCustomer != ""
            and nameCustomer != ""
            and firstNameCustomer != ""
            and addressCustomer != ""
            and postalCodeCustomer != ""
            and typeCustomer != ""
        ):
            self.data.modif_item(
                idCustomer,
                nameCustomer,
                firstNameCustomer,
                addressCustomer,
                postalCodeCustomer,
                typeCustomer,
                numberTvaCustomer,
                emailCustomer,
                phoneCustomer,
            )
            windowView.Window.show_message_success("Le client a bien été modifier.")
        else:
            windowView.Window.show_message_failure("Veuillez remplire les données")
