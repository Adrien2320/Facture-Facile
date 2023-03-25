import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk


class MainView(ttk.Window):
    def __init__(self):
        super().__init__(themename="superhero")
        self.title("FACTURE FACILE")
        # split window in several frame
        main_menu_frame = ttk.Frame(self, style="warning")
        self.option_menu_frame = ttk.Frame(self, style="success")
        self.data_frame = ttk.Frame(self, style="danger")
        # position frame
        main_menu_frame.pack(side=cttk.LEFT, fill=cttk.Y)
        self.option_menu_frame.pack(side=cttk.LEFT, fill=cttk.Y)
        self.data_frame.pack(side=cttk.RIGHT, fill=cttk.BOTH, expand=True)
        # widget button
        bt_item = ttk.Button(
            main_menu_frame, text="ARTICLE", command=self.do_show_article
        )
        bt_customer = ttk.Button(
            main_menu_frame, text="CLIENT", command=self.do_show_customer
        )
        bt_invoice = ttk.Button(
            main_menu_frame, text="FACTURE", command=self.do_show_invoice
        )
        bt_close = ttk.Button(main_menu_frame, text="QUITTER", command=self.do_close)
        # position widget
        bt_item.pack(side=cttk.TOP)
        bt_customer.pack(side=cttk.TOP)
        bt_invoice.pack(side=cttk.TOP)
        bt_close.pack(side=cttk.BOTTOM)

    def star_main_view(self):
        self.mainloop()

    def do_close(self):
        exit()

    def do_show_article(self):
        MenuOption(self.option_menu_frame, self.data_frame)

    def do_show_customer(self):
        pass

    def do_show_invoice(self):
        pass


class MenuOption:
    def __init__(self, menu_frame: ttk.Frame, data_frame: ttk.Frame):
        # variable global
        self.data_Frame = data_frame
        # widget button
        bt_add = ttk.Button(menu_frame, text="AJOUTER", command=self.do_show_add_data)
        bt_change = ttk.Button(
            menu_frame, text="MODIFIER", command=self.do_show_change_data
        )
        bt_remove = ttk.Button(
            menu_frame, text="SUPPRIMER", command=self.do_show_remove_data
        )
        bt_item_search = ttk.Button(
            menu_frame, text="RECHERCHER", command=self.do_show_search_item_data
        )
        # position button
        bt_add.pack(side=cttk.TOP)
        bt_change.pack(side=cttk.TOP)
        bt_remove.pack(side=cttk.TOP)
        bt_item_search.pack(side=cttk.TOP)

    def do_show_add_data(self):
        # config position
        self.data_Frame.columnconfigure(0, weight=1)
        self.data_Frame.columnconfigure(1, weight=2)
        # widget button
        bt_confirm = ttk.Button(self.data_Frame, text="CONFIRMATION")
        # widget label
        lb_name = ttk.Label(self.data_Frame, text="Nom :")
        lb_description = ttk.Label(self.data_Frame, text="Description :")
        lb_prix_htva = ttk.Label(self.data_Frame, text="Prix HTVA :")
        lb_taux_tva = ttk.Label(self.data_Frame, text="Taux TVA :")
        # widget entry
        en_name = ttk.Entry(self.data_Frame)
        en_description = ttk.Entry(self.data_Frame)
        en_prix_htva = ttk.Entry(self.data_Frame)
        en_taux_tva = ttk.Entry(self.data_Frame)
        # position label
        lb_name.grid(column=0, row=0)
        lb_description.grid(column=0, row=1)
        lb_prix_htva.grid(column=0, row=2)
        lb_taux_tva.grid(column=0, row=3)
        # position entry
        en_name.grid(column=1, row=0, sticky=cttk.EW)
        en_description.grid(column=1, row=1, sticky=cttk.EW)
        en_prix_htva.grid(column=1, row=2, sticky=cttk.EW)
        en_taux_tva.grid(column=1, row=3, sticky=cttk.EW)
        # position button
        bt_confirm.grid(columnspan=2, row=4, sticky=cttk.EW)

    def do_show_change_data(self):
        pass

    def do_show_remove_data(self):
        pass

    def do_show_search_item_data(self):
        pass


if __name__ == "__main__":
    MainView().star_main_view()
