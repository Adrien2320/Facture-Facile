from tkinter import PhotoImage

import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk
import views.windowView as windowView
import other.pdf as pdf
import datetime
import locale


class DataInvoice(ttk.Frame):
    tableCustomer: ttk.Treeview
    table_invoice: ttk.Treeview
    tableItem: ttk.Treeview

    tableCustomerWindow: ttk.Toplevel
    tableItemWindow: ttk.Toplevel

    en_quantityItem: ttk.Entry

    def __init__(self, window):
        """Constructeur"""
        # paramètre de la frame
        super().__init__(window)
        # variable
        self.window = window

        # position de la frame
        self.pack(side=cttk.RIGHT, fill=cttk.BOTH, expand=True)

        # config du grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # variable ttk customer
        self.id_customer: int = 0
        self.var_full_name_customer = ttk.StringVar()
        self.var_address_customer = ttk.StringVar()
        self.var_postal_code_customer = ttk.StringVar()
        self.var_number_tva_customer = ttk.StringVar()
        self.var_phone_customer = ttk.StringVar()

        # variable ttk my company
        self.var_name_company = ttk.StringVar()
        self.var_address_company = ttk.StringVar()
        self.var_postal_code_company = ttk.StringVar()
        self.var_number_tva_company = ttk.StringVar()
        self.var_email_company = ttk.StringVar()
        self.var_phone_company = ttk.StringVar()
        self.var_account_number_company = ttk.StringVar()

        # crate
        self.create_dataInvoice()

        # set variable ttk customer
        self.set_variable_ttk_customer()

        # set variable ttk company
        self.set_variable_ttk_company()

    @property
    def controllerCustomer(self):
        """Créer le paramètre controller du customer"""
        try:
            return self._controllerCustomer
        except AttributeError:
            windowView.Window.show_message_error("Pas de controlleur pour client")
            self.quit()

    @controllerCustomer.setter
    def controllerCustomer(self, value):
        """Assigne le paramètre controller du customer"""
        self._controllerCustomer = value

    @property
    def controllerZipcode(self):
        """Créer le paramètre controller du zipcode"""
        try:
            return self._controllerZipcode
        except AttributeError:
            windowView.Window.show_message_error("Pas de controlleur pour code postal")
            self.quit()

    @controllerZipcode.setter
    def controllerZipcode(self, value):
        """Assigne le paramètre controller du zipcode"""
        self._controllerZipcode = value

    @property
    def controllerItem(self):
        """Créer le paramètre controller du customer"""
        try:
            return self._controllerItem
        except AttributeError:
            windowView.Window.show_message_error("Pas de controlleur pour Article")
            self.quit()

    @controllerItem.setter
    def controllerItem(self, value):
        """Assigne le paramètre controller du customer"""
        self._controllerItem = value

    @property
    def controllerInvoice(self):
        """Créer le paramètre controller"""
        try:
            return self._controllerInvoice
        except AttributeError:
            windowView.Window.show_message_error("Pas de controlleur pour facture")
            self.quit()

    @controllerInvoice.setter
    def controllerInvoice(self, value):
        """Assigne le paramètre controller"""
        self._controllerInvoice = value

    @property
    def controllerItemInvoice(self):
        """Créer le paramètre controller"""
        try:
            return self._controllerItemInvoice
        except AttributeError:
            windowView.Window.show_message_error("Pas de controlleur pour Article facturé")
            self.quit()

    @controllerItemInvoice.setter
    def controllerItemInvoice(self, value):
        """Assigne le paramètre controller"""
        self._controllerItemInvoice = value

    @property
    def controllerCompany(self):
        """Créer le paramètre controller du customer"""
        try:
            return self._controllerCompany
        except AttributeError:
            windowView.Window.show_message_error("Pas de controlleur pour mon entreprise")
            self.quit()

    @controllerCompany.setter
    def controllerCompany(self, value):
        """Assigne le paramètre controller du customer"""
        self._controllerCompany = value

    def create_dataInvoice(self):
        """Créer les widgets"""

        # style
        ttk.Style().configure("data.TFrame", background="#283747")
        ttk.Style().configure("data.TLabel", background="#283747", font=("Georgia", 20))
        ttk.Style().configure("item.Treeview", background="#283747", rowheight=25)

        # frame
        top_frame = ttk.Frame(self)
        bottom_frame = ttk.Frame(self)
        customer_frame = ttk.Frame(top_frame, style="data.TFrame")
        my_company_frame = ttk.Frame(top_frame, style="data.TFrame")
        table_invoice_frame = ttk.Frame(bottom_frame, style="data.TFrame")
        table_invoice_frame.columnconfigure(0, weight=1)
        table_invoice_frame.rowconfigure(1, weight=1)

        # position frame
        top_frame.grid(row=0, column=0, sticky=cttk.EW, pady=20, padx=30)
        bottom_frame.grid(row=1, column=0, sticky=cttk.NSEW, pady=20, padx=30)
        customer_frame.pack(
            side=cttk.LEFT,
            fill=cttk.BOTH,
            expand=True,
            padx=10,
            pady=10,
        )
        my_company_frame.pack(
            side=cttk.RIGHT,
            fill=cttk.BOTH,
            expand=True,
            padx=10,
            pady=10,
        )
        table_invoice_frame.pack(
            side=cttk.TOP,
            fill=cttk.BOTH,
            expand=True,
            padx=10,
            pady=10,
        )

        # label customer
        lb_title = ttk.Label(
            customer_frame,
            text="Client",
            justify=cttk.CENTER,
            anchor=cttk.CENTER,
            style="data.TLabel",
        )
        lb_full_name = ttk.Label(
            customer_frame,
            textvariable=self.var_full_name_customer,
            style="data.TLabel",
        )
        lb_address = ttk.Label(
            customer_frame, textvariable=self.var_address_customer, style="data.TLabel"
        )
        lb_postal_code = ttk.Label(
            customer_frame,
            textvariable=self.var_postal_code_customer,
            style="data.TLabel",
        )
        lb_number_tva = ttk.Label(
            customer_frame,
            textvariable=self.var_number_tva_customer,
            style="data.TLabel",
        )
        lb_number_phone = ttk.Label(
            customer_frame, textvariable=self.var_phone_customer, style="data.TLabel"
        )

        # position customer
        lb_title.pack(side=cttk.TOP, fill=cttk.X, expand=True)
        lb_full_name.pack(side=cttk.TOP, fill=cttk.X, expand=True)
        lb_address.pack(side=cttk.TOP, fill=cttk.X, expand=True)
        lb_postal_code.pack(side=cttk.TOP, fill=cttk.X, expand=True)
        lb_number_tva.pack(side=cttk.TOP, fill=cttk.X, expand=True)
        lb_number_phone.pack(side=cttk.TOP, fill=cttk.X, expand=True)

        # label my company
        lb_title_company = ttk.Label(
            my_company_frame,
            text="Entreprise",
            justify=cttk.CENTER,
            anchor=cttk.CENTER,
            style="data.TLabel",
        )
        lb_full_name_company = ttk.Label(
            my_company_frame, textvariable=self.var_name_company, style="data.TLabel"
        )
        lb_address_company = ttk.Label(
            my_company_frame, textvariable=self.var_address_company, style="data.TLabel"
        )
        lb_postal_code_company = ttk.Label(
            my_company_frame,
            textvariable=self.var_postal_code_company,
            style="data.TLabel",
        )
        lb_number_tva_company = ttk.Label(
            my_company_frame,
            textvariable=self.var_number_tva_company,
            style="data.TLabel",
        )
        lb_email_company = ttk.Label(
            my_company_frame, textvariable=self.var_email_company, style="data.TLabel"
        )
        lb_number_phone_company = ttk.Label(
            my_company_frame, textvariable=self.var_phone_company, style="data.TLabel"
        )
        lb_account_number_company = ttk.Label(
            my_company_frame,
            textvariable=self.var_account_number_company,
            style="data.TLabel",
        )

        # position my company
        lb_title_company.pack(side=cttk.TOP, fill=cttk.X, expand=True, pady=4)
        lb_full_name_company.pack(side=cttk.TOP, fill=cttk.X, expand=True, pady=4)
        lb_address_company.pack(side=cttk.TOP, fill=cttk.X, expand=True, pady=4)
        lb_postal_code_company.pack(side=cttk.TOP, fill=cttk.X, expand=True, pady=4)
        lb_number_tva_company.pack(side=cttk.TOP, fill=cttk.X, expand=True, pady=4)
        lb_email_company.pack(side=cttk.TOP, fill=cttk.X, expand=True, pady=4)
        lb_number_phone_company.pack(side=cttk.TOP, fill=cttk.X, expand=True, pady=4)
        lb_account_number_company.pack(side=cttk.TOP, fill=cttk.X, expand=True, pady=4)

        # create table article
        lb_title_item = ttk.Label(
            table_invoice_frame, text="Article", anchor=cttk.CENTER, style="data.TLabel"
        )
        scrollbar = ttk.Scrollbar(table_invoice_frame, orient=cttk.VERTICAL)
        self.table_invoice = ttk.Treeview(
            table_invoice_frame,
            columns=[
                "itemCode",
                "item",
                "tvaRate",
                "priceHtva",
                "priceTvac",
                "quantity",
            ],
            yscrollcommand=scrollbar.set,
            selectmode=cttk.NONE,
            style="item.Treeview",
        )

        # config the scrollbar
        scrollbar.config(command=self.table_invoice.yview)

        # column configure
        self.table_invoice.column(
            "#0", anchor=cttk.W, stretch=False, width=0, minwidth=0
        )
        self.table_invoice.column(
            "itemCode",
            anchor=cttk.W,
            stretch=False,
        )
        self.table_invoice.column(
            "item",
            anchor=cttk.W,
            stretch=True,
        )
        self.table_invoice.column(
            "tvaRate",
            anchor=cttk.W,
            stretch=True,
        )
        self.table_invoice.column(
            "priceHtva",
            anchor=cttk.W,
            stretch=True,
        )
        self.table_invoice.column("priceTvac", anchor=cttk.W, stretch=True)
        self.table_invoice.column(
            "quantity",
            anchor=cttk.W,
            stretch=True,
        )

        # heading column
        self.table_invoice.heading("#0", anchor=cttk.W)
        self.table_invoice.heading("itemCode", text="Numéro Article", anchor=cttk.W)
        self.table_invoice.heading("item", text="Produit", anchor=cttk.W)
        self.table_invoice.heading("tvaRate", text="Taux Tva", anchor=cttk.W)
        self.table_invoice.heading("priceHtva", text="Prix HTVA", anchor=cttk.W)
        self.table_invoice.heading("priceTvac", text="Prix TVAC", anchor=cttk.W)
        self.table_invoice.heading("quantity", text="Quantité", anchor=cttk.W)

        # position views table
        lb_title_item.grid(columnspan=2, row=0, sticky=cttk.EW)
        self.table_invoice.grid(column=0, row=1, sticky=cttk.NSEW)
        scrollbar.grid(column=1, row=1, sticky=cttk.NS)

    def create_table_customer(self):
        """Affiche tous les clients dans une treeview"""
        # create toplevel
        self.tableCustomerWindow = ttk.Toplevel()
        self.tableCustomerWindow.minsize(480, 480)
        icon = PhotoImage(file="pictures/logo.png")
        self.tableCustomerWindow.iconphoto(False, icon)
        self.tableCustomerWindow.title("Recherche Client")

        self.tableCustomerWindow.columnconfigure(2, weight=1)
        self.tableCustomerWindow.columnconfigure(1, weight=1)
        self.tableCustomerWindow.columnconfigure(3, weight=1)
        self.tableCustomerWindow.rowconfigure(1, weight=1)

        # style
        ttk.Style().configure(
            "back.TButton",
            background="#C0392B",
            bordercolor="#C0392B",
            relief="flat",
            font=("Georgia", 15),
        )
        ttk.Style().configure(
            "confirm.TButton",
            background="#2ECC71",
            bordercolor="#2ECC71",
            relief="flat",
            font=("Georgia", 15),
        )
        ttk.Style().configure("my.Treeview", background="#283747", rowheight=25)
        ttk.Style().configure(
            "title.TLabel", background="#283747", font=("Georgia", 20)
        )

        # title
        lb_title = ttk.Label(
            self.tableCustomerWindow,
            text="Recherche Client",
            anchor=cttk.CENTER,
            font=("Georgia", 20),
        )

        # frame
        table_frame = ttk.Frame(self.tableCustomerWindow)

        # views table
        scrollbar = ttk.Scrollbar(table_frame, orient=cttk.VERTICAL)
        self.tableCustomer = ttk.Treeview(
            table_frame,
            columns=["id", "name", "firstName", "address"],
            yscrollcommand=scrollbar.set,
            selectmode=cttk.BROWSE,
            style="my.Treeview",
        )

        # config the scrollbar
        scrollbar.config(command=self.tableCustomer.yview)

        # format column
        self.tableCustomer.column(
            "#0", anchor=cttk.W, stretch=False, width=0, minwidth=0
        )
        self.tableCustomer.column("id", anchor=cttk.W, stretch=False, width=200)
        self.tableCustomer.column("name", anchor=cttk.W, stretch=True, width=200)
        self.tableCustomer.column("address", anchor=cttk.W, stretch=True, width=200)

        # heading column
        self.tableCustomer.heading("#0", anchor=cttk.W)
        self.tableCustomer.heading("id", text="Numéro Client", anchor=cttk.W)
        self.tableCustomer.heading("name", text="Nom", anchor=cttk.W)
        self.tableCustomer.heading("address", text="Adresse", anchor=cttk.W)

        # button widget
        bt_back = ttk.Button(
            self.tableCustomerWindow,
            text="Retour",
            style="back.TButton",
            command=self.tableCustomerWindow.destroy,
            width=15,
        )
        bt_confirm_selected = ttk.Button(
            self.tableCustomerWindow,
            text="Confirmer",
            style="confirm.TButton",
            command=self.insert_customer_into_invoice,
            width=15,
        )

        # position views table
        lb_title.grid(column=2, row=0, padx=10, pady=20)
        table_frame.grid(columnspan=5, row=1, sticky=cttk.NSEW, padx=20, pady=30)
        self.tableCustomer.pack(side=cttk.LEFT, fill=cttk.BOTH, expand=True)
        scrollbar.pack(side=cttk.LEFT, fill=cttk.Y)

        # button position
        bt_back.grid(column=1, row=2, padx=20, pady=20)
        bt_confirm_selected.grid(column=3, row=2, padx=20, pady=20)

    def set_variable_ttk_customer(
        self,
        id_customer: int = -1,
        name_customer: str = " ",
        address_customer: str = " ",
        postalCode_customer: str = " ",
        numberTva_customer: str = " ",
        numberPhone_customer: str = " ",
    ):
        """Assigne les variables clients de ttk"""
        self.id_customer = id_customer
        self.var_full_name_customer.set(f" {name_customer}")
        self.var_address_customer.set(f" {address_customer}")
        self.var_postal_code_customer.set(f" {postalCode_customer}")
        self.var_number_tva_customer.set(f" {numberTva_customer}")
        self.var_phone_customer.set(f" {numberPhone_customer}")

    def set_variable_ttk_company(
        self,
        name_company: str = " ",
        address_company: str = " ",
        postalCode_company: str = " ",
        numberTva_company: str = " ",
        email_company: str = " ",
        numberPhone_company: str = " ",
        accountNumber_company: str = " ",
    ):
        """Assigne les variables entreprises de ttk"""
        self.var_name_company.set(f" {name_company}")
        self.var_address_company.set(f" {address_company}")
        self.var_postal_code_company.set(f" {postalCode_company}")
        self.var_number_tva_company.set(f" {numberTva_company}")
        self.var_email_company.set(f" {email_company}")
        self.var_phone_company.set(f" {numberPhone_company}")
        self.var_account_number_company.set(f" {accountNumber_company}")

    def insert_data_in_tableCustomer(self):
        """Ajout chaque client dans la table"""
        customers = self.controllerCustomer.load_customers()

        for customer in customers:
            self.tableCustomer.insert(
                "",
                ttk.END,
                values=(
                    customer.id_customer,
                    f"{customer.name_customer} {customer.first_name}",
                    customer.address_customer,
                ),
            )

    def add_client(self):
        self.create_table_customer()
        self.insert_data_in_tableCustomer()

    def insert_customer_into_invoice(self):
        try:
            customer = self.get_selected_customer()
            code_postal_customer = self.get_postalCode_customer(
                customer.postalCode_customer
            )
            self.set_variable_ttk_customer(
                customer.id_customer,
                f"{customer.name_customer} {customer.first_name}",
                customer.address_customer,
                f"{code_postal_customer.codePostal_zipcode} {code_postal_customer.locality_zipcode}",
                customer.numberTva_customer,
                customer.phone_customer,
            )
            self.tableCustomerWindow.destroy()
        except AttributeError:
            windowView.Window.show_message_failure("Veuillez sélectionnez un élément!")

    def get_selected_customer(self):
        """Récupère les données de l'article, sélectionnez"""
        for selected_item in self.tableCustomer.selection():
            select = self.tableCustomer.item(selected_item)
            customer = select["values"]
            return self.controllerCustomer.load_customer(customer[0])

    def get_postalCode_customer(self, index_zipCode):
        """Récupère le code postal et la localité et la retourne sous un string"""
        return self.controllerZipcode.load_zipcode(index_zipCode)

    def create_table_item(self):
        """Affiche tous les articles dans une treeview"""
        # create toplevel
        self.tableItemWindow = ttk.Toplevel()
        self.tableItemWindow.minsize(480, 480)
        self.tableItemWindow.title("Recherche Article")
        icon = PhotoImage(file="pictures/logo.png")
        self.tableItemWindow.iconphoto(False, icon)

        self.tableItemWindow.columnconfigure(2, weight=1)
        self.tableItemWindow.columnconfigure(1, weight=1)
        self.tableItemWindow.columnconfigure(3, weight=1)
        self.tableItemWindow.rowconfigure(1, weight=1)

        # style
        ttk.Style().configure(
            "back.TButton",
            background="#C0392B",
            bordercolor="#C0392B",
            relief="flat",
            font=("Georgia", 15),
        )
        ttk.Style().configure(
            "confirm.TButton",
            background="#2ECC71",
            bordercolor="#2ECC71",
            relief="flat",
            font=("Georgia", 15),
        )
        ttk.Style().configure("my.Treeview", background="#283747", rowheight=25)
        ttk.Style().configure(
            "quantity.TEntry", background="#283747", font=("Georgia", 15)
        )

        # title
        lb_title = ttk.Label(
            self.tableItemWindow,
            text="Recherche Article",
            anchor=cttk.CENTER,
            font=("Georgia", 20),
        )

        # frame
        table_frame = ttk.Frame(self.tableItemWindow)
        quantity_frame = ttk.Frame(self.tableItemWindow)

        # views table
        scrollbar = ttk.Scrollbar(table_frame, orient=cttk.VERTICAL)
        self.tableItem = ttk.Treeview(
            table_frame,
            columns=["id", "name", "htva", "tvac"],
            yscrollcommand=scrollbar.set,
            selectmode=cttk.BROWSE,
            style="my.Treeview",
        )

        # config the scrollbar
        scrollbar.config(command=self.tableItem.yview)

        # format column
        self.tableItem.column("#0", anchor=cttk.W, stretch=False, width=0, minwidth=0)
        self.tableItem.column("id", anchor=cttk.W, stretch=False, width=200)
        self.tableItem.column("name", anchor=cttk.W, stretch=True, width=200)
        self.tableItem.column("htva", anchor=cttk.W, stretch=True, width=200)
        self.tableItem.column("tvac", anchor=cttk.W, stretch=True, width=200)

        # heading column
        self.tableItem.heading("#0", anchor=cttk.W)
        self.tableItem.heading("id", text="Code Article", anchor=cttk.W)
        self.tableItem.heading("name", text="Nom", anchor=cttk.W)
        self.tableItem.heading("htva", text="Prix HTVA", anchor=cttk.W)
        self.tableItem.heading("tvac", text="Prix TVAC", anchor=cttk.W)

        # quanty widget
        lb_quantity = ttk.Label(quantity_frame, text="Quantité:", font=("Georgia", 15))
        self.en_quantityItem = ttk.Entry(quantity_frame, style="quantity.TEntry")

        # button widget
        bt_back = ttk.Button(
            self.tableItemWindow,
            text="Retour",
            style="back.TButton",
            command=self.tableItemWindow.destroy,
            width=15,
        )
        bt_confirm_selected = ttk.Button(
            self.tableItemWindow,
            text="Confirmer",
            style="confirm.TButton",
            command=self.insert_Item_into_invoice,
            width=15,
        )

        # position views table
        lb_title.grid(column=2, row=0, padx=10, pady=20)
        table_frame.grid(columnspan=5, row=1, sticky=cttk.NSEW, padx=20, pady=30)
        quantity_frame.grid(column=2, row=2, sticky=cttk.EW)
        self.tableItem.pack(side=cttk.LEFT, fill=cttk.BOTH, expand=True)
        scrollbar.pack(side=cttk.LEFT, fill=cttk.Y)

        # quantity widget position
        lb_quantity.pack(side=cttk.LEFT, fill=cttk.X, expand=True)
        self.en_quantityItem.pack(side=cttk.LEFT, fill=cttk.X, expand=True)

        # button position
        bt_back.grid(column=1, row=3, padx=20, pady=20)
        bt_confirm_selected.grid(column=3, row=3, padx=20, pady=20)

    def insert_Item_into_invoice(self):
        """Insert l'article choisit dans la facture"""
        tva_tare_int: int
        quantity: int
        try:
            item = self.get_selected_item()
            match item.tva_tare:
                case "21%":
                    tva_tare_int = 21
                case "12%":
                    tva_tare_int = 12
                case _:
                    tva_tare_int = 6

            quantity = int(self.en_quantityItem.get())
            self.table_invoice.insert(
                "",
                ttk.END,
                values=(
                    item.id_item,
                    item.name_item,
                    item.tva_tare,
                    item.htva_price,
                    round(
                        (item.htva_price * quantity)
                        + (item.htva_price * quantity / 100 * tva_tare_int),
                        2,
                    ),
                    quantity,
                ),
            )
            self.tableItemWindow.destroy()
        except AttributeError:
            windowView.Window.show_message_failure("Veuillez sélectionnez un élément!")

    def insert_data_in_tableItem(self):
        print(1)
        """Ajout chaque client dans la table"""
        items = self.controllerItem.load_data_items()
        tva_tare_int: int

        for item in items:
            match item.tva_tare:
                case "21%":
                    tva_tare_int = 21
                case "12%":
                    tva_tare_int = 12
                case _:
                    tva_tare_int = 6

            self.tableItem.insert(
                "",
                ttk.END,
                values=(
                    item.id_item,
                    item.name_item,
                    item.htva_price,
                    round(item.htva_price + (item.htva_price / 100 * tva_tare_int), 2),
                ),
            )

    def add_item(self):
        self.create_table_item()
        self.insert_data_in_tableItem()

    def delete_item(self):
        self.create_table_item()
        self.insert_item_data_of_invoice_in_the_table()

    def get_selected_item(self):
        """Récupère les données de l'article, sélectionnez"""
        for selected_item in self.tableItem.selection():
            select = self.tableItem.item(selected_item)
            item = select["values"]
            return self.controllerItem.load_data_item(item[0])

    def insert_item_data_of_invoice_in_the_table(self):
        # récupère les données de table invoice et les insert dans le table supprimer item
        pass

    @staticmethod
    def get_date() -> str:
        locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
        now = datetime.datetime.now()
        date = now.strftime("%d %B %Y")
        return str(date)

    def show_invoice(self):
        pass

    def create_pdf(self):
        invoice = pdf.PDF()
        invoice.add_page()
        invoice.add_invoice_header(1, self.get_date())
        invoice.add_invoice_client_and_company(
            "Adrien Mertens",
            "Zénith Computer",
            "Rue constant legrève 51",
            "Rue des battons 25",
            "1300 Limal",
            "1300 Wavre",
            "",
            "BE17.125.158.4125",
            "",
            "Zénith-computer@gmail.com",
            "",
            "010.25.69.35.84",
            124587,
            "BE56.2587.3695.2547",
        )
        invoice.add_invoice_items(
            [
                {
                    "numéroArticle": "1254",
                    "product": "Produit 1",
                    "tauxTva": "21%",
                    "quantity": 2,
                    "price": 10,
                    "total": 20,
                },
                {
                    "numéroArticle": "4578",
                    "product": "Produit 2",
                    "tauxTva": "12%",
                    "quantity": 1,
                    "price": 100,
                    "total": 100,
                },
            ]
        )

        invoice.create_pdf("test.pdf")

    def record_invoice(self):
        """enregistré les données de la facture dans la base de données"""

