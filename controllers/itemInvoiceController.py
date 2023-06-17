from models.itemInvoiceModel import ItemInvoices


class ItemInvoiceController:
    def __init__(self, data: ItemInvoices):
        self.data = data

    def add_itemInvoice(selfn, numberInvoice: int, numberItem: int, quantity: int):
        selfn.data.add_itemInvoice(numberInvoice, numberItem, quantity)
