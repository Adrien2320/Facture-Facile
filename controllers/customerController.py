import views.windowView as windowView
from models.customerModel import Customers


class CustomerController:
    def __init__(self, data: Customers):
        self.data = data


