import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk
import views.menuItemView

class DataItem(ttk.Frame):
    bt_confirm_item: ttk.Button

    def __init__(self, window,parent):
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
        self.parent = parent

    def create_data_item(self, frame):
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
        top_frame = ttk.Frame(frame)
        bottom_frame = ttk.Frame(frame)
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

    def back_item_menu(self):
        """Reviens sur le menu article"""
        self.destroy()
        self.clean_variable_ttk()
        views.menuItemView.MenuItem.state_item_menu(self.parent,"normal")

    def clean_variable_ttk(self) -> None:
        """Vide les variables"""
        self.var_name.set("")
        self.var_description.set("")
        self.var_htva_price.set(00.00)
        self.var_tva_tare.set("")

    def set_variable_ttk(self, id:int,name :str,description : str,htva_price : float,tva_tare : str) -> None:
        """Assigne les variables"""
        self.var_id.set(id)
        self.var_name.set(name)
        self.var_description.set(description)
        self.var_htva_price.set(htva_price)
        self.var_tva_tare.set(tva_tare)

    def show_new_item(self):
        self.create_data_item(self)
        self.bt_confirm_item["command"] = self.new_item
    def show_modif_item(self):
        pass

    def show_delete_item(self):
        pass

    def show_search_item(self):
        pass

    # command button
    def new_item(self):
        """Crée un article dans la base de données"""
        self.controller.new_item(
            str(self.var_name.get()),
            str(self.var_description.get()),
            float(str(self.var_htva_price.get())),
            str(self.var_tva_tare.get()),
        )
        self.destroy()
        views.menuItemView.MenuItem.state_item_menu(self.parent,"normal")

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


