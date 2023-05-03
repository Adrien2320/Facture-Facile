import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk
import views.customer.menuCustomerView as menuCustomer
import views.windowView as windowView


class DataCustomer(ttk.Frame):
    bt_confirm_customer: ttk.Button
    table: ttk.Treeview
    bt_confirm_selected: ttk.Button

    def __init__(self, window, menu_customer):
        """Constructeur"""
        # style Frame
        ttk.Style().configure("frame.TFrame", background="#283747")
        # paramètre de la frame
        super().__init__(window, style="frame.TFrame")
        # position de la frame
        self.pack(side=cttk.RIGHT, fill=cttk.BOTH, expand=True)
        # variable
        self.window = window
        self.menu_customer = menu_customer
        self.postal_code = self.insert_postal_code()
        # variable ttk
        self.var_id = ttk.IntVar()
        self.var_name = ttk.StringVar()
        self.var_first_name = ttk.StringVar()
        self.var_address = ttk.StringVar()
        self.var_postal_code = ttk.StringVar()
        self.var_tva = ttk.StringVar()
        self.var_type = ttk.StringVar()
        self.var_email = ttk.StringVar()
        self.var_phone = ttk.StringVar()

    def insert_postal_code(self):
        """Récupère les localités et code postal dans la base de données. Ensuite les retourne sous une liste"""
        result = self.controllerZipcode.loads_zipcode()
        print(result)

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
        en_tva = ttk.Entry(top_frame, font=("Georgia", 15), textvariable=self.var_tva)
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
        cbb_postal_code = ttk.Combobox(
            top_frame,
            font=("Georgia", 15),
            textvariable=self.var_postal_code,
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
        cbb_postal_code.grid(column=1, row=4, sticky=cttk.EW, pady=10, padx=20)

    def back_customer_menu(self):
        """Supprime la frame data_customer et débloque le menu customer"""
        self.destroy()
        # vider les variables ttk
        menuCustomer.MenuCustomer.state_customer_menu(self.menu_customer, "normal")

    def show_new_customer(self):
        """Affiche le formulaire pour créer un nouveau client"""
        self.create_data_customer()
        self.bt_confirm_customer["command"] = self.new_customer

    def new_customer(self):
        """Créer un nouveau client"""
        # envoyer les données vers le controller pour créer client
        menuCustomer.MenuCustomer.state_customer_menu(self.menu_customer, "normal")
        self.destroy()

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
