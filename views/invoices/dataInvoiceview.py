import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk


class DataInvoice(ttk.Frame):
    def __init__(self, window):
        # paramètre de la frame
        super().__init__(window)
        # position de la frame
        self.pack(side=cttk.RIGHT, fill=cttk.BOTH, expand=True)
        # variable ttk customer
        self.id_customer: int
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
        # create widget
        self.create_dataInvoice()
        # set variable ttk customer
        self.set_variable_ttk_customer()
        # set variable ttk company
        self.set_variable_ttk_company()

    def create_dataInvoice(self):
        # style
        ttk.Style().configure("data.TFrame", background="#283747")
        ttk.Style().configure("data.TLabel", background="#283747",font=("Georgia", 15))

        # frame
        top_frame = ttk.Frame(self)
        bottom_frame = ttk.Frame(self)
        customer_frame = ttk.Frame(top_frame, style="data.TFrame")
        my_company_frame = ttk.Frame(top_frame, style="data.TFrame")
        # position frame
        top_frame.pack(
            side=cttk.TOP,
            fill=cttk.X,
            expand=True,
            padx=10,
            pady=10,
        )
        bottom_frame.pack(
            side=cttk.BOTTOM,
            fill=cttk.BOTH,
            expand=True,
            padx=10,
            pady=10,
        )
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

    def set_variable_ttk_customer(self):
        self.var_full_name_customer.set("Nom: ")
        self.var_address_customer.set("Adresse: ")
        self.var_postal_code_customer.set("Code Postale: ")
        self.var_number_tva_customer.set("TVA: ")
        self.var_phone_customer.set("Téléphone:")

    def set_variable_ttk_company(self):
        self.var_name_company.set("Nom: ")
        self.var_address_company.set("Adresse:")
        self.var_postal_code_company.set("Code Postale:")
        self.var_number_tva_company.set("TVA: ")
        self.var_email_company.set("Email: ")
        self.var_phone_company.set("Téléphone: ")
        self.var_account_number_company.set("Numéro De Compte: ")
