from dataclasses import dataclass, field
import sqlite3
from contextlib import closing


@dataclass
class Invoice:
    date_invoice: str
    numberCustomer: int
    my_company: str
    numbers_invoice: int = field(default=-1)


class Invoices:
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

    def add_invoice(self, date: str, idCustomer: int, myCompany: str):
        """crée une facture dans la table T_Invoices"""
        sql = """INSERT INTO T_Invoices (date_invoice, customer_invoice, myCompany_invoice) VALUES (?,?,?); SELECT last_insert_rowid()"""

        with closing(self.cursor) as cursor:
            result = cursor.execute(sql, [date, idCustomer, myCompany])
            self.commit()
        return result
