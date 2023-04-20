import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk

class TableItem(ttk.Frame):

    def __init__(self,parent):
        super().__init__(parent)

    def show_item_table(self):
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

    def set_show_search_item(self):
        """Affiche l'article, sélectionnez"""
        try:
            item = self.get_selected()
            self.clean_frame(self.frame_data)
            self.set_variable_ttk(item)
            self.data_item()
            self.bt_confirm_item.destroy()
        except AttributeError:
            Main.show_message_failure("Veuillez sélectionnez un élément!")
            self.state_item_menu("normal")

    def set_show_modif_item(self):
        """Assigne l'affichage pour modifier un article"""
        try:
            item = self.get_selected()
            self.clean_frame(self.frame_data)
            self.set_variable_ttk(item)
            self.data_item()
            self.bt_confirm_item["command"] = self.modif_item
        except AttributeError:
            Main.show_message_failure("Veuillez sélectionnez un élément!")
            self.state_item_menu("normal")