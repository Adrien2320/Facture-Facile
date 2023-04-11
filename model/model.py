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
        """ Crée la table items"""
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
        """ Crée un item dans la table items"""
        sql = """ INSERT INTO T_Items (name_item, description_item, htva_price_item, tva_tare_item) VALUES (?,?,?,?)"""

        with closing(self.cursor) as cursor:
            cursor.execute(
                sql,
                [item.name_item, item.description_item, item.htva_price, item.tva_tare],
            )
            self.commit()

    def load_items(self):
        """ Récupère tous les articles dans la table items"""
        sql = """ SELECT * FROM T_Items"""

        with closing(self.cursor) as cursor:
            result = cursor.execute(sql)
            result.row_factory = lambda cursor, row: Item(
                id_item=row[0],
                name_item=row[1],
                description_item=row[2],
                htva_price=row[3],
                tva_tare=row[4],
            )
            return result.fetchall()

    def load_item(self, id_item: int):
        """ Récupère un article dans la table items"""
        sql = """ SELECT id_item,name_item,description_item,htva_price_item,tva_tare_item FROM T_Items WHERE id_item = ?"""

        with closing(self.cursor) as cursor:
            result = cursor.execute(sql, [id_item])
            result.row_factory = lambda cursor, row: Item(
                id_item=row[0],
                name_item=row[1],
                description_item=row[2],
                htva_price=row[3],
                tva_tare=row[4],
            )
            return result.fetchone()
