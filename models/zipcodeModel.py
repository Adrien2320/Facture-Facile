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
        pass
