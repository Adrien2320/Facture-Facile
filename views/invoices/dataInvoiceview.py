import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk


class DataInvoice(ttk.Frame):
    table_invoice : ttk.Treeview
    def __init__(self, window):
        # paramètre de la frame
        super().__init__(window)
        # position de la frame
        self.pack(side=cttk.RIGHT, fill=cttk.BOTH, expand=True)
        # config du grid
        self.columnconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
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
        # create data client et entreprise
        self.create_dataInvoice()
        # set variable ttk customer
        self.set_variable_ttk_customer()
        # set variable ttk company
        self.set_variable_ttk_company()

    def create_dataInvoice(self):
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
        table_invoice_frame.columnconfigure(0,weight=1)
        table_invoice_frame.rowconfigure(1,weight=1)
        # position frame
        top_frame.grid(row=0,column=0,sticky=cttk.EW,pady=10,padx=10)
        bottom_frame.grid(row=1,column=0,sticky=cttk.NSEW,pady=10,padx=10)
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
        table_invoice_frame.pack(side=cttk.TOP,
            fill=cttk.BOTH,
            expand=True,
            padx=10,
            pady=10,)
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
        lb_title_item =ttk.Label(table_invoice_frame, text="Article",anchor=cttk.CENTER,style="data.TLabel")
        scrollbar = ttk.Scrollbar(table_invoice_frame, orient=cttk.VERTICAL)
        self.table_invoice = ttk.Treeview(
            table_invoice_frame,
            columns=["itemCode", "item", "tvaRate", "priceHtva","quantity"],
            yscrollcommand=scrollbar.set,
            selectmode=cttk.NONE,
            style="item.Treeview",
        )
        # config the scrollbar
        scrollbar.config(command=self.table_invoice.yview)
        # column configure
        self.table_invoice.column("#0", anchor=cttk.W, stretch=False, width=0, minwidth=0)
        self.table_invoice.column("itemCode",anchor=cttk.W, stretch=False,)
        self.table_invoice.column("item",anchor=cttk.W, stretch=True,)
        self.table_invoice.column("tvaRate",anchor=cttk.W, stretch=True,)
        self.table_invoice.column("priceHtva",anchor=cttk.W, stretch=True,)
        self.table_invoice.column("quantity",anchor=cttk.W, stretch=True,)
        # heading column
        self.table_invoice.heading("#0", anchor=cttk.W)
        self.table_invoice.heading("itemCode", text="Numéro Article", anchor=cttk.W)
        self.table_invoice.heading("item", text="Produit", anchor=cttk.W)
        self.table_invoice.heading("tvaRate", text="Taux Tva", anchor=cttk.W)
        self.table_invoice.heading("priceHtva", text="Prix Htva", anchor=cttk.W)
        self.table_invoice.heading("quantity",text="Quantité")
        # position views table
        lb_title_item.grid(columnspan=2,row=0,sticky=cttk.EW)
        self.table_invoice.grid(column=0,row=1,sticky=cttk.NSEW)
        scrollbar.grid(column=1,row=1,sticky=cttk.NS)


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
