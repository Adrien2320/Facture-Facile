import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk


class MainView(ttk.Window):
    def __init__(self, title: str, height: int, width: int):
        super().__init__(themename="superhero")
        self.title(title)
        self.geometry(f"{width}x{height}")
        # style
        bt_item_style = ttk.Style()
        bt_customer_style = ttk.Style()
        bt_invoice_style = ttk.Style()
        bt_apropos_style = ttk.Style()
        bt_setting_style = ttk.Style()
        # config style
        bt_item_style.configure(
            "item.TButton", background="#E59866", bordercolor="#E59866", relief="flat"
        )
        bt_customer_style.configure("customer.TButton", background="#8BC34A", bordercolor="#8BC34A", relief="flat")
        bt_invoice_style.configure("invoice.TButton",background="#7E57C2",bordercolor="#7E57C2", relief="flat")
        bt_apropos_style.configure("apropos.TButton",background="#4DD0E1",bordercolor="#4DD0E1", relief="flat")
        bt_setting_style.configure("setting.TButton",background="#FFA726",bordercolor="#FFA726", relief="flat")
        # split window in multiple frames
        main_menu_frame = ttk.Frame(self)
        self.option_menu_frame = ttk.Frame(self)
        self.data_frame = ttk.Frame(self)
        # position of the frames
        main_menu_frame.pack(side=cttk.LEFT, fill=cttk.Y)
        self.option_menu_frame.pack(side=cttk.LEFT, fill=cttk.Y)
        self.data_frame.pack(side=cttk.RIGHT, fill=cttk.BOTH, expand=True)
        # widget button
        self.bt_item = ttk.Button(
            main_menu_frame,
            text="Article",
            command=self.do_show_article,
            width=20,
            style="item.TButton",
        )
        self.bt_customer = ttk.Button(
            main_menu_frame, text="Client", command=self.do_show_customer, width=20, style="customer.TButton"
        )
        self.bt_invoice = ttk.Button(
            main_menu_frame, text="Facture", command=self.do_show_invoice, width=20, style="invoice.TButton"
        )
        self.bt_close = ttk.Button(
            main_menu_frame,
            text="Quitter",
            command=self.do_close,
            width=20,
            style="danger",
        )
        self.bt_apropos = ttk.Button(main_menu_frame, text="Apropos", width=20,style="apropos.TButton")
        self.bt_setting = ttk.Button(main_menu_frame, text="Paramètres", width=20,style="setting.TButton")
        # position widget
        self.bt_item.pack(side=cttk.TOP, pady=30, padx=10)
        self.bt_customer.pack(side=cttk.TOP, padx=10)
        self.bt_invoice.pack(side=cttk.TOP, pady=30, padx=10)
        self.bt_close.pack(side=cttk.BOTTOM, pady=20, padx=10)
        self.bt_apropos.pack(side=cttk.BOTTOM, padx=10)
        self.bt_setting.pack(side=cttk.BOTTOM, pady=20, padx=10)

    def start_main_view(self):
        self.mainloop()

    def do_show_article(self):
        MenuArticle(
            self.option_menu_frame,
            self.data_frame,
            self.bt_item,
            self.bt_customer,
            self.bt_invoice,
            self.bt_close,
            self.bt_apropos,
            self.bt_setting,
        )
        self.bt_item["state"] = "disable"
        self.bt_customer["state"] = "disable"
        self.bt_invoice["state"] = "disable"
        self.bt_close["state"] = "disable"
        self.bt_apropos["state"] = "disable"
        self.bt_setting["state"] = "disable"

    def do_show_customer(self):
        pass

    def do_show_invoice(self):
        pass

    def do_close(self):
        exit()


