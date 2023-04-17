import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk

class MenuItem(ttk.Frame):
    def __init__(self, parent):
        # style frame
        ttk.Style().configure("frame.TFrame", background="#283747")
        # paramètre object lui-même
        super().__init__(parent,style="frame.TFrame")
        # position self
        self.pack(side=cttk.LEFT, fill=cttk.Y)
        self.create_menu_item()

    def create_menu_item(self):
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

    def show_new_item(self):
        """Affiche formulaire pour créer un article"""
        self.state_item_menu("disabled")
        self.data_item()
        self.bt_confirm_item["command"] = self.new_item

    def show_modif_item(self):
        """Affiche le formulaire pour changer un article"""
        self.state_item_menu("disabled")
        self.clean_frame(self.frame_data)
        self.show_item_table()
        self.insert_item_in_table()
        self.bt_confirm_selected["command"] = self.set_show_modif_item

    def show_delete_item(self):
        """Affiche le formulaire pour supprimer un article"""
        self.state_item_menu("disabled")
        self.clean_frame(self.frame_data)
        self.show_item_table()
        self.insert_item_in_table()
        self.bt_confirm_selected["command"] = self.delete_item

    def show_search_item(self):
        """Affiche les données d'un article"""
        self.state_item_menu("disabled")
        self.clean_frame(self.frame_data)
        self.show_item_table()
        self.insert_item_in_table()
        self.bt_confirm_selected["command"] = self.set_show_search_item

    def back_main_menu(self):
        """Reviens au menu principale"""
        self.clean_frame(self.frame_menu)
        Main.create_main_menu(self.window)

    def state_item_menu(self, state: str):
        """Modifie le status des boutons du menu article"""
        self.bt_add.configure(state=state)
        self.bt_change.configure(state=state)
        self.bt_remove.configure(state=state)
        self.bt_item_search.configure(state=state)
        self.bt_back.configure(state=state)
