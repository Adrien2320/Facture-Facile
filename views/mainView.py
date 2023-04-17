import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk
import ttkbootstrap.dialogs as dialogs


class MainView(ttk.Window):
    def __init__(self, title: str, height: int, width: int):
        # Paramètre object lui-même
        super().__init__(themename="superhero")
        self.title(title)
        self.minsize(width, height)
        # style frame
        ttk.Style().configure("frame.TFrame", background="#283747")
        # frame
        self.frame_menu = ttk.Frame(self, style="frame.TFrame")
        # position of the frame
        self.frame_menu.pack(side=cttk.LEFT, fill=cttk.Y)
        # création du menu
        self.create_main_menu()

    def create_main_menu(self):
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
            self.frame_menu,
            text="Menu Principale",
            font=("Georgia", 20),
            background="#283747",
        )
        # widget button
        bt_item = ttk.Button(
            self.frame_menu,
            text="Article",
            command=self.show_article,
            width=10,
            style="item.TButton",
        )
        bt_customer = ttk.Button(
            self.frame_menu,
            text="Client",
            command=self.do_show_customer,
            width=10,
            style="customer.TButton",
        )
        bt_invoice = ttk.Button(
            self.frame_menu,
            text="Facture",
            command=self.do_show_invoice,
            width=10,
            style="invoice.TButton",
        )
        bt_close = ttk.Button(
            self.frame_menu,
            text="Quitter",
            command=self.quit,
            width=10,
            style="close.TButton",
        )
        bt_apropos = ttk.Button(
            self.frame_menu, text="Apropos", width=10, style="apropos.TButton"
        )
        bt_setting = ttk.Button(
            self.frame_menu, text="Paramètres", width=10, style="setting.TButton"
        )
        # position widget
        lb_tittle.pack(side=cttk.TOP, pady=20, padx=10)
        bt_item.pack(side=cttk.TOP, pady=30, padx=10)
        bt_customer.pack(side=cttk.TOP, padx=10)
        bt_invoice.pack(side=cttk.TOP, pady=30, padx=10)
        bt_close.pack(side=cttk.BOTTOM, pady=30, padx=10)
        bt_apropos.pack(side=cttk.BOTTOM, padx=10)
        bt_setting.pack(side=cttk.BOTTOM, pady=30, padx=10)

    def start_main(self):
        # start l'interface
        self.mainloop()

    def show_article(self):
        # vide la frame_main_menu
        self.frame_menu.destroy()
        # affiche le menu article
        # TODO lancer le menu item

    def do_show_customer(self):
        # affiche le menu client
        pass

    def do_show_invoice(self):
        # affiche le menu facture
        pass

    @staticmethod
    def show_message_success(text: str):
        # message pour confirmer une action
        dialogs.Messagebox.show_info(text, "Réussi")

    @staticmethod
    def show_message_failure(text: str):
        # message pour avertir qu'une action à échouer
        dialogs.Messagebox.show_info(text, "Echec")

    @staticmethod
    def show_message_error(text: str):
        # message qui avertir qu'il y a un bug dans l'application
        dialogs.Messagebox.show_error(text, title="ERROR")
