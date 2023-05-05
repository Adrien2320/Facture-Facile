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
        """ Créer un nouveau client """
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
