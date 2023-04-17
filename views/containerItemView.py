
# variable ttk
        self.var_id = ttk.IntVar()
        self.var_name = ttk.StringVar()
        self.var_description = ttk.StringVar()
        self.var_tva_tare = ttk.StringVar()
        self.var_htva_price = ttk.DoubleVar()




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

    def clean_variable_ttk(self) -> None:
        """Vide les variables"""
        self.var_name.set("")
        self.var_description.set("")
        self.var_htva_price.set(00.00)
        self.var_tva_tare.set("")

    def set_variable_ttk(self, item: Item) -> None:
        """Assigne les variables"""
        self.var_id.set(item.id_item)
        self.var_name.set(item.name_item)
        self.var_description.set(item.description_item)
        self.var_htva_price.set(item.htva_price)
        self.var_tva_tare.set(item.tva_tare)

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

    def modif_item(self):
        """Modifie un article"""
        self.controller.modif_item(
            int(self.var_id.get()),
            str(self.var_name.get()),
            str(self.var_description.get()),
            float(str(self.var_htva_price.get())),
            str(self.var_tva_tare.get()),
        )
        self.clean_frame(self.frame_data)
        self.state_item_menu("normal")

    def delete_item(self):
        """Supprime un article"""
        try:
            item = self.get_selected()
            self.clean_frame(self.frame_data)
            self.controller.delete_item(item)
            self.clean_frame(self.frame_data)
            self.state_item_menu("normal")
        except AttributeError:
            Main.show_message_failure("Veuillez sélectionnez un élément!")
            self.state_item_menu("normal")
