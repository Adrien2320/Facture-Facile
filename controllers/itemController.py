
from models.itemModel import Data


class ItemController:
    def __init__(self,data : Data):
        self.data = data

    def new_item(self, name: str, description: str, htva_price: float, tva_tare: str):
            """Ajout un article dans la base de données"""
            if name != "" and htva_price != "" and tva_tare != "":
                self.data.add_item(name,description,htva_price,tva_tare)
                self.view_dialogs.show_message_success("L'article a bien été enregistré.")
            else:
                self.view_dialogs.show_message_failure("Veuillez remplire les données")

    def modif_item(
        self,
        id_item: int,
        name: str,
        description: str,
        htva_price: float,
        tva_tare: str,
    ):
        # Modifie un article dans la base de données
        if name != "" and htva_price != "" and tva_tare != "":
            self.data.modif_item(id_item,name,description,htva_price,tva_tare)
            self.view_dialogs.show_message_success("L'article a bien été modifier.")
        else:
            self.view_dialogs.show_message_failure("Veuillez remplire les données")

    def delete_item(self,id_item):
        # Supprime un article de la base de données
        if id_item != "":
            self.data.delete_item(id_item)
            self.view_dialogs.show_message_success("L'article a bien été supprimé.")
        else:
            self.view_dialogs.show_message_failure("Veuillez remplire les données")

    def load_data_items(self):
        # Récupère l'ensemble de la table article
        result = self.data.load_items()
        return result

    def load_data_item(self, id_item):
        #Récupère un élément de la table article
        return self.data.load_item(id_item)

