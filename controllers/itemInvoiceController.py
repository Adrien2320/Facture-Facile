from models.itemInvoiceModel import ItemInvoices


class ItemInvoiceController:
    def __init__(self, data: ItemInvoices):
        self.data = data

    def add_itemInvoice(self, numberInvoice: int, items):
        self.data.add_itemInvoice(numberInvoice, items)
