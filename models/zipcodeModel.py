from dataclasses import dataclass, field
import sqlite3
from contextlib import closing


@dataclass
class ZipCode:
    codePostal_zipcode: str
    locality_zipcode: str
    id_zipcode: int = field(default=-1)


class ZipCodes:
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

    def loads_zipcode(self):
        """Récupère tous les articles dans la table T_items"""
        sql = """ SELECT * FROM T_Zipcodes"""

        with closing(self.cursor) as cursor:
            result = cursor.execute(sql)
            result.row_factory = lambda cursor, row: ZipCode(
                id_zipcode=row[0],
                codePostal_zipcode=row[1],
                locality_zipcode=row[2],
            )
            return result.fetchall()

    def load_zipcode(self, index_zipCode):
        """Récupère une localité et code postal"""
        sql = """ SELECT id_zipcode, postal_code_zipcode, locality_zipcode FROM T_Zipcodes WHERE id_zipcode = ? """

        with closing(self.cursor) as cursor:
            result = cursor.execute(sql ,[index_zipCode])
            result.row_factory = lambda cursor, row: ZipCode(
                    id_zipcode=row[0],
                    codePostal_zipcode=row[1],
                    locality_zipcode=row[2],
            )
            return result.fetchone()

