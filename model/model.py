from dataclasses import dataclass, field
import sqlite3
from contextlib import closing


@dataclass
class Item:
    name_item: str
    description_item: str
    htva_price: float
    tva_tare: str
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
        htva_price_item REAL NOT NULL ,
        tva_tare_item TEXT NOT NULL                     
        ) """

        with closing(self.cursor) as cursor:
            cursor.execute(sql)
            self.commit()

    def add_item(self, item: Item):
        sql = """ INSERT INTO T_Items (name_item, description_item, htva_price_item, tva_tare_item) VALUES (?,?,?,?)"""

        with closing(self.cursor) as cursor:
            cursor.execute(
                sql,
                [item.name_item, item.description_item, item.htva_price, item.tva_tare],
            )
            self.commit()
