import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk
import views.mainMenuView as mainMenu


class MenuInvoice(ttk.Frame):
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

    def create_menu(self):
        """Création des widgets du menu facture"""
        # style of widgets
        ttk.Style().configure("TFrame", background="#283747")
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
        # frame
        frame_customer = ttk.Labelframe(self, text="Client", style="TFrame")
        frame_item = ttk.Labelframe(self, text="Article", style="TFrame")
        # widget label self
        lb_title = ttk.Label(
            self,
            text="Menu Facture",
            font=("Georgia", 20),
            background="#283747",
        )
        # widget button customer
        bt_add_customer = ttk.Button(frame_customer, text="Ajouter", style="customer.TButton",width=12)
        bt_modif_customer = ttk.Button(frame_customer, text="Modifier", style="customer.TButton",width=12)
        bt_delete_customer = ttk.Button(
            frame_customer, text="Supprimer", style="customer.TButton",width=12
        )
        # widget button item
        bt_add_item = ttk.Button(frame_item, text="Ajouter", style="item.TButton",width=12)
        bt_modif_item = ttk.Button(frame_item, text="Modifier", style="item.TButton",width=12)
        bt_delete_item = ttk.Button(frame_item, text="Supprimer", style="item.TButton",width=12)
        # widget button self
        bt_main_menu = ttk.Button(
            self, text="Menu Principale", style="main.TButton",width=12, command=self.back_main_menu
        )
        bt_invoice_overview = ttk.Button(
            self, text="Aperçu Facture", style="test.TButton",width=12
        )
        # position label self
        lb_title.pack(side=cttk.TOP, padx=15, pady=20)
        # position frame
        frame_customer.pack(side=cttk.TOP, pady=30, padx=10)
        frame_item.pack(side=cttk.TOP, pady=30, padx=10)
        # position button customer
        bt_add_customer.pack(side=cttk.TOP, padx=10, pady=10)
        bt_modif_customer.pack(side=cttk.TOP, padx=10, pady=10)
        bt_delete_customer.pack(side=cttk.TOP, padx=10, pady=10)
        # position button customer
        bt_add_item.pack(side=cttk.TOP, padx=10, pady=10)
        bt_modif_item.pack(side=cttk.TOP, padx=10, pady=10)
        bt_delete_item.pack(side=cttk.TOP, padx=10, pady=10)
        # position button self
        bt_main_menu.pack(side=cttk.BOTTOM, padx=10, pady=10)
        bt_invoice_overview.pack(side=cttk.BOTTOM, pady=20, padx=10)

    def back_main_menu(self):
        """Reviens au menu principale"""
        self.destroy()
        mainMenu.MainMenu(self.window)