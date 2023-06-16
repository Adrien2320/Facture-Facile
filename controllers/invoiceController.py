from models.invoiceModel import Invoices

class InvoiceController:

    def __init__(self,data : Invoices):
        self.data = data

    def add(self,date: str, idCustomer: int, myCompany: str):
        return self.data.add_invoice(date,idCustomer,myCompany)
