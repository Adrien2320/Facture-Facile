import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk
import views.windowView as windowView
from models.zipcodeModel import ZipCode


class DataInvoice(ttk.Frame):
    tableCustomer: ttk.Treeview
    tableWindow: ttk.Toplevel

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
            columns=["itemCode", "item", "tvaRate", "priceHtva", "quantity"],
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
        self.table_invoice.heading("priceHtva", text="Prix Htva", anchor=cttk.W)
        self.table_invoice.heading("quantity", text="Quantité")

        # position views table
        lb_title_item.grid(columnspan=2, row=0, sticky=cttk.EW)
        self.table_invoice.grid(column=0, row=1, sticky=cttk.NSEW)
        scrollbar.grid(column=1, row=1, sticky=cttk.NS)

    def create_table_customer(self):
        """Affiche tous les clients dans une treeview"""
        # create toplevel
        self.tableWindow = ttk.Toplevel()
        self.tableWindow.minsize(480, 480)

        self.tableWindow.columnconfigure(2, weight=1)
        self.tableWindow.columnconfigure(1, weight=1)
        self.tableWindow.columnconfigure(3, weight=1)
        self.tableWindow.rowconfigure(1, weight=1)

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
            self.tableWindow,
            text="Recherche Client",
            anchor=cttk.CENTER,
            font=("Georgia", 20),
        )

        # frame
        table_frame = ttk.Frame(self.tableWindow)

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
            self.tableWindow,
            text="Retour",
            style="back.TButton",
            command=self.tableWindow.destroy,
            width=15,
        )
        bt_confirm_selected = ttk.Button(
            self.tableWindow,
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
        self.var_full_name_customer.set(f"Nom: {name_customer}")
        self.var_address_customer.set(f"Adresse: {address_customer}")
        self.var_postal_code_customer.set(f"Code Postale: {postalCode_customer}")
        self.var_number_tva_customer.set(f"TVA: {numberTva_customer}")
        self.var_phone_customer.set(f"Téléphone: {numberPhone_customer}")

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
        self.var_name_company.set(f"Nom:{name_company}")
        self.var_address_company.set(f"Adresse:{address_company}")
        self.var_postal_code_company.set(f"Code Postale:{postalCode_company}")
        self.var_number_tva_company.set(f"TVA:{numberTva_company}")
        self.var_email_company.set(f"Email:{email_company}")
        self.var_phone_company.set(f"Téléphone:{numberPhone_company}")
        self.var_account_number_company.set(f"Numéro De Compte:{accountNumber_company}")

    def insert_data_in_table(self):
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

    def start_add_client(self):
        self.create_table_customer()
        self.insert_data_in_table()

    def insert_customer_into_invoice(self):
        try:
            customer = self.get_selected_customer()
            print(customer.postalCode_customer)
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
            self.tableWindow.destroy()
        except AttributeError:
            windowView.Window.show_message_failure("Veuillez sélectionnez un élément!")

    def get_selected_customer(self):
        """Récupère les données de l'article, sélectionnez"""
        for selected_item in self.tableCustomer.selection():
            select = self.tableCustomer.item(selected_item)
            customer = select["values"]
            return self.controllerCustomer.load_customer(customer[0])

    def get_postalCode_customer(self, index_zipCode) -> ZipCode:
        """Récupère le code postal et la localité et la retourne sous un string"""
        return self.controllerZipcode.load_zipcode(index_zipCode)



