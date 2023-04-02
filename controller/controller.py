from model.model import Data, Item
from view.view import MainView


class Controller:
    def __init__(self, view: MainView, data: Data):
        self.view = view
        self.data = data

    def add_item(self, name: str, description: str, htva_price: float, tva_tare: str):
        if name != "" and htva_price != "" and tva_tare != "":
            self.data.add_item(name, description, htva_price, tva_tare)
