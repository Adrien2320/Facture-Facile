import views.windowView as windowView
from models.itemModel import Data


class ItemController:
    def __init__(self, data: Data):
        """Constructeur"""
        self.data = data

    def new_item(self, name: str, description: str, htva_price: float, tva_tare: str):
        """Ajout un article dans la table T_items"""
        if name != "" and htva_price != "" and tva_tare != "":
            self.data.add_item(name, description, htva_price, tva_tare)
            windowView.Window.show_message_success("L'article a bien été enregistré.")
        else:
            windowView.Window.show_message_failure("Veuillez remplire les données")

    def modif_item(
        self,
        id_item: int,
        name: str,
        description: str,
        htva_price: float,
        tva_tare: str,
    ):
        """Modifie un article dans la table T_items"""
        if name != "" and htva_price != "" and tva_tare != "":
            self.data.modif_item(id_item, name, description, htva_price, tva_tare)
            windowView.Window.show_message_success("L'article a bien été modifier.")
        else:
            windowView.Window.show_message_failure("Veuillez remplire les données")

    def delete_item(self, id_item):
        """Supprime un article de la table T_items"""
        if id_item != "":
            self.data.delete_item(id_item)
            windowView.Window.show_message_success("L'article a bien été supprimé.")
        else:
            windowView.Window.show_message_failure("Veuillez remplire les données")

    def load_data_items(self):
        """Récupère l'ensemble de la table article"""
        result = self.data.load_items()
        return result

    def load_data_item(self, id_item):
        """Récupère un élément de la table article"""
        return self.data.load_item(id_item)

    def check_if_item_exist(self, name: str):
        """Vérifie si l'article existe déjà et retourne la réponse en boolean"""
        return self.data.check_exist_or_no(name)
