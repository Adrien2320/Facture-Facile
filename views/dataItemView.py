import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk
import views.menuItemView as menuItem
import views.windowView as windowView
from models.itemModel import Item


class DataItem(ttk.Frame):
    bt_confirm_item: ttk.Button
    table: ttk.Treeview
    bt_confirm_selected: ttk.Button

    def __init__(self, window, menu_item):
        """Constructeur"""
        # style Frame
        ttk.Style().configure("frame.TFrame", background="#283747")
        # paramètre de la frame
        super().__init__(window, style="frame.TFrame")
        # position de la frame
        self.pack(side=cttk.RIGHT, fill=cttk.BOTH, expand=True)
        # variable ttk
        self.var_id = ttk.IntVar()
        self.var_name = ttk.StringVar()
        self.var_description = ttk.StringVar()
        self.var_tva_tare = ttk.StringVar()
        self.var_htva_price = ttk.DoubleVar()
        # variable
        self.window = window
        self.menu_item = menu_item

    def create_data_item(self):
        """Crée les widgets pour les formulaires"""
        # variable
        tva_rate = ["21%", "12%", "6%"]
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
        # split window in multiple frames
        top_frame = ttk.Frame(self)
        bottom_frame = ttk.Frame(self)
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

    def create_table(self):
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
        bottom_frame = ttk.Frame(self)
        top_frame = ttk.Frame(self)
        table_frame = ttk.Frame(top_frame)
        # position frame
        bottom_frame.pack(side=cttk.BOTTOM, fill=cttk.X, expand=True)
        top_frame.pack(side=cttk.TOP, fill=cttk.BOTH, expand=True)
        table_frame.pack(pady=50, padx=50, fill=cttk.BOTH, expand=True)
        # views table
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
        # position views table
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
        self.bt_confirm_selected = ttk.Button(
            bottom_frame,
            text="Confirmer",
            style="confirm.TButton",
            width=15,
        )
        # button position
        bt_back.pack(side=cttk.LEFT, padx=20, pady=10)
        self.bt_confirm_selected.pack(side=cttk.RIGHT, padx=20, pady=10)

    def clean_frame(self):
        """vide la frame"""
        for widget in self.winfo_children():
            widget.destroy()

    def back_item_menu(self):
        """Reviens sur le menu article"""
        self.destroy()
        self.clean_variable_ttk()
        menuItem.MenuItem.state_item_menu(self.menu_item, "normal")

    def clean_variable_ttk(self) -> None:
        """Vide les variables"""
        self.var_name.set("")
        self.var_description.set("")
        self.var_htva_price.set(00.00)
        self.var_tva_tare.set("")

    def set_variable_ttk(
        self, id_item: int, name: str, description: str, htva_price: float, tva_tare: str
    ) -> None:
        """Assigne les variables"""
        self.var_id.set(id_item)
        self.var_name.set(name)
        self.var_description.set(description)
        self.var_htva_price.set(htva_price)
        self.var_tva_tare.set(tva_tare)

    def show_new_item(self):
        self.create_data_item()
        self.bt_confirm_item["command"] = self.new_item

    def new_item(self):
        """Crée un article dans la base de données"""
        self.controller.new_item(
            str(self.var_name.get()),
            str(self.var_description.get()),
            float(str(self.var_htva_price.get())),
            str(self.var_tva_tare.get()),
        )
        self.destroy()
        menuItem.MenuItem.state_item_menu(self.menu_item, "normal")

    def show_search_item(self):
        """Affiche le formulaire pour rechercher un article"""
        self.create_table()
        self.insert_item_in_table()
        self.bt_confirm_selected["command"] = self.set_search_item

    def set_search_item(self):
        """Insert les données récolté dans la vue dataItem"""
        try:
            item = self.get_selected()
            self.set_variable_ttk(
                item.id_item,
                item.name_item,
                item.description_item,
                item.htva_price,
                item.tva_tare,
            )
            self.clean_frame()
            self.create_data_item()
            self.bt_confirm_item.destroy()
        except AttributeError:
            windowView.Window.show_message_failure("Veuillez sélectionnez un élément!")
            menuItem.MenuItem.state_item_menu(self.menu_item, "normal")

    def insert_item_in_table(self):
        """Ajout chaque article de la basse de données dans la vue"""
        items = self.controller.load_data_items()

        for item in items:
            self.table.insert("", ttk.END, values=(item.id_item, item.name_item))

    def get_selected(self) -> Item:
        """Récupère les données de l'article, sélectionnez"""
        for selected_item in self.table.selection():
            select = self.table.item(selected_item)
            item = select["values"]
            return self.controller.load_data_item(item[0])

    # method pour command button

    def modif_item(self):
        """Modifie un article"""
        pass
        """
        self.controller.modif_item(
            int(self.var_id.get()),
            str(self.var_name.get()),
            str(self.var_description.get()),
            float(str(self.var_htva_price.get())),
            str(self.var_tva_tare.get()),
        )
        self.clean_frame(self.frame_data)
        self.state_item_menu("normal")
        """

    def delete_item(self):
        """Supprime un article"""
        pass
        """
        try:
            item = self.get_selected()
            self.clean_frame(self.frame_data)
            self.controller.delete_item(item)
            self.clean_frame(self.frame_data)
            self.state_item_menu("normal")
        except AttributeError:
            Main.show_message_failure("Veuillez sélectionnez un élément!")
            self.state_item_menu("normal")
        """

    @property
    def controller(self):
        try:
            return self._controller
        except AttributeError:
            windowView.Window.show_message_error("Pas de controlleur")
            self.quit()

    @controller.setter
    def controller(self, value):
        self._controller = value
