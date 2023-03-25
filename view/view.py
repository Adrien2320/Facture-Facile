import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk


class MainView(ttk.Window):
    def __init__(self, title: str,height : int , width : int):
        super().__init__(themename="superhero")
        self.title(title)
        self.geometry(f"{width}x{height}")

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
            main_menu_frame, text="ARTICLE", command=self.do_show_article
        )
        self.bt_customer = ttk.Button(
            main_menu_frame, text="CLIENT", command=self.do_show_customer
        )
        self.bt_invoice = ttk.Button(
            main_menu_frame, text="FACTURE", command=self.do_show_invoice
        )
        self.bt_close = ttk.Button(
            main_menu_frame, text="QUITTER", command=self.do_close
        )
        # position widget
        self.bt_item.pack(side=cttk.TOP)
        self.bt_customer.pack(side=cttk.TOP)
        self.bt_invoice.pack(side=cttk.TOP)
        self.bt_close.pack(side=cttk.BOTTOM)

    def start_main_view(self):
        self.mainloop()

    def do_show_article(self):
        MenuArticle(self.option_menu_frame, self.data_frame,self.bt_item,self.bt_customer,self.bt_invoice,self.bt_close)
        self.bt_item.configure(state='disabled')
        self.bt_customer.configure(state='disabled')
        self.bt_invoice.configure(state='disabled')
        self.bt_close.configure(state='disabled')
    def do_show_customer(self):
        pass

    def do_show_invoice(self):
        pass

    def do_close(self):
        exit()


class MenuArticle:
    def __init__(self, menu_frame: ttk.Frame, data_frame: ttk.Frame,bt_item : ttk.Button,bt_customer : ttk.Button, bt_invoice : ttk.Button, bt_close : ttk.Button):
        # variable get from main menu frame
        self.menu_frame = menu_frame
        self.data_Frame = data_frame
        self.bt_item_main_menu = bt_item
        self.bt_customer_main_menu = bt_customer
        self.bt_invoice_main_menu = bt_invoice
        self.bt_close_main_menu = bt_close
        # widget button
        self.bt_add = ttk.Button(menu_frame, text="AJOUTER", command=self.do_show_add_data)
        self.bt_change = ttk.Button(
            menu_frame, text="MODIFIER", command=self.do_show_change_data
        )
        self.bt_remove = ttk.Button(
            menu_frame, text="SUPPRIMER", command=self.do_show_remove_data
        )
        self.bt_item_search = ttk.Button(
            menu_frame, text="RECHERCHER", command=self.do_show_search_item_data
        )
        self.bt_back = ttk.Button(
            menu_frame, text="RETOUR", command=self.do_back_menu
        )
        # position button
        self.bt_add.pack(side=cttk.TOP)
        self.bt_change.pack(side=cttk.TOP)
        self.bt_remove.pack(side=cttk.TOP)
        self.bt_item_search.pack(side=cttk.TOP)
        self.bt_back.pack(side=cttk.BOTTOM)

    def do_show_add_data(self):
        # split window in multiple frames
        self.top_frame = ttk.Frame(self.data_Frame)
        self.bottom_frame = ttk.Frame(self.data_Frame)
        # position frames
        self.top_frame.pack(side=cttk.TOP,expand=True,fill=cttk.BOTH)
        self.bottom_frame.pack(side=cttk.BOTTOM,expand=True,fill=cttk.X)
        # config position
        self.top_frame.columnconfigure(1, weight=2)
        self.top_frame.rowconfigure(0,weight=1)
        self.top_frame.rowconfigure(5,weight=1)
        # widget button
        bt_confirm = ttk.Button(self.bottom_frame, text="CONFIRMATION")
        bt_back= ttk.Button(self.bottom_frame, text="RETOUR")
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
        lb_top_empty.grid(columnspan=2,row=0,sticky=cttk.NSEW)
        lb_name.grid(column=0, row=1,pady=10)
        lb_description.grid(column=0, row=2,pady=10)
        lb_prix_htva.grid(column=0, row=3,pady=10)
        lb_taux_tva.grid(column=0, row=4,pady=10)
        lb_bottom_empty.grid(columnspan=2,row=5,sticky=cttk.NSEW)
        # position entry
        en_name.grid(column=1, row=1, sticky=cttk.EW,pady=10)
        en_description.grid(column=1, row=2, sticky=cttk.EW,pady=10)
        en_prix_htva.grid(column=1, row=3, sticky=cttk.EW,pady=10)
        en_taux_tva.grid(column=1, row=4, sticky=cttk.EW,pady=10)
        # position button
        bt_confirm.pack(side=cttk.RIGHT,fill=cttk.X,expand=True,padx=20)
        bt_back.pack(side=cttk.LEFT,fill=cttk.X,expand=True,padx=20)

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
        self.bt_item_main_menu['state'] ='normal'
        self.bt_customer_main_menu['state'] = 'normal'
        self.bt_invoice_main_menu['state'] = 'normal'
        self.bt_close_main_menu['state'] = 'normal'
