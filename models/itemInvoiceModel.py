from dataclasses import dataclass, field
import sqlite3
from contextlib import closing

@dataclass
class ItemInvoice:
    quantity : int
    numberClient : int
    numberInvoice : int
    id_itemInvoice: int = field(default=-1)


class ItemInvoices:
    def __init__(self):
        """Constructeur"""
        self.database = sqlite3.connect("data_facture_facile.db")

    @property
    def cursor(self) -> sqlite3.Cursor:
        """Créer le paramètre"""
        return self.database.cursor()

    def commit(self):
        """Sauvegarde les modifications appliquée à la table"""
        self.database.commit()

    def add_itemInvoice(self,numberInvoice : int,numberItem:int,quantity:int):
        sql = """INSERT INTO T_Items_Invoices (idInvoice_itemInvoice, idItem_itemInvoice, quantity_itemInvoice) VALUES (?,?,?)"""

        with closing(self.cursor) as cursor:
            cursor.execute(sql,[numberInvoice,numberItem,quantity])
            self.commit()