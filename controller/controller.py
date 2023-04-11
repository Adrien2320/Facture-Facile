from model.model import Data, Item
from view.view import MainView


class Controller:
    def __init__(self, view: MainView, data: Data):
        self.view = view
        self.data = data

    def new_item(self, name, description, htva_price, tva_tare):
        """ Ajout un item dans la base de données """
        if name != "" and htva_price != "" and tva_tare != "":
            item = Item(name, description, htva_price, tva_tare)
            self.data.add_item(item)
            self.view.show_message_success("L'article a bien été enregistré.")
        else:
            self.view.show_message_failure("Veuillez remplire les données")

    def load_data_items(self):
        """ Récupère l'ensemble de la table article"""
        result = self.data.load_items()
        return result

    def load_data_item(self, id_item):
        """Récupère un élément de la table article"""
        return self.data.load_item(id_item)
