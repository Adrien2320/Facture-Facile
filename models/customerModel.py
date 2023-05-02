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
        self.create_table()

    def create_table(self):
        pass
