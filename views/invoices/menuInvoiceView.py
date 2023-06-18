import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk
import views.mainMenuView as mainMenu
import views.invoices.dataInvoiceView as invoiceView
import controllers.customerController as customerController
import models.customerModel as customerModel
import controllers.zipcodeController as zipCodeController
import models.zipcodeModel as zipCodeModel
import controllers.itemController as itemController
import models.itemModel as itemModel
import controllers.invoiceController as invoiceController
import models.invoiceModel as invoiceModel
import controllers.itemInvoiceController as itemInvoiceController
import models.itemInvoiceModel as itemInvoiceModel
import controllers.companyController as companyController
import models.companyModel as companyModel


class MenuInvoice(ttk.Frame):
    bt_delete_customer: ttk.Button

    def __init__(self, window):
        # style frame
        ttk.Style().configure("frame.TFrame", background="#283747")
        # paramètre de la frame
        super().__init__(window, style="frame.TFrame")
        # position de la frame
        self.pack(side=cttk.LEFT, fill=cttk.Y)
        # variable
        self.window = window
        # creation du menu
        self.create_menu()
        # assign of dataInvoice
        self.data_invoice = invoiceView.DataInvoice(self.window)
        self.data_invoice.controllerCustomer = customerController.CustomerController(
            customerModel.Customers()
        )
        self.data_invoice.controllerZipcode = zipCodeController.ZipCodeController(
            zipCodeModel.ZipCodes()
        )
        self.data_invoice.controllerItem = itemController.ItemController(
            itemModel.Data()
        )
        self.data_invoice.controllerInvoice = invoiceController.InvoiceController(
            invoiceModel.Invoices()
        )
        self.data_invoice.controllerItemInvoice = (
            itemInvoiceController.ItemInvoiceController(itemInvoiceModel.ItemInvoices())
        )
        self.data_invoice.controllerCompany = companyController.CompanyController(
            companyModel.MyCompanys()
        )
        self.data_invoice.create_dataInvoice()

    def create_menu(self):
        """Création des widgets du menu facture"""

        # style of widgets
        ttk.Style().configure("under.TFrame", background="#283747")
        ttk.Style().configure(
            "customer.TButton",
            background="#96875A",
            bordercolor="#96875A",
            relief="flat",
            font=("Georgia", 15),
        )
        ttk.Style().configure(
            "item.TButton",
            background="#6E5A96",
            bordercolor="#6E5A96",
            relief="flat",
            font=("Georgia", 15),
        )
        ttk.Style().configure(
            "main.TButton",
            background="#C0392B",
            bordercolor="#C0392B",
            relief="flat",
            font=("Georgia", 15),
        )
        ttk.Style().configure(
            "test.TButton",
            background="#2F818B",
            bordercolor="#2F818B",
            relief="flat",
            font=("Georgia", 15),
        )
        ttk.Style().configure(
            "general.TLabel",
            background="#283747",
            bordercolor="#283747",
            relief="flat",
            font=("Georgia", 15),
        )

        # frames
        frame_customer = ttk.Frame(self, style="under.TFrame")
        frame_item = ttk.Frame(self, style="under.TFrame")

        # widgets for customer
        lb_title_customer = ttk.Label(
            frame_customer,
            text="Client",
            style="general.TLabel",
            width=13,
            anchor=cttk.CENTER,
            justify=cttk.CENTER,
        )
        bt_add_customer = ttk.Button(
            frame_customer,
            text="Ajouter",
            style="customer.TButton",
            width=13,
            command=self.add_customer,
        )

        # widgets for article
        lb_title_item = ttk.Label(
            frame_item,
            text="Article",
            style="general.TLabel",
            width=13,
            anchor=cttk.CENTER,
            justify=cttk.CENTER,
        )
        bt_add_item = ttk.Button(
            frame_item,
            text="Ajouter",
            style="item.TButton",
            width=13,
            command=self.add_item,
        )
        bt_delete_item = ttk.Button(
            frame_item,
            text="Supprimer",
            style="item.TButton",
            width=13,
            command=self.delete_item,
        )

        # widgets for self
        lb_title = ttk.Label(
            self,
            text="Menu Facture",
            font=("Georgia", 20),
            background="#283747",
        )
        bt_main_menu = ttk.Button(
            self,
            text="Menu Principale",
            style="main.TButton",
            width=13,
            command=self.back_main_menu,
        )
        bt_invoice_overview = ttk.Button(
            self,
            text="Aperçu Facture",
            style="test.TButton",
            width=13,
            command=self.show_facture,
        )

        # position label self
        lb_title.pack(side=cttk.TOP, padx=15, pady=20)

        # position frames
        frame_customer.pack(side=cttk.TOP, pady=30, padx=10)
        frame_item.pack(side=cttk.TOP, pady=30, padx=10)

        # position widgets customer
        lb_title_customer.pack(side=cttk.TOP, padx=10, pady=10)
        bt_add_customer.pack(side=cttk.TOP, padx=10, pady=10)

        # position widgets item
        lb_title_item.pack(side=cttk.TOP, padx=10, pady=10)
        bt_add_item.pack(side=cttk.TOP, padx=10, pady=10)
        bt_delete_item.pack(side=cttk.TOP, padx=10, pady=10)

        # position widgets self
        bt_main_menu.pack(side=cttk.BOTTOM, padx=10, pady=10)
        bt_invoice_overview.pack(side=cttk.BOTTOM, pady=20, padx=10)

    def back_main_menu(self):
        """Reviens au menu principale"""
        for widget in self.window.winfo_children():
            widget.destroy()
        mainMenu.MainMenu(self.window)

    def state_bt_delete_customer(self, state: str):
        """Modifie le status du bouton supprimer un client"""
        self.bt_delete_customer.configure(state=state)

    def add_customer(self):
        self.data_invoice.add_client()

    def add_item(self):
        self.data_invoice.add_item()

    def show_facture(self):
        self.data_invoice.record_invoice()

    def delete_item(self):
        self.data_invoice.delete_item()