class MenuArticle:
    def __init__(
        self,
        menu_frame: ttk.Frame,
        data_frame: ttk.Frame,
        bt_item: ttk.Button,
        bt_customer: ttk.Button,
        bt_invoice: ttk.Button,
        bt_close: ttk.Button,
        bt_apropos: ttk.Button,
        bt_setting: ttk.Button,
    ):
        # variable get from main menu frame
        self.menu_frame = menu_frame
        self.data_Frame = data_frame
        self.bt_item_main_menu = bt_item
        self.bt_customer_main_menu = bt_customer
        self.bt_invoice_main_menu = bt_invoice
        self.bt_close_main_menu = bt_close
        self.bt_apropos_main_menu = bt_apropos
        self.bt_setting_main_menu = bt_setting
        # widget button
        self.bt_add = ttk.Button(
            menu_frame, text="Ajouter", command=self.do_show_add_data, width=20
        )
        self.bt_change = ttk.Button(
            menu_frame, text="Modifier", command=self.do_show_change_data, width=20
        )
        self.bt_remove = ttk.Button(
            menu_frame, text="Supprimer", command=self.do_show_remove_data, width=20
        )
        self.bt_item_search = ttk.Button(
            menu_frame,
            text="Rechercher",
            command=self.do_show_search_item_data,
            width=20,
        )
        self.bt_back = ttk.Button(
            menu_frame,
            text="Retour",
            command=self.do_back_menu,
            width=20,
            style="danger",
        )
        # position button
        self.bt_add.pack(side=cttk.TOP, padx=10, pady=20)
        self.bt_change.pack(side=cttk.TOP, padx=10)
        self.bt_remove.pack(side=cttk.TOP, padx=10, pady=20)
        self.bt_item_search.pack(side=cttk.TOP, padx=10)
        self.bt_back.pack(side=cttk.BOTTOM, padx=10, pady=20)

    def do_show_add_data(self):
        # hide the menu frame
        self.bt_add["state"] = "disable"
        self.bt_change["state"] = "disable"
        self.bt_remove["state"] = "disable"
        self.bt_item_search["state"] = "disable"
        self.bt_back["state"] = "disable"
        # split window in multiple frames
        self.top_frame = ttk.Frame(self.data_Frame)
        self.bottom_frame = ttk.Frame(self.data_Frame)
        # position frames
        self.top_frame.pack(side=cttk.TOP, expand=True, fill=cttk.BOTH)
        self.bottom_frame.pack(side=cttk.BOTTOM, expand=True, fill=cttk.X)
        # config position
        self.top_frame.columnconfigure(1, weight=2)
        self.top_frame.rowconfigure(0, weight=1)
        self.top_frame.rowconfigure(5, weight=1)
        # widget button
        bt_confirm = ttk.Button(self.bottom_frame, text="CONFIRMATION")
        bt_back = ttk.Button(
            self.bottom_frame,
            text="RETOUR",
            command=self.do_back_menu_option,
            style="danger",
        )
        # widget label
        lb_top_empty = ttk.Label(self.top_frame)
        lb_bottom_empty = ttk.Label(self.top_frame)
        lb_name = ttk.Label(self.top_frame, text="Nom :")
        lb_description = ttk.Label(self.top_frame, text="Description :")
        lb_prix_htva = ttk.Label(self.top_frame, text="Prix HTVA :")
        lb_taux_tva = ttk.Label(self.top_frame, text="Taux TVA :")
        # widget entry
        en_name = ttk.Entry(self.top_frame)
        en_description = ttk.Entry(self.top_frame)
        en_prix_htva = ttk.Entry(self.top_frame)
        en_taux_tva = ttk.Entry(self.top_frame)
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
        self.bt_add.destroy()
        self.bt_change.destroy()
        self.bt_remove.destroy()
        self.bt_item_search.destroy()
        self.bt_back.destroy()
        self.bt_item_main_menu["state"] = "normal"
        self.bt_customer_main_menu["state"] = "normal"
        self.bt_invoice_main_menu["state"] = "normal"
        self.bt_close_main_menu["state"] = "normal"
        self.bt_apropos_main_menu["state"] = "normal"
        self.bt_setting_main_menu["state"] = "normal"

    def do_back_menu_option(self):
        self.top_frame.pack_forget()
        self.bottom_frame.pack_forget()
        self.bt_add["state"] = "normal"
        self.bt_change["state"] = "normal"
        self.bt_remove["state"] = "normal"
        self.bt_item_search["state"] = "normal"
        self.bt_back["state"] = "normal"
