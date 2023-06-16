from dataclasses import dataclass, field
import sqlite3
from contextlib import closing

@dataclass
class MyCompany:
    name : str
    address : str
    postalCode : int
    phoneNumber : str
    email : str
    tva : str
    accountNumber : str


class MyCompanys:
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

    def add_myCompany(self,name,adresse,postalCode,numberPhone,email,tva,accountNumber):
        """créer les donnes de l'entreprise"""
        sql = """INSERT INTO T_MyCompany (name_company, address_company, postalCode_company, phone_company, email_company, tva_company, accountNumber_company) VALUES (?,?,?,?,?,?,?)"""

        with closing(self.cursor) as cursor:
            cursor.execute(sql,[name,adresse,postalCode,numberPhone,email,tva,accountNumber])
            self.commit()

    def modif_myCompany(self,name,adresse,postalCode,numberPhone,email,tva,accountNumber,old_name):
        """modifie les coordonnées de l'entreprise"""
        sql = """ UPDATE T_MyCompany SET name_company=?, address_company=?, postalCode_company=?, phone_company=?, email_company=?, tva_company=?, accountNumber_company=? WHERE name_company = ?"""

        with closing(self.cursor) as cursor :
            cursor.execute(sql,[name,adresse,postalCode,numberPhone,email,tva,accountNumber,old_name])
            self.commit()

    def load_myCompany(self):
        """Récupère les données de l'entreprise"""
        sql = """ SELECT * FROM T_MyCompany"""
        with   closing(self.cursor) as cursor:
            result = cursor.execute(sql)
            result.row_factory = lambda cursor, row: MyCompany(
                name=row[0],
                address=row[1],
                postalCode=row[2],
                phoneNumber=row[3],
                email=row[4],
                tva=row[5],
                accountNumber=row[6],
            )
            return result.fetchall()


