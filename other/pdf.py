from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # en-tête de la facture
        self.set_font("Arial", "B", 15)
        self.cell(0, 10, "FACTURE", 0, 1, "L")

    def footer(self):
        # Pied de page avec le numéro de page
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page %s" % self.page_no(), 0, 0, "C")

    def add_invoice_header(self, invoice_number: int, invoice_date: str):
        # ajout la date et le numéro de facture
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Facture numéro: %s" % invoice_number, 0, 1, "L")
        self.cell(0, 10, "Date: %s" % invoice_date, 0, 1, "L")
        self.ln(10)

    def add_invoice_client_and_company(
        self,
        FullName_customer: str,
        name_company: str,
        address_customer: str,
        address_company: str,
        zipcode_customer: str,
        zipcode_company: str,
        numberTva_customer: str,
        numberTva_company: str,
        email_customer: str,
        email_company: str,
        phoneNumber_customer: str,
        phoneNumber_company: str,
        numberCustomer: int,
        accountNumberCompany: str,
    ):
        self.set_font("Arial", "B", 12)
        self.cell(0, 0, "Client", 0, 1, "L")
        self.cell(0, 0, "VENDEUR", 0, 1, "R")
        self.ln(10)
        self.cell(0, 0, FullName_customer, 0, 1, "L")
        self.cell(0, 0, name_company, 0, 1, "R")
        self.ln(5)
        self.cell(0, 0, address_customer, 0, 1, "L")
        self.cell(0, 0, address_company, 0, 1, "R")
        self.ln(5)
        self.cell(0, 0, zipcode_customer, 0, 1, "L")
        self.cell(0, 0, zipcode_company, 0, 1, "R")
        self.ln(5)
        self.cell(
            0,
            0,
            f"TVA:{numberTva_customer}" if numberTva_customer != " " else "",
            0,
            1,
            "L",
        )
        self.cell(
            0,
            0,
            f"TVA:{numberTva_company}" if numberTva_company != " " else "",
            0,
            1,
            "R",
        )
        self.ln(5)
        self.cell(0, 0, email_customer, 0, 1, "L")
        self.cell(0, 0, email_company, 0, 1, "R")
        self.ln(5)
        self.cell(0, 0, phoneNumber_customer, 0, 1, "L")
        self.cell(0, 0, phoneNumber_company, 0, 1, "R")
        self.ln(5)
        self.cell(0, 0, f"Numéro Client:{numberCustomer}", 0, 1, "L")
        self.cell(0, 0, f"IBAN:{accountNumberCompany}", 0, 1, "R")
        self.ln(5)

    def add_invoice_items(self, items):
        # variable
        totalHt21 = 0
        totalTaxe21 = 0
        totalHt12 = 0
        totalTaxe12 = 0
        totalHt6 = 0
        totalTaxe6 = 0
        taux21 = {}
        taux12 = {}
        taux6 = {}
        totalHtAll = 0
        totalTaxeAll = 0

        # En-têtes des colonnes
        self.set_font("Arial", "B", 12)
        self.cell(30, 10, "Référence", 1, 0, "C")
        self.cell(65, 10, "Produit", 1, 0, "C")
        self.cell(20, 10, "Taux Tva", 1, 0, "C")
        self.cell(10, 10, "Qté", 1, 0, "C")
        self.cell(35, 10, "Prix unitaire (HT)", 1, 0, "C")
        self.cell(30, 10, "Total (HT)", 1, 1, "C")

        # Données des éléments de la facture
        self.set_font("Arial", "", 12)
        for item in items:
            self.cell(30, 10, str(item["numéroArticle"]), 1, 0, "L")
            self.cell(65, 10, item["product"], 1, 0, "L")
            self.cell(20, 10, str(item["tauxTva"]), 1, 0, "R")
            self.cell(10, 10, str(item["quantity"]), 1, 0, "R")
            self.cell(35, 10, str(item["price"])+chr(128), 1, 0, "R")
            self.cell(30, 10, str(item["total"])+chr(128), 1, 1, "R")

            # récupère le total pour chaque article a 21%
            if item["tauxTva"] == "21%":
                totalHt21 += item["total"]
                totalTaxe21 += item["total"] / 100 * 21
                taux21 = {
                    "tauxTva": "21%",
                    "totalHt": totalHt21,
                    "totalTaxe": totalTaxe21,
                }

            # récupère le total pour chaque article a 12%
            elif item["tauxTva"] == "12%":
                totalHt12 += item["total"]
                totalTaxe12 += item["total"] / 100 * 21
                taux12: dict = {
                    "tauxTva": "12%",
                    "totalHt": totalHt12,
                    "totalTaxe": totalTaxe12,
                }

            # récupère le total pour chaque article a 6%
            else:
                totalHt6 += item["total"]
                totalTaxe6 += item["total"] / 100 * 21
                taux6: dict = {
                    "tauxTva": "6%",
                    "totalHt": totalHt6,
                    "totalTaxe": totalTaxe6,
                }

        elements = [taux21, taux12, taux6]

        self.ln(10)

        # En-têtes des colonnes
        var_y = self.get_y()
        self.set_font("Arial", "B", 12)
        self.cell(30, 10, "Taux de taxe", 1, 0, "C")
        self.cell(35, 10, "Prix de Base", 1, 0, "C")
        var_x = self.get_x()
        self.cell(30, 10, "Total Taxes", 1, 1, "C")

        # Données en desous du tableau a gauche
        self.set_font("Arial", "", 12)
        for element in elements:
            if not element == {}:
                self.cell(30, 10, str(element["tauxTva"]), 1, 0, "L")
                self.cell(35, 10, str(element["totalHt"])+chr(128), 1, 0, "L")
                self.cell(30, 10, str(element["totalTaxe"])+chr(128), 1, 0, "L")
                self.ln()
                totalHtAll += element["totalHt"]
                totalTaxeAll += element["totalTaxe"]

        # données en desous du tableau a droite
        self.set_font("Arial", "B", 12)
        self.set_y(var_y)
        self.set_x(var_x + 65)
        self.cell(30, 10, "Total (HT)", 1, 0, "R")
        self.set_font("Arial", "", 12)
        self.cell(30, 10, str(totalHtAll)+chr(128), 1, 0, "R")
        self.ln()
        self.set_x(var_x + 65)
        self.set_font("Arial", "B", 12)
        self.cell(30, 10, "Total Taxes", 1, 0, "R")
        self.set_font("Arial", "", 12)
        self.cell(30, 10, str(totalTaxeAll)+chr(128), 1, 0, "R")
        self.ln()
        self.set_x(var_x + 65)
        self.set_font("Arial", "B", 12)
        self.cell(30, 10, "Total", 1, 0, "R")
        self.set_font("Arial", "", 12)
        self.cell(30, 10, str(totalHtAll + totalTaxeAll)+chr(128), 1, 0, "R")

    def create_pdf(self, name: str):
        self.output(name, "F")
