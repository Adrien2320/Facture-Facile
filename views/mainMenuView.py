import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk
import views.menuItemView


class MainMenu(ttk.Frame):
    def __init__(self, window):
        # style frame
        ttk.Style().configure("frame.TFrame", background="#283747")
        super().__init__(window, style="frame.TFrame")
        # position of the frame
        self.pack(side=cttk.LEFT, fill=cttk.Y)
        # creation du menu
        self.create_main_menu(self)
        # variable
        self.window = window

    def create_main_menu(self, frame):
        """ Créer les widgets du menu principal """
        # style of widgets
        ttk.Style().configure(
            "item.TButton",
            background="#E59866",
            bordercolor="#E59866",
            relief="flat",
            font=("Georgia", 20),
        )
        ttk.Style().configure(
            "customer.TButton",
            background="#8BC34A",
            bordercolor="#8BC34A",
            relief="flat",
            font=("Georgia", 20),
        )
        ttk.Style().configure(
            "invoice.TButton",
            background="#7E57C2",
            bordercolor="#7E57C2",
            relief="flat",
            font=("Georgia", 20),
        )
        ttk.Style().configure(
            "apropos.TButton",
            background="#42B7C6",
            bordercolor="#42B7C6",
            relief="flat",
            font=("Georgia", 20),
        )
        ttk.Style().configure(
            "setting.TButton",
            background="#FFA726",
            bordercolor="#FFA726",
            relief="flat",
            font=("Georgia", 20),
        )
        ttk.Style().configure(
            "close.TButton",
            background="#C0392B",
            bordercolor="#C0392B",
            relief="flat",
            font=("Georgia", 20),
        )
        # widget label
        lb_tittle = ttk.Label(
            frame,
            text="Menu Principale",
            font=("Georgia", 20),
            background="#283747",
        )
        # widget button
        bt_item = ttk.Button(
            frame,
            text="Article",
            command=self.show_article,
            width=10,
            style="item.TButton",
        )
        bt_customer = ttk.Button(
            frame,
            text="Client",
            command=self.do_show_customer,
            width=10,
            style="customer.TButton",
        )
        bt_invoice = ttk.Button(
            frame,
            text="Facture",
            command=self.do_show_invoice,
            width=10,
            style="invoice.TButton",
        )
        bt_close = ttk.Button(
            frame,
            text="Quitter",
            command=self.quit,
            width=10,
            style="close.TButton",
        )
        bt_apropos = ttk.Button(
            frame, text="Apropos", width=10, style="apropos.TButton"
        )
        bt_setting = ttk.Button(
            frame, text="Paramètres", width=10, style="setting.TButton"
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
        """ Lance le menu article """
        # détruit la fenêtre
        self.destroy()
        # affiche le menu article
        views.menuItemView.MenuItem(self.window)

    def do_show_customer(self):
        """  Lance le menu client"""
        # affiche le menu client
        pass

    def do_show_invoice(self):
        """ Lance la menu facture """
        # affiche le menu facture
        pass