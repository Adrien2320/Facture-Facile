import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk
import views.windowView as windowView
import models.companyModel as companyModel


class DataCompany(ttk.Frame):
    cbb_postal_code: ttk.Combobox
    oldName : str

    def __init__(self, window, mainMenu):
        """Constructeur"""
        # style Frame
        ttk.Style().configure("frame.TFrame", background="#283747")
        # paramètre de la frame
        super().__init__(window, style="frame.TFrame")
        # position de la frame
        self.pack(side=cttk.RIGHT, fill=cttk.BOTH, expand=True)
        # variable
        self.window = window
        self.mainMenu = mainMenu
        self.emptyData = False

        # variable ttk
        self.var_name = ttk.StringVar()
        self.var_address = ttk.StringVar()
        self.var_postal_code = ttk.IntVar()
        self.var_number_tva = ttk.StringVar()
        self.var_email = ttk.StringVar()
        self.var_phone = ttk.StringVar()
        self.var_accountNumber = ttk.StringVar()
        self.codePostalTemp = 0

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
    def controllerCompany(self):
        """Créer le paramètre controller du customer"""
        try:
            return self._controllerCompany
        except AttributeError:
            windowView.Window.show_message_error("Pas de controlleur pour company")
            self.quit()

    @controllerCompany.setter
    def controllerCompany(self, value):
        """Assigne le paramètre controller du customer"""
        self._controllerCompany = value

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
        name_company: str,
        address_company: str,
        postalCode_company: int,
        number_tva_company: str,
        email_company: str,
        phone_company: str,
        accountNumber: str,
    ):
        """Assigne les variables ttk"""
        self.var_name.set(name_company)
        self.var_address.set(address_company)
        self.var_postal_code.set(postalCode_company)
        self.var_number_tva.set(number_tva_company)
        self.var_email.set(email_company)
        self.var_phone.set(phone_company)
        self.var_accountNumber.set(accountNumber)

    def clean_variable_ttk(
        self
    ):
        """Assigne les variables ttk"""
        self.var_name.set("")
        self.var_address.set("")
        self.var_postal_code.set(int())
        self.var_number_tva.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_accountNumber.set("")

    def create_data_company(self):
        """ créer le formulaire pour mon entreprise"""
        # Préremplis le formulaire
        self.check_data_in_table_and_return()
        self.postal_code = self.insert_postal_code()
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
        self.bt_confirm_company = ttk.Button(
            bottom_frame,
            text="Enregistrer",
            style="confirm.TButton",
            width=15,
            command=self.confirm_company,
            state="disabled"
        )
        self.bt_back = ttk.Button(
            bottom_frame,
            text="Retour",
            style="back.TButton",
            width=15,
            command=self.back_mainMenu,
        )
        # widget label
        lb_name = ttk.Label(top_frame, text="Nom :", font=("Georgia", 15))
        lb_address = ttk.Label(top_frame, text="Adresse :", font=("Georgia", 15))
        lb_postal_code = ttk.Label(
            top_frame, text="code postal :", font=("Georgia", 15)
        )
        lb_tva = ttk.Label(top_frame, text="Numéro de tva :", font=("Georgia", 15))
        lb_email = ttk.Label(top_frame, text="Email :", font=("Georgia", 15))
        lb_phone = ttk.Label(top_frame, text="Téléphone :", font=("Georgia", 15))
        lb_accountNumber = ttk.Label(
            top_frame, text="Numéro de compte :", font=("Georgia", 15)
        )
        # widget Entry
        en_name = ttk.Entry(top_frame, font=("Georgia", 15), textvariable=self.var_name)
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
        en_accountNumber = ttk.Entry(
            top_frame, font=("Georgia", 15), textvariable=self.var_accountNumber
        )
        # widget combobox
        self.cbb_postal_code = ttk.Combobox(
            top_frame,
            font=("Georgia", 15),
            values=self.postal_code,
            state="readonly",
        )
        # position button
        self.bt_confirm_company.pack(side=cttk.RIGHT, padx=50)
        self.bt_back.pack(side=cttk.LEFT, padx=50)
        # position Label
        lb_name.grid(column=0, row=1, pady=10)
        lb_address.grid(column=0, row=2, pady=10)
        lb_postal_code.grid(column=0, row=3, pady=10)
        lb_tva.grid(column=0, row=4, pady=10, padx=50)
        lb_email.grid(column=0, row=7, pady=10)
        lb_phone.grid(column=0, row=8, pady=10)
        lb_accountNumber.grid(column=0, row=5, pady=10)
        # position entry
        en_name.grid(column=1, row=1, sticky=cttk.EW, pady=10, padx=20)
        en_address.grid(column=1, row=2, sticky=cttk.EW, pady=10, padx=20)
        en_tva.grid(column=1, row=4, sticky=cttk.EW, pady=10, padx=20)
        en_email.grid(column=1, row=7, sticky=cttk.EW, pady=10, padx=20)
        en_phone.grid(column=1, row=8, sticky=cttk.EW, pady=10, padx=20)
        en_accountNumber.grid(column=1, row=5, sticky=cttk.EW, pady=10, padx=20)
        # position combobox
        self.cbb_postal_code.grid(column=1, row=3, sticky=cttk.EW, pady=10, padx=20)
        if not self.emptyData:
            self.set_cbb_postal_code(self.codePostalTemp)
        # check the contents of entry
        en_name.bind("<FocusOut>", self.check_if_all_entry_are_filled)
        en_address.bind("<FocusOut>", self.check_if_all_entry_are_filled)
        self.cbb_postal_code.bind("<FocusOut>", self.check_if_all_entry_are_filled)
        en_tva.bind("<FocusOut>", self.check_if_all_entry_are_filled)
        en_accountNumber.bind("<FocusOut>", self.check_if_all_entry_are_filled)
        en_email.bind("<FocusOut>", self.check_if_all_entry_are_filled)
        en_phone.bind("<FocusOut>", self.check_if_all_entry_are_filled)

    def confirm_company(self):
        """ Enregistre les données. Si elle existe déjà, elle va modifier au lieu de les crées"""
        self.clean_variable_ttk()
        if self.emptyData:
            self.controllerCompany.add_company(str(self.var_name.get()),str(self.var_address.get()),int(self.cbb_postal_code.current()+1),str(self.var_phone.get()),str(self.var_email.get()),str(self.var_number_tva.get()),str(self.var_accountNumber.get()))
            self.clean_variable_ttk()
        else:
            self.controllerCompany.modif_company(str(self.var_name.get()),str(self.var_address.get()),int(self.cbb_postal_code.current()+1),str(self.var_phone.get()),str(self.var_email.get()),str(self.var_number_tva.get()),str(self.var_accountNumber.get()),self.oldName)
            self.clean_variable_ttk()

    def back_mainMenu(self):
        """ Débloque le menu et supprime le formulaire mon entreprise"""
        self.destroy()
        self.mainMenu.state_bt_mainMenu("normal")

    def check_data_in_table_and_return(self):
        """vérifie si, l'utilisateur à déjà enregistré des données si oui il les retourn"""
        result = self.controllerCompany.load_company()
        if result == []:
            self.emptyData = True
        else:
            self.emptyData = False
            element: companyModel.MyCompany = result[0]
            self.oldName = element.name
            self.set_variable_ttk(
                element.name,
                element.address,
                element.postalCode,
                element.tva,
                element.email,
                element.phoneNumber,
                element.accountNumber,
            )
            self.codePostalTemp = element.postalCode


    def set_cbb_postal_code(self, indexPostalCode:int):
        self.cbb_postal_code.current(indexPostalCode-1)

    def check_if_all_entry_are_filled(self,*args):
        """Vérifie si l'utilisateur a rempli toutes les entrées importantes"""
        if self.var_name.get() and self.var_address.get() and self.cbb_postal_code.get() and self.var_number_tva.get() and self.var_accountNumber.get() and self.var_email.get() and self.var_phone.get():
            self.bt_confirm_company.configure(state="normal")
        else:
            self.bt_confirm_company.configure(state="disabled")