import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk


class MainView(ttk.Window):
    def __init__(self, title: str, height: int, width: int):
        super().__init__(themename="superhero")
        self.title(title)
        self.minsize(width, height)

        self.create_main_menu()

    def create_main_menu(self):
        # style and config's
        bt_item_style = ttk.Style().configure(
            "item.TButton",
            background="#E59866",
            bordercolor="#E59866",
            relief="flat",
            font=("Helvitica", 20),
        )
        bt_customer_style = ttk.Style().configure(
            "customer.TButton",
            background="#8BC34A",
            bordercolor="#8BC34A",
            relief="flat",
            font=("Helvitica", 20),
        )
        bt_invoice_style = ttk.Style().configure(
            "invoice.TButton",
            background="#7E57C2",
            bordercolor="#7E57C2",
            relief="flat",
            font=("Helvitica", 20),
        )
        bt_apropos_style = ttk.Style().configure(
            "apropos.TButton",
            background="#4DD0E1",
            bordercolor="#4DD0E1",
            relief="flat",
            font=("Helvitica", 20),
        )
        bt_setting_style = ttk.Style().configure(
            "setting.TButton",
            background="#FFA726",
            bordercolor="#FFA726",
            relief="flat",
            font=("Helvitica", 20),
        )
        bt_close_style = ttk.Style().configure(
            "close.TButton",
            background="#C0392B",
            bordercolor="#C0392B",
            relief="flat",
            font=("Helvitica", 20),
        )
        # frame
        self.main_menu_frame = ttk.Frame(self)
        # position of the frame
        self.main_menu_frame.pack(side=cttk.LEFT, fill=cttk.Y)
        # widget button
        self.bt_item = ttk.Button(
            self.main_menu_frame,
            text="Article",
            command=self.do_show_article,
            width=10,
            style="item.TButton",
        )
        self.bt_customer = ttk.Button(
            self.main_menu_frame,
            text="Client",
            command=self.do_show_customer,
            width=10,
            style="customer.TButton",
        )
        self.bt_invoice = ttk.Button(
            self.main_menu_frame,
            text="Facture",
            command=self.do_show_invoice,
            width=10,
            style="invoice.TButton",
        )
        self.bt_close = ttk.Button(
            self.main_menu_frame,
            text="Quitter",
            command=self.do_close,
            width=10,
            style="close.TButton",
        )
        self.bt_apropos = ttk.Button(
            self.main_menu_frame, text="Apropos", width=10, style="apropos.TButton"
        )
        self.bt_setting = ttk.Button(
            self.main_menu_frame, text="Paramètres", width=10, style="setting.TButton"
        )
        # position widget
        self.bt_item.pack(side=cttk.TOP, pady=30, padx=10)
        self.bt_customer.pack(side=cttk.TOP, padx=10)
        self.bt_invoice.pack(side=cttk.TOP, pady=30, padx=10)
        self.bt_close.pack(side=cttk.BOTTOM, pady=30, padx=10)
        self.bt_apropos.pack(side=cttk.BOTTOM, padx=10)
        self.bt_setting.pack(side=cttk.BOTTOM, pady=30, padx=10)

    def start_main_view(self):
        self.mainloop()

    def do_show_article(self):
        self.main_menu_frame.pack_forget()
        Article(self)

    def do_show_customer(self):
        pass

    def do_show_invoice(self):
        pass

    def do_close(self):
        exit()


class Article:
    def __init__(self, parent):
        self.window = parent
        self.frame = ttk.Frame(parent)
        self.frame.pack(side=cttk.LEFT, fill=cttk.Y)
        # style and
        bt_add_style = ttk.Style().configure(
            "add.TButton",
            background="#8BC34A",
            bordercolor="#8BC34A",
            relief="flat",
            font=("Helvitica", 20),
        )
        bt_change_style = ttk.Style().configure(
            "change.TButton",
            background="#E59866",
            bordercolor="#E59866",
            relief="flat",
            font=("Helvitica", 20),
        )
        bt_remove_style = ttk.Style().configure(
            "remove.TButton",
            background="#7E57C2",
            bordercolor="#7E57C2",
            relief="flat",
            font=("Helvitica", 20),
        )
        bt_item_search = ttk.Style().configure(
            "search.TButton",
            background="#4DD0E1",
            bordercolor="#4DD0E1",
            relief="flat",
            font=("Helvitica", 20),
        )
        bt_back_style = ttk.Style().configure(
            "back.TButton",
            background="#C0392B",
            bordercolor="#C0392B",
            relief="flat",
            font=("Helvitica", 20),
        )
        # widget button
        self.bt_add = ttk.Button(
            self.frame,
            text="Ajouter",
            command=self.create_add_item,
            width=10,
            style="add.TButton",
        )
        self.bt_change = ttk.Button(
            self.frame,
            text="Modifier",
            command=self.do_show_change_data,
            width=10,
            style="change.TButton",
        )
        self.bt_remove = ttk.Button(
            self.frame,
            text="Supprimer",
            command=self.do_show_remove_data,
            width=10,
            style="remove.TButton",
        )
        self.bt_item_search = ttk.Button(
            self.frame,
            text="Rechercher",
            command=self.do_show_search_item_data,
            width=10,
            style="search.TButton",
        )
        self.bt_back = ttk.Button(
            self.frame,
            text="Retour",
            command=self.do_back_menu,
            width=10,
            style="back.TButton",
        )
        # position button
        self.bt_add.pack(side=cttk.TOP, padx=10, pady=30)
        self.bt_change.pack(side=cttk.TOP, padx=10)
        self.bt_remove.pack(side=cttk.TOP, padx=10, pady=30)
        self.bt_item_search.pack(side=cttk.TOP, padx=10)
        self.bt_back.pack(side=cttk.BOTTOM, padx=10, pady=30)

    def create_add_item(self):
        # split window in multiple frames
        self.add_item_frame = ttk.Frame(self.window)
        top_frame = ttk.Frame(self.add_item_frame)
        bottom_frame = ttk.Frame(self.add_item_frame)
        # position frames
        self.add_item_frame.pack(side=cttk.RIGHT,expand=True,fill=cttk.BOTH)
        top_frame.pack(side=cttk.TOP, expand=True, fill=cttk.BOTH)
        bottom_frame.pack(side=cttk.BOTTOM, expand=True, fill=cttk.X)
        # config position
        top_frame.columnconfigure(1, weight=2)
        top_frame.rowconfigure(0, weight=1)
        top_frame.rowconfigure(5, weight=1)
        # widget button
        bt_confirm = ttk.Button(bottom_frame, text="CONFIRMATION")
        bt_back = ttk.Button(
            bottom_frame,
            text="RETOUR",
            command=self.do_back_menu_option,
            style="danger",
        )
        # widget label
        lb_top_empty = ttk.Label(top_frame)
        lb_bottom_empty = ttk.Label(top_frame)
        lb_name = ttk.Label(top_frame, text="Nom :")
        lb_description = ttk.Label(top_frame, text="Description :")
        lb_prix_htva = ttk.Label(top_frame, text="Prix HTVA :")
        lb_taux_tva = ttk.Label(top_frame, text="Taux TVA :")
        # widget entry
        en_name = ttk.Entry(top_frame)
        en_description = ttk.Entry(top_frame)
        en_prix_htva = ttk.Entry(top_frame)
        en_taux_tva = ttk.Entry(top_frame)
        # position label
        lb_top_empty.grid(columnspan=2, row=0, sticky=cttk.NSEW)
        lb_name.grid(column=0, row=1, pady=10)
        lb_description.grid(column=0, row=2, pady=10)
        lb_prix_htva.grid(column=0, row=3, pady=10)
        lb_taux_tva.grid(column=0, row=4, pady=10)
        lb_bottom_empty.grid(columnspan=2, row=5, sticky=cttk.NSEW)
        # position entry
        en_name.grid(column=1, row=1, sticky=cttk.EW, pady=10, padx=10)
        en_description.grid(column=1, row=2, sticky=cttk.EW, pady=10, padx=10)
        en_prix_htva.grid(column=1, row=3, sticky=cttk.EW, pady=10, padx=10)
        en_taux_tva.grid(column=1, row=4, sticky=cttk.EW, pady=10, padx=10)
        # position button
        bt_confirm.pack(side=cttk.RIGHT, fill=cttk.X, expand=True, padx=20)
        bt_back.pack(side=cttk.LEFT, fill=cttk.X, expand=True, padx=20)

    def do_show_change_data(self):
        pass

    def do_show_remove_data(self):
        pass

    def do_show_search_item_data(self):
        pass

    def do_back_menu(self):
        self.frame.pack_forget()
        MainView.create_main_menu(self.window)

    def do_back_menu_option(self):
        self.add_item_frame.pack_forget()

    def hide_widget(self):
        pass
