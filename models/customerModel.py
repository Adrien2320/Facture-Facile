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
