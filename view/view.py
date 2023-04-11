import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk
import ttkbootstrap.dialogs as dialogs
from model.model import Item


class MainView(ttk.Window):
    def __init__(self, title: str, height: int, width: int):
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

    def start_main_view(self):
        # start l'interface
        self.mainloop()

    def show_article(self):
        # vide la frame_main_menu
        self.clean_widget_frame(self.frame_menu)
        # affiche le menu article
        ItemMenu(self, self.controller, self.frame_menu)

    def do_show_customer(self):
        # affiche le menu client
        pass

    def do_show_invoice(self):
        # affiche le menu facture
        pass

    @staticmethod
    def clean_widget_frame(frame):
        # boucle qui supprime tous les éléments de la frame
        for widget in frame.winfo_children():
            widget.destroy()

    @property
    def controller(self):
        """controller"""
        try:
            return self._controller
        except AttributeError:
            self.show_message_error("No controller set")
            self.quit()

    @controller.setter
    def controller(self, value):
        # assigne le paramètre controller
        self._controller = value

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


class ItemMenu:
    def __init__(self, parent, controller, frame_menu):
        # style du menu article
        ttk.Style().configure("frame.TFrame", background="#283747")
        ttk.Style().configure(
            "add.TButton",
            background="#8BC34A",
            bordercolor="#8BC34A",
            relief="flat",
            font=("Georgia", 20),
        )
        ttk.Style().configure(
            "change.TButton",
            background="#E59866",
            bordercolor="#E59866",
            relief="flat",
            font=("Georgia", 20),
        )
        ttk.Style().configure(
            "remove.TButton",
            background="#7E57C2",
            bordercolor="#7E57C2",
            relief="flat",
            font=("Georgia", 20),
        )
        ttk.Style().configure(
            "search.TButton",
            background="#42B7C6",
            bordercolor="#42B7C6",
            relief="flat",
            font=("Georgia", 20),
        )
        ttk.Style().configure(
            "back.TButton",
            background="#C0392B",
            bordercolor="#C0392B",
            relief="flat",
            font=("Georgia", 20),
        )
        # variable de récupération
        self.window = parent
        self.controller = controller
        # frame
        self.frame_menu = frame_menu
        self.frame_data = ttk.Frame(parent)
        self.frame_data.pack(side=cttk.RIGHT, expand=True, fill=cttk.BOTH)
        # variable ttk
        self.var_name = ttk.StringVar()
        self.var_description = ttk.StringVar()
        self.var_tva_tare = ttk.StringVar()
        self.var_htva_price = ttk.DoubleVar()
        # widget label
        lb_title = ttk.Label(
            self.frame_menu,
            text="Menu Article",
            font=("Georgia", 20),
            background="#283747",
        )
        # widget button
        self.bt_add = ttk.Button(
            self.frame_menu,
            text="Ajouter",
            command=self.show_new_item,
            width=10,
            style="add.TButton",
        )
        self.bt_change = ttk.Button(
            self.frame_menu,
            text="Modifier",
            command=self.show_modif_item,
            width=10,
            style="change.TButton",
        )
        self.bt_remove = ttk.Button(
            self.frame_menu,
            text="Supprimer",
            command=self.show_delete_item,
            width=10,
            style="remove.TButton",
        )
        self.bt_item_search = ttk.Button(
            self.frame_menu,
            text="Rechercher",
            command=self.show_search_item,
            width=10,
            style="search.TButton",
        )
        self.bt_back = ttk.Button(
            self.frame_menu,
            text="Retour",
            command=self.back_main_menu,
            width=10,
            style="back.TButton",
        )
        # position label
        lb_title.pack(side=cttk.TOP, padx=10, pady=10)
        # position button
        self.bt_add.pack(side=cttk.TOP, padx=10, pady=30)
        self.bt_change.pack(side=cttk.TOP, padx=10)
        self.bt_remove.pack(side=cttk.TOP, padx=10, pady=30)
        self.bt_item_search.pack(side=cttk.TOP, padx=10)
        self.bt_back.pack(side=cttk.BOTTOM, padx=10, pady=30)

    def data_item(self):
        """Crée les widgets pour les formulaires"""
        # variable
        tva_rate = ["21%", "12%", "6%"]
        # style
        ttk.Style().configure("frame.TFrame", background="#283747")
        ttk.Style().configure(
            "back.TButton",
            background="#C0392B",
            bordercolor="#C0392B",
            relief="flat",
            font=("Georgia", 25),
        )
        ttk.Style().configure(
            "confirm.TButton",
            background="#2ECC71",
            bordercolor="#2ECC71",
            relief="flat",
            font=("Georgia", 25),
        )
        # split window in multiple frames
        top_frame = ttk.Frame(self.frame_data)
        bottom_frame = ttk.Frame(self.frame_data)
        # position frames
        top_frame.pack(side=cttk.TOP, expand=True, fill=cttk.BOTH)
        bottom_frame.pack(side=cttk.BOTTOM, expand=True, fill=cttk.BOTH)
        # config of columns and rows
        top_frame.columnconfigure(1, weight=2)
        top_frame.rowconfigure(0, weight=1)
        top_frame.rowconfigure(5, weight=1)
        # widget button
        self.bt_confirm_item = ttk.Button(
            bottom_frame,
            text="Confirmation",
            style="confirm.TButton",
            width=15,
        )
        bt_back = ttk.Button(
            bottom_frame,
            text="Retour",
            command=self.back_item_menu,
            style="back.TButton",
            width=15,
        )
        # widget label
        lb_name = ttk.Label(top_frame, text="Nom :", font=("Georgia", 25))
        lb_description = ttk.Label(
            top_frame, text="Description :", font=("Georgia", 25)
        )
        lb_htva_price = ttk.Label(top_frame, text="Prix HTVA :", font=("Georgia", 25))
        lb_tva_tare = ttk.Label(top_frame, text="Taux TVA :", font=("Georgia", 25))
        # widget entry
        en_name = ttk.Entry(top_frame, font=("Georgia", 25), textvariable=self.var_name)
        en_description = ttk.Entry(
            top_frame, font=("Georgia", 25), textvariable=self.var_description
        )
        en_htva_price = ttk.Entry(
            top_frame, font=("Georgia", 25), textvariable=self.var_htva_price
        )
        # widget list
        en_tva_tare = ttk.Combobox(
            top_frame,
            values=tva_rate,
            font=("Georgia", 25),
            textvariable=self.var_tva_tare,
        )
        # position label
        lb_name.grid(column=0, row=1, pady=10)
        lb_description.grid(column=0, row=2, pady=10)
        lb_htva_price.grid(column=0, row=3, pady=10)
        lb_tva_tare.grid(column=0, row=4, pady=10)
        # position entry
        en_name.grid(column=1, row=1, sticky=cttk.EW, pady=10, padx=10)
        en_description.grid(column=1, row=2, sticky=cttk.EW, pady=10, padx=10)
        en_htva_price.grid(column=1, row=3, sticky=cttk.EW, pady=10, padx=10)
        en_tva_tare.grid(column=1, row=4, sticky=cttk.EW, pady=10, padx=10)
        # position button
        self.bt_confirm_item.pack(side=cttk.RIGHT, padx=50)
        bt_back.pack(side=cttk.LEFT, padx=50)

    def show_new_item(self):
        """Affiche formulaire pour créer un article"""
        self.state_item_menu("disabled")
        self.data_item()
        self.bt_confirm_item["command"] = self.new_item

    def show_modif_item(self):
        """Affiche le formulaire pour changer un article"""
        pass

    def show_delete_item(self):
        """Affiche le formulaire pour supprimer un article"""
        pass

    def show_search_item(self):
        """Affiche les données d'un article"""
        self.state_item_menu("disabled")
        self.clean_frame(self.frame_data)
        self.show_item_database(self.set_show_search_item)
        self.insert_item_in_view_item_database()

    def back_main_menu(self):
        """Reviens au menu principale"""
        self.clean_frame(self.frame_menu)
        MainView.create_main_menu(self.window)

    def state_item_menu(self, state: str):
        """Modifie le status des boutons du menu article"""
        self.bt_add.configure(state=state)
        self.bt_change.configure(state=state)
        self.bt_remove.configure(state=state)
        self.bt_item_search.configure(state=state)
        self.bt_back.configure(state=state)

    def new_item(self):
        """Crée un article dans la base de données"""
        self.controller.new_item(
            str(self.var_name.get()),
            str(self.var_description.get()),
            float(str(self.var_htva_price.get())),
            str(self.var_tva_tare.get()),
        )
        self.clean_frame(self.frame_data)
        self.state_item_menu("normal")

    @staticmethod
    def clean_frame(frame):
        """Vide la frame menu"""
        for widget in frame.winfo_children():
            widget.destroy()

    def back_item_menu(self):
        """Reviens sur le menu article"""
        self.clean_frame(self.frame_data)
        self.clean_variable_ttk()
        self.state_item_menu("normal")

    def show_item_database(self, command_confirm):
        """Affiche les articles de la base de données"""
        # style
        ttk.Style().configure(
            "back.TButton",
            background="#C0392B",
            bordercolor="#C0392B",
            relief="flat",
            font=("Georgia", 25),
        )
        ttk.Style().configure(
            "confirm.TButton",
            background="#2ECC71",
            bordercolor="#2ECC71",
            relief="flat",
            font=("Georgia", 25),
        )
        ttk.Style().configure("my.Treeview", background="#283747", rowheight=25)
        # frame
        bottom_frame = ttk.Frame(self.frame_data)
        top_frame = ttk.Frame(self.frame_data)
        table_frame = ttk.Frame(top_frame)
        # position frame
        bottom_frame.pack(side=cttk.BOTTOM, fill=cttk.X, expand=True)
        top_frame.pack(side=cttk.TOP, fill=cttk.BOTH, expand=True)
        table_frame.pack(pady=50, padx=50, fill=cttk.BOTH, expand=True)
        # view table
        scrollbar = ttk.Scrollbar(table_frame, orient=cttk.VERTICAL)
        self.table = ttk.Treeview(
            table_frame,
            columns=["id", "name"],
            yscrollcommand=scrollbar.set,
            selectmode=cttk.BROWSE,
            style="my.Treeview",
        )
        # config the scrollbar
        scrollbar.config(command=self.table.yview)
        # format column
        self.table.column("#0", anchor=cttk.W, stretch=False, width=0, minwidth=0)
        self.table.column("id", anchor=cttk.W, stretch=False, width=100)
        self.table.column("name", anchor=cttk.W, stretch=True, width=200)
        # heading column
        self.table.heading("#0", anchor=cttk.W)
        self.table.heading("id", text="Code Article", anchor=cttk.W)
        self.table.heading("name", text="Nom", anchor=cttk.W)
        # position view table
        self.table.pack(side=cttk.LEFT, fill=cttk.BOTH, expand=True)
        scrollbar.pack(side=cttk.LEFT, fill=cttk.Y, padx=5)
        # button widget
        bt_back = ttk.Button(
            bottom_frame,
            text="Retour",
            style="back.TButton",
            command=self.back_item_menu,
            width=15,
        )
        bt_confirm = ttk.Button(
            bottom_frame,
            text="Confirmer",
            style="confirm.TButton",
            width=15,
            command=command_confirm,
        )
        # button position
        bt_back.pack(side=cttk.LEFT, padx=20, pady=10)
        bt_confirm.pack(side=cttk.RIGHT, padx=20, pady=10)

    def insert_item_in_view_item_database(self):
        """Ajout chaque article de la basse de données dans la vue"""
        items = self.controller.load_data_items()

        for item in items:
            self.table.insert("", ttk.END, values=(item.id_item, item.name_item))

    def get_data_of_selected_item(self):
        """Récupère les données de l'article, sélectionnez"""
        for selected_item in self.table.selection():
            select = self.table.item(selected_item)
            item = select["values"]
            return self.controller.load_data_item(item[0])


    def set_show_search_item(self):
        """Affiche l'article, sélectionnez"""
        try:
            item = self.get_data_of_selected_item()
            self.clean_frame(self.frame_data)
            self.set_variable_ttk(item)
            self.data_item()
            self.bt_confirm_item.destroy()
        except AttributeError:
            MainView.show_message_failure("Veuillez sélectionnez un élément!")
            self.state_item_menu("normal")


    def clean_variable_ttk(self) -> None:
        self.var_name.set("")
        self.var_description.set("")
        self.var_htva_price.set(00.00)
        self.var_tva_tare.set("")

    def set_variable_ttk(self, item: Item) -> None:
        self.var_name.set(item.name_item)
        self.var_description.set(item.description_item)
        self.var_htva_price.set(item.htva_price)
        self.var_tva_tare.set(item.tva_tare)
