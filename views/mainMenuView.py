import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk
import views.items.menuItemView as menuItem
import views.customer.menuCustomerView as menuCustomer
import views.invoices.menuInvoiceView as menuInvoice
import views.company.dataCompany as dataCompany
import controllers.zipcodeController as zipcodeController
import controllers.companyController as companyController
import models.zipcodeModel as zipcodeModel
import models.companyModel as companyModel


class MainMenu(ttk.Frame):
    def __init__(self, window):
        """constructeur"""
        # style frame
        ttk.Style().configure("frame.TFrame", background="#283747")
        # paramètre de la frame
        super().__init__(window, style="frame.TFrame")
        # position of the frame
        self.pack(side=cttk.LEFT, fill=cttk.Y)
        # creation du menu
        self.create_main_menu()
        # variable
        self.window = window

    def create_main_menu(self):
        """Création des widgets du menu principal"""
        # style of widgets
        ttk.Style().configure(
            "item.TButton",
            background="#96875A",
            bordercolor="#96875A",
            relief="flat",
            font=("Georgia", 15),
        )
        ttk.Style().configure(
            "customer.TButton",
            background="#6E9A3A",
            bordercolor="#6E9A3A",
            relief="flat",
            font=("Georgia", 15),
        )
        ttk.Style().configure(
            "invoices.TButton",
            background="#6E5A96",
            bordercolor="#6E5A96",
            relief="flat",
            font=("Georgia", 15),
        )
        ttk.Style().configure(
            "setting.TButton",
            background="#B17F35",
            bordercolor="#B17F35",
            relief="flat",
            font=("Georgia", 15),
        )
        ttk.Style().configure(
            "close.TButton",
            background="#C0392B",
            bordercolor="#C0392B",
            relief="flat",
            font=("Georgia", 15),
        )
        # widget label
        lb_tittle = ttk.Label(
            self,
            text="Menu Principal",
            font=("Georgia", 20),
            background="#283747",
        )
        # widget button
        self.bt_item = ttk.Button(
            self,
            text="Article",
            command=self.show_article,
            width=12,
            style="item.TButton",
        )
        self.bt_customer = ttk.Button(
            self,
            text="Client",
            command=self.do_show_customer,
            width=12,
            style="customer.TButton",
        )
        self.bt_invoice = ttk.Button(
            self,
            text="Facture",
            command=self.do_show_invoice,
            width=12,
            style="invoices.TButton",
        )
        self.bt_close = ttk.Button(
            self,
            text="Quitter",
            command=self.quit,
            width=12,
            style="close.TButton",
        )
        self.bt_myCompany = ttk.Button(
            self,
            text="Mon entreprise",
            width=12,
            style="setting.TButton",
            command=self.do_show_company,
        )
        # position widget
        lb_tittle.pack(side=cttk.TOP, pady=20, padx=10)
        self.bt_item.pack(side=cttk.TOP, pady=30, padx=10)
        self.bt_customer.pack(side=cttk.TOP, padx=10)
        self.bt_invoice.pack(side=cttk.TOP, pady=30, padx=10)
        self.bt_close.pack(side=cttk.BOTTOM, pady=30, padx=10)
        self.bt_myCompany.pack(side=cttk.BOTTOM, pady=30, padx=10)

    def show_article(self):
        """Lance le menu article"""
        # détruit le menu principal
        self.destroy()
        # affiche le menu article
        menuItem.MenuItem(self.window)

    def do_show_customer(self):
        """Lance le menu client"""
        self.destroy()
        # affiche le menu client
        menuCustomer.MenuCustomer(self.window).create_menu_customer()

    def do_show_invoice(self):
        """Lance la menu facture"""
        # détruit le menu principal
        self.destroy()
        # affiche le menu facture
        menuInvoice.MenuInvoice(self.window)

    def do_show_company(self):
        # Module MyCompany
        myCompany = dataCompany.DataCompany(self.window, self)
        myCompany.controllerZipcode = zipcodeController.ZipCodeController(
            zipcodeModel.ZipCodes()
        )
        myCompany.controllerCompany = companyController.CompanyController(
            companyModel.MyCompanys()
        )
        myCompany.create_data_company()
        self.state_bt_mainMenu("disabled")

    def state_bt_mainMenu(self, state):
        self.bt_customer.configure(state=state)
        self.bt_item.configure(state=state)
        self.bt_invoice.configure(state=state)
        self.bt_myCompany.configure(state=state)
        self.bt_close.configure(state=state)
