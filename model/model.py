from dataclasses import dataclass, field
import sqlite3
from contextlib import closing


@dataclass
class Item:
    name_item: str
    description_item: str
    prix_htva: float
    taux_tva: int
    id_item: int = field(default=-1)


class Data:
    def __init__(self):
        self.database = sqlite3.connect("data_facture_facile.db")
        self.create_table()

    @property
    def cursor(self) -> sqlite3.Cursor:
        return self.database.cursor()

    def commit(self):
        self.database.commit()

    def create_table(self):
        sql = """ CREATE TABLE IF NOT EXISTS T_Items (
        id_item INTEGER PRIMARY KEY AUTOINCREMENT,
        name_item TEXT NOT NULL ,
        description_item TEXT,
        prix_htva_item REAL NOT NULL ,
        taux_tva_item INTEGER NOT NULL                     
        ) """

        with closing(self.cursor) as cursor:
            cursor.execute(sql)
            self.commit()
