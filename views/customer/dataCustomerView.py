import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk
import views.customer.menuCustomerView as menuCustomer
import views.windowView as windowView
from models.customerModel import Customer
import tkinter as tk


class DataCustomer(ttk.Frame):
    bt_confirm_customer: ttk.Button
    table: ttk.Treeview
    bt_confirm_selected: ttk.Button
    cbb_postal_code: ttk.Combobox

    def __init__(self, window, menu_customer):
        """Constructeur"""
        # style Frame
        ttk.Style().configure("myFrame.TFrame", background="#283747")
        # paramètre de la frame
        super().__init__(window, style="myFrame.TFrame")
        # position de la frame
        self.pack(side=cttk.RIGHT, fill=cttk.BOTH, expand=True)
        # variable
        self.window = window
        self.menu_customer = menu_customer
        self.varBtConfirm_exist =False
        self.postal_code = self.insert_postal_code()
        # variable ttk
        self.var_idCustomer = ttk.IntVar()
        self.var_name = ttk.StringVar()
        self.var_first_name = ttk.StringVar()
        self.var_address = ttk.StringVar()
        self.var_postal_code = ttk.IntVar()
        self.var_number_tva = ttk.StringVar()
        self.var_type = ttk.StringVar()
        self.var_email = ttk.StringVar()
        self.var_phone = ttk.StringVar()

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

    def insert_postal_code(self) -> list:
        """Récupère les localités et code postal dans la base de données. Ensuite les retourne sous une liste"""
        result = self.controllerZipcode.loads_zipcode()
        list_zipcode: list = []
        for zipcode in result:
            list_zipcode.append(
                f"{zipcode.codePostal_zipcode} {zipcode.locality_zipcode}"
            )
        return list_zipcode

    def set_variable_ttk(
        self,
        id_customer: int,
        name_customer: str,
        first_name_customer: str,
        address_customer: str,
        postal_code_customer: int,
        number_tva_customer: str,
        type_customer: str,
        email_customer: str,
        phone_customer: str,
    ):
        """Assigne les variables ttk"""
        self.var_idCustomer.set(id_customer)
        self.var_name.set(name_customer)
        self.var_first_name.set(first_name_customer)
        self.var_address.set(address_customer)
        self.var_postal_code.set(postal_code_customer)
        self.var_number_tva.set(number_tva_customer)
        self.var_type.set(type_customer)
        self.var_email.set(email_customer)
        self.var_phone.set(phone_customer)

    def clean_variable_ttk(self):
        """Nettoie les variables ttk"""
        self.var_idCustomer.set(int())
        self.var_name.set("")
        self.var_first_name.set("")
        self.var_address.set("")
        self.var_postal_code.set(int())
        self.var_number_tva.set("")
        self.var_type.set("")
        self.var_email.set("")
        self.var_phone.set("")

    def clean_frame(self):
        """vide la frame"""
        for widget in self.winfo_children():
            widget.destroy()

    def create_data_customer(self):
        """Création des widgets pour le formulaire client"""
        # variable
        types = ["Particulier", "Professionnel"]
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

        # sépare le frame en plusieurs parties
        top_frame = ttk.Frame(self)
        bottom_frame = ttk.Frame(self)
        # config of columns and rows
        top_frame.columnconfigure(1, weight=2)
        top_frame.rowconfigure(0, weight=1)
        top_frame.rowconfigure(9, weight=1)
        # position frame
        top_frame.pack(side=cttk.TOP, expand=True, fill=cttk.BOTH)
        bottom_frame.pack(side=cttk.BOTTOM, expand=True, fill=cttk.BOTH)
        # widget button
        self.bt_confirm_customer = ttk.Button(
            bottom_frame,
            text="Confirmer",
            style="confirm.TButton",
            width=15,
            state="disabled"
        )
        bt_back = ttk.Button(
            bottom_frame,
            text="Retour",
            style="back.TButton",
            width=15,
            command=self.back_customer_menu,
        )
        # widget label
        lb_name = ttk.Label(top_frame, text="Nom :", font=("Georgia", 15))
        lb_first_name = ttk.Label(top_frame, text="Prénom :", font=("Georgia", 15))
        lb_address = ttk.Label(top_frame, text="Adresse :", font=("Georgia", 15))
        lb_postal_code = ttk.Label(
            top_frame, text="code postal :", font=("Georgia", 15)
        )
        lb_tva = ttk.Label(top_frame, text="Numéro de tva :", font=("Georgia", 15))
        lb_type = ttk.Label(top_frame, text="Type :", font=("Georgia", 15))
        lb_email = ttk.Label(top_frame, text="Email :", font=("Georgia", 15))
        lb_phone = ttk.Label(top_frame, text="Téléphone :", font=("Georgia", 15))
        # widget Entry
        en_name = ttk.Entry(top_frame, font=("Georgia", 15), textvariable=self.var_name)
        en_first_name = ttk.Entry(
            top_frame, font=("Georgia", 15), textvariable=self.var_first_name
        )
        en_address = ttk.Entry(
            top_frame, font=("Georgia", 15), textvariable=self.var_address
        )
        en_tva = ttk.Entry(
            top_frame, font=("Georgia", 15), textvariable=self.var_number_tva
        )
        en_email = ttk.Entry(
            top_frame, font=("Georgia", 15), textvariable=self.var_email
        )
        en_phone = ttk.Entry(
            top_frame, font=("Georgia", 15), textvariable=self.var_phone
        )
        # widget combobox
        cbb_type = ttk.Combobox(
            top_frame,
            font=("Georgia", 15),
            textvariable=self.var_type,
            values=types,
            state="readonly",
        )
        self.cbb_postal_code = ttk.Combobox(
            top_frame,
            font=("Georgia", 15),
            values=self.postal_code,
            state="readonly",
        )
        # position button
        self.bt_confirm_customer.pack(side=cttk.RIGHT, padx=50)
        bt_back.pack(side=cttk.LEFT, padx=50)
        # position Label
        lb_name.grid(column=0, row=1, pady=10)
        lb_first_name.grid(column=0, row=2, pady=10)
        lb_address.grid(column=0, row=3, pady=10)
        lb_postal_code.grid(column=0, row=4, pady=10)
        lb_tva.grid(column=0, row=5, pady=10, padx=50)
        lb_type.grid(column=0, row=6, pady=10)
        lb_email.grid(column=0, row=7, pady=10)
        lb_phone.grid(column=0, row=8, pady=10)
        # position entry
        en_name.grid(column=1, row=1, sticky=cttk.EW, pady=10, padx=20)
        en_first_name.grid(column=1, row=2, sticky=cttk.EW, pady=10, padx=20)
        en_address.grid(column=1, row=3, sticky=cttk.EW, pady=10, padx=20)
        en_tva.grid(column=1, row=5, sticky=cttk.EW, pady=10, padx=20)
        en_email.grid(column=1, row=7, sticky=cttk.EW, pady=10, padx=20)
        en_phone.grid(column=1, row=8, sticky=cttk.EW, pady=10, padx=20)
        # position combobox
        cbb_type.grid(column=1, row=6, sticky=cttk.EW, pady=10, padx=20)
        self.cbb_postal_code.grid(column=1, row=4, sticky=cttk.EW, pady=10, padx=20)
        # check the contents of entry
        if self.varBtConfirm_exist:
            en_name.bind("<FocusOut>", self.check_if_all_entry_are_filled)
            en_first_name.bind("<FocusOut>", self.check_if_all_entry_are_filled)
            en_address.bind("<FocusOut>", self.check_if_all_entry_are_filled)
            self.cbb_postal_code.bind("<FocusOut>", self.check_if_all_entry_are_filled)
            en_tva.bind("<FocusOut>", self.check_if_all_entry_are_filled)


    def create_table_customer(self):
        """Affiche tous les clients dans une treeview"""
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
        ttk.Style().configure("title.TLabel", background="#283747")

        # Frame
        bottom_frame = ttk.Frame(self)
        top_frame = ttk.Frame(self)
        table_frame = ttk.Frame(top_frame)

        # title
        lb_title = ttk.Label(top_frame, text="Liste de sélection de client", style="title.TLabel",
                             font=("Georgia", 20), anchor=cttk.CENTER)

        # position frame
        bottom_frame.pack(side=cttk.BOTTOM, fill=cttk.BOTH, expand=True)
        bottom_frame.columnconfigure(0, weight=1)
        bottom_frame.columnconfigure(2, weight=1)
        bottom_frame.columnconfigure(4, weight=1)
        bottom_frame.rowconfigure(0, weight=1)
        bottom_frame.rowconfigure(2, weight=1)

        top_frame.pack(side=cttk.TOP, fill=cttk.BOTH, expand=True)
        lb_title.pack(side=cttk.TOP, fill=cttk.X)
        table_frame.pack(pady=20, padx=20, fill=cttk.BOTH, expand=True)

        # views table
        scrollbar = ttk.Scrollbar(table_frame, orient=cttk.VERTICAL)
        self.table = ttk.Treeview(
            table_frame,
            columns=["id", "name", "firstName", "address"],
            yscrollcommand=scrollbar.set,
            selectmode=cttk.BROWSE,
            style="my.Treeview",
        )

        # config the scrollbar
        scrollbar.config(command=self.table.yview)

        # format column
        self.table.column("#0", anchor=cttk.W, stretch=False, width=0, minwidth=0)
        self.table.column("id", anchor=cttk.W, stretch=False, width=200)
        self.table.column("name", anchor=cttk.W, stretch=True, width=200)
        self.table.column("firstName", anchor=cttk.W, stretch=True, width=200)
        self.table.column("address", anchor=cttk.W, stretch=True, width=200)

        # heading column
        self.table.heading("#0", anchor=cttk.W)
        self.table.heading("id", text="Numéro Client", anchor=cttk.W)
        self.table.heading("name", text="Nom", anchor=cttk.W)
        self.table.heading("firstName", text="Prénom", anchor=cttk.W)
        self.table.heading("address", text="Adresse", anchor=cttk.W)

        # position views table
        self.table.pack(side=cttk.LEFT, fill=cttk.BOTH, expand=True)
        self.table.bind("<<TreeviewSelect>>",self.check_treeview_select)
        scrollbar.pack(side=cttk.LEFT, fill=cttk.Y, padx=5)

        # button widget
        bt_back = ttk.Button(
            bottom_frame,
            text="Retour",
            style="back.TButton",
            command=self.back_customer_menu,
            width=15,
        )
        self.bt_confirm_selected = ttk.Button(
            bottom_frame,
            text="Confirmer",
            style="confirm.TButton",
            width=15,
            state="disabled"
        )
        # label widget
        lb_top = tk.Label(bottom_frame, height=5)
        lb_bottom = tk.Label(bottom_frame, height=5)

        # button position
        lb_top.grid(columnspan=5, row=0, sticky=cttk.NS)
        bt_back.grid(column=1,row=1,sticky=cttk.EW)
        self.bt_confirm_selected.grid(column=3,row=1,sticky=cttk.EW)
        lb_bottom.grid(columnspan=5, row=2, sticky=cttk.NS)

    def insert_customer_in_table(self):
        """Ajout chaque client dans la table"""
        customers = self.controllerCustomer.load_customers()

        for customer in customers:
            self.table.insert(
                "",
                ttk.END,
                values=(
                    customer.id_customer,
                    customer.name_customer,
                    customer.first_name,
                    customer.address_customer,
                ),
            )

    def back_customer_menu(self):
        """Supprime la frame data_customer et débloque le menu customer"""
        self.destroy()
        # vider les variables ttk
        menuCustomer.MenuCustomer.state_customer_menu(self.menu_customer, "normal")

    def show_new_customer(self):
        """Affiche le formulaire pour créer un nouveau client"""
        self.varBtConfirm_exist = True
        self.create_data_customer()
        self.bt_confirm_customer["command"] = self.new_customer

    def new_customer(self):
        """Créer un nouveau client"""
        self.controllerCustomer.new_customer(
            str(self.var_name.get()),
            str(self.var_first_name.get()),
            str(self.var_address.get()),
            int(self.cbb_postal_code.current() + 1),
            str(self.var_type.get()),
            str(self.var_number_tva.get()),
            str(self.var_email.get()),
            str(self.var_phone.get()),
        )
        menuCustomer.MenuCustomer.state_customer_menu(self.menu_customer, "normal")
        self.clean_variable_ttk()
        self.destroy()

    def show_search_customer(self):
        """Affiche la table de client pour sélectionner le client à rechercher"""
        self.create_table_customer()
        self.insert_customer_in_table()
        self.bt_confirm_selected["command"] = self.set_search_customer

    def set_search_customer(self):
        """Insert les données récolté dans le formulaire de recherche d'un client"""
        try:
            customer = self.get_selected()
            self.set_variable_ttk(
                customer.id_customer,
                customer.name_customer,
                customer.first_name,
                customer.address_customer,
                customer.postalCode_customer,
                customer.numberTva_customer,
                customer.type_customer,
                customer.email_customer,
                customer.phone_customer,
            )
            self.clean_frame()
            self.create_data_customer()
            self.set_cbb_postal_code(customer.postalCode_customer)
            self.bt_confirm_customer.destroy()
        except AttributeError:
            windowView.Window.show_message_failure("Veuillez sélectionnez un élément!")
            menuCustomer.MenuCustomer.state_customer_menu(self.menu_customer, "normal")

    def get_selected(self) -> Customer:
        """Récupère les données de l'article, sélectionnez"""
        for selected_item in self.table.selection():
            select = self.table.item(selected_item)
            customer = select["values"]
            return self.controllerCustomer.load_customer(customer[0])

    def set_cbb_postal_code(self, indexCustomer):
        self.cbb_postal_code.current(int(indexCustomer) - 1)

    def show_delete_customer(self):
        """Affiche la table pour sélectionner un client à supprimer"""
        self.create_table_customer()
        self.insert_customer_in_table()
        self.bt_confirm_selected["command"] = self.delete_item

    def delete_item(self):
        """Supprime un client"""
        try:
            customer = self.get_selected()
            self.controllerCustomer.delete_item(customer.id_customer)
            self.destroy()
            menuCustomer.MenuCustomer.state_customer_menu(self.menu_customer, "normal")
        except AttributeError:
            windowView.Window.show_message_failure("Veuillez sélectionnez un élément!")
            menuCustomer.MenuCustomer.state_customer_menu(self.menu_customer, "normal")

    def show_modif_customer(self):
        """Affiche la table pour sélectionner le client à modifier"""
        self.create_table_customer()
        self.varBtConfirm_exist = True
        self.insert_customer_in_table()
        self.bt_confirm_selected["command"] = self.set_modif_customer

    def set_modif_customer(self):
        """Insert les données dans le formulaire pour modifier un client"""
        try:
            customer = self.get_selected()
            self.set_variable_ttk(
                customer.id_customer,
                customer.name_customer,
                customer.first_name,
                customer.address_customer,
                customer.postalCode_customer,
                customer.numberTva_customer,
                customer.type_customer,
                customer.email_customer,
                customer.phone_customer,
            )
            self.clean_frame()
            self.varBtConfirm_exist = True
            self.create_data_customer()
            self.set_cbb_postal_code(customer.postalCode_customer)
            self.bt_confirm_customer["command"] = self.modif_customer
        except AttributeError:
            windowView.Window.show_message_failure("Veuillez sélectionnez un élément!")
            menuCustomer.MenuCustomer.state_customer_menu(self.menu_customer, "normal")

    def modif_customer(self):
        """Modifie un client"""
        self.controllerCustomer.modif_item(
            int(self.var_idCustomer.get()),
            str(self.var_name.get()),
            str(self.var_first_name.get()),
            str(self.var_address.get()),
            int(self.cbb_postal_code.current() + 1),
            str(self.var_type.get()),
            str(self.var_number_tva.get()),
            str(self.var_email.get()),
            str(self.var_phone.get()),
        )
        self.destroy()
        menuCustomer.MenuCustomer.state_customer_menu(self.menu_customer, "normal")

    def check_if_all_entry_are_filled(self, *args):
        """Vérifie si l'utilisateur a rempli toutes les entrées selon le type de client"""
        if self.var_type.get() == "Professionnel":
            if self.var_name.get() and self.var_address.get() and self.cbb_postal_code.get() and self.var_number_tva.get():
                self.bt_confirm_customer.configure(state="normal")
            else:
                self.bt_confirm_customer.configure(state="disabled")
        elif self.var_type.get() == "Particulier":
            if self.var_first_name.get() and self.var_name.get() and self.var_address.get() and self.cbb_postal_code.get():
                self.bt_confirm_customer.configure(state="normal")
            else:
                self.bt_confirm_customer.configure(state="disabled")

    def check_treeview_select(self, event):
        """ Vérifie si l'utilisateur à sélectionner un élément  """
        selected_item = self.table.selection()
        if selected_item:
            self.bt_confirm_selected.configure(state="normal")
        else:
            self.bt_confirm_selected.configure(state="disabled")

