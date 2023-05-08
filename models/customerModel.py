from dataclasses import dataclass, field
import sqlite3
from contextlib import closing


@dataclass
class Customer:
    name_customer: str
    first_name: str
    address_customer: str
    postalCode_customer: int
    type_customer: str
    numberTva_customer: str
    email_customer: str
    phone_customer: str
    id_customer: int = field(default=-1)


class Customers:
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

    def new_customer(
        self,
        nameCustomer: str,
        firstNameCustomer: str,
        addressCustomer: str,
        postalCodeCustomer: int,
        typeCustomer: str,
        numberTvaCustomer: str,
        emailCustomer: str,
        phoneCustomer: str,
    ):
        """Créer un nouveau client"""

        sql = """ INSERT INTO T_Customers(name_customer, first_name_customer, address_customer, postal_code, type_customer, number_tva, email_customer, phone_customer) VALUES (?,?,?,?,?,?,?,?)"""

        with closing(self.cursor) as cursor:
            cursor.execute(
                sql,
                [
                    nameCustomer,
                    firstNameCustomer,
                    addressCustomer,
                    postalCodeCustomer,
                    typeCustomer,
                    numberTvaCustomer,
                    emailCustomer,
                    phoneCustomer,
                ],
            )
            self.commit()

    def load_customers(self):
        """Récupère tous les articles dans la table T_Customer"""
        sql = """ SELECT * FROM T_Customers"""

        with closing(self.cursor) as cursor:
            result = cursor.execute(sql)
            result.row_factory = lambda cursor, row: Customer(
                id_customer=row[0],
                name_customer=row[1],
                first_name=row[2],
                address_customer=row[3],
                postalCode_customer=row[4],
                type_customer=row[5],
                numberTva_customer=row[6],
                email_customer=row[7],
                phone_customer=row[8],
            )
            return result.fetchall()

    def load_customer(self, id_customer):
        """Récupère un client dans la table T_Customer"""
        sql = """ SELECT id_customer, name_customer, first_name_customer, address_customer, postal_code, type_customer, number_tva, email_customer, phone_customer FROM T_Customers WHERE id_customer = ?"""

        with closing(self.cursor) as cursor:
            result = cursor.execute(sql, [id_customer])
            result.row_factory = lambda cursor, row: Customer(
                id_customer=row[0],
                name_customer=row[1],
                first_name=row[2],
                address_customer=row[3],
                postalCode_customer=row[4],
                type_customer=row[5],
                numberTva_customer=row[6],
                email_customer=row[7],
                phone_customer=row[8],
            )
            return result.fetchone()

    def delete_item(self, id_customer):
        """Supprime un client"""
        sql = """ DELETE FROM T_Customers WHERE id_customer = ? """

        with closing(self.cursor) as cursor:
            cursor.execute(sql, [id_customer])
            self.commit()

    def modif_item(
        self,
        id_customer: int,
        nameCustomer: str,
        firstNameCustomer: str,
        addressCustomer: str,
        postalCodeCustomer: int,
        typeCustomer: str,
        numberTvaCustomer: str,
        emailCustomer: str,
        phoneCustomer: str,
    ):
        """Modifie un client"""
        sql = """ UPDATE T_Customers SET name_customer=?, first_name_customer=?, address_customer=?, postal_code=?, type_customer=?, number_tva=?, email_customer=?, phone_customer=?   WHERE id_customer = ? """

        with closing(self.cursor) as cursor:
            cursor.execute(
                sql,
                [
                    nameCustomer,
                    firstNameCustomer,
                    addressCustomer,
                    postalCodeCustomer,
                    typeCustomer,
                    numberTvaCustomer,
                    emailCustomer,
                    phoneCustomer,
                    id_customer,
                ],
            )
            self.commit()
