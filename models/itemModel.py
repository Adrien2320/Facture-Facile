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
        """Constructeur"""
        self.database = sqlite3.connect("data_facture_facile.db")

    @property
    def cursor(self) -> sqlite3.Cursor:
        """Créer le paramètre"""
        return self.database.cursor()

    def commit(self):
        """Sauvegarde les modifications appliquée à la table"""
        self.database.commit()

    def add_item(
        self, name_item: str, description_item: str, htva_price: float, tva_tare: str
    ):
        """Crée un article dans la table T_items"""
        sql = """ INSERT INTO T_Items (name_item, description_item, htva_price_item, tva_tare_item) VALUES (?,?,?,?)"""

        with closing(self.cursor) as cursor:
            cursor.execute(
                sql,
                [name_item, description_item, htva_price, tva_tare],
            )
            self.commit()

    def modif_item(
        self,
        id_item: int,
        name_item: str,
        description_item: str,
        htva_price: float,
        tva_tare: str,
    ):
        """Modifie un article dans la table T_items"""
        sql = """ UPDATE T_Items SET name_item = ?,description_item = ?,htva_price_item = ?,tva_tare_item=?   WHERE id_item = ? """

        with closing(self.cursor) as cursor:
            cursor.execute(
                sql,
                [name_item, description_item, htva_price, tva_tare, id_item],
            )
            self.commit()

    def load_items(self):
        """Récupère tous les articles dans la table T_items"""
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
        """Récupère un article dans la table T_items"""
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

    def delete_item(self, id_item: int):
        """Supprime un article de la table T_items"""
        sql = """ DELETE FROM T_Items WHERE id_item = ? """

        with closing(self.cursor) as cursor:
            cursor.execute(sql, [id_item])
            self.commit()

    def check_exist_or_no(self, name: str) -> bool:
        """Vérifier si l'article existe déjà et retourne oui ou non"""
        sql = """ SELECT COUNT(*) FROM T_Items WHERE name_item=?"""
        with closing(self.cursor) as cursor:
            cursor.execute(sql, [name])
            result = cursor.fetchone()
            if result[0] == 0:
                return False
            else:
                return True
