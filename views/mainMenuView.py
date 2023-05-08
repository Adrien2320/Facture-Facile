import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk
import views.items.menuItemView as menuItem
import views.customer.menuCustomerView as menuCustomer
import views.invoices.menuInvoiceview as menuInvoice
import views.invoices.dataInvoiceview as dataInvoice


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
            "apropos.TButton",
            background="#2F818B",
            bordercolor="#2F818B",
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
        bt_item = ttk.Button(
            self,
            text="Article",
            command=self.show_article,
            width=12,
            style="item.TButton",
        )
        bt_customer = ttk.Button(
            self,
            text="Client",
            command=self.do_show_customer,
            width=12,
            style="customer.TButton",
        )
        bt_invoice = ttk.Button(
            self,
            text="Facture",
            command=self.do_show_invoice,
            width=12,
            style="invoices.TButton",
        )
        bt_close = ttk.Button(
            self,
            text="Quitter",
            command=self.quit,
            width=12,
            style="close.TButton",
        )
        bt_apropos = ttk.Button(self, text="Apropos", width=12, style="apropos.TButton")
        bt_setting = ttk.Button(
            self, text="Paramètres", width=12, style="setting.TButton"
        )
        # position widget
        lb_tittle.pack(side=cttk.TOP, pady=20, padx=10)
        bt_item.pack(side=cttk.TOP, pady=30, padx=10)
        bt_customer.pack(side=cttk.TOP, padx=10)
        bt_invoice.pack(side=cttk.TOP, pady=30, padx=10)
        bt_close.pack(side=cttk.BOTTOM, pady=30, padx=10)
        bt_apropos.pack(side=cttk.BOTTOM, padx=10)
        bt_setting.pack(side=cttk.BOTTOM, pady=30, padx=10)

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
        dataInvoice.DataInvoice(self.window)

