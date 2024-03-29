import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk
import views.mainMenuView as mainMenu
import views.customer.dataCustomerView as dataCustomer
import controllers.customerController as controllerCustomer
import models.customerModel as modelCustomer
import controllers.zipcodeController as controllerZipcode
import models.zipcodeModel as modelZipcode


class MenuCustomer(ttk.Frame):
    bt_add: ttk.Button
    bt_change: ttk.Button
    bt_remove: ttk.Button
    bt_item_search: ttk.Button
    bt_back: ttk.Button

    def __init__(self, window):
        """Constructeur"""
        # style frame
        ttk.Style().configure("customer.TFrame", background="#283747")
        # paramètre de la frame
        super().__init__(window, style="customer.TFrame")
        # position de la frame
        self.pack(side=cttk.LEFT, fill=cttk.Y)
        # variable
        self.window = window

    def create_menu_customer(self):
        """Creation du menu article"""
        # style du menu article
        ttk.Style().configure(
            "add.TButton",
            background="#8BC34A",
            bordercolor="#8BC34A",
            relief="flat",
            font=("Georgia", 15),
        )
        ttk.Style().configure(
            "change.TButton",
            background="#E59866",
            bordercolor="#E59866",
            relief="flat",
            font=("Georgia", 15),
        )
        ttk.Style().configure(
            "remove.TButton",
            background="#7E57C2",
            bordercolor="#7E57C2",
            relief="flat",
            font=("Georgia", 15),
        )
        ttk.Style().configure(
            "search.TButton",
            background="#42B7C6",
            bordercolor="#42B7C6",
            relief="flat",
            font=("Georgia", 15),
        )
        ttk.Style().configure(
            "back.TButton",
            background="#C0392B",
            bordercolor="#C0392B",
            relief="flat",
            font=("Georgia", 15),
        )
        # widget label
        lb_title = ttk.Label(
            self,
            text="Menu Client",
            font=("Georgia", 20),
            background="#283747",
        )
        # widget button
        self.bt_add_customer = ttk.Button(
            self,
            text="Ajouter",
            command=self.new_customer,
            width=12,
            style="add.TButton",
        )
        self.bt_change_customer = ttk.Button(
            self,
            text="Modifier",
            command=self.modif_customer,
            width=12,
            style="change.TButton",
        )
        self.bt_remove_customer = ttk.Button(
            self,
            text="Supprimer",
            command=self.delete_customer,
            width=12,
            style="remove.TButton",
        )
        self.bt_search_customer = ttk.Button(
            self,
            text="Rechercher",
            command=self.search_customer,
            width=12,
            style="search.TButton",
        )
        self.bt_back_customer = ttk.Button(
            self,
            text="Menu Principal",
            command=self.back_main_menu,
            width=12,
            style="back.TButton",
        )
        # position label
        lb_title.pack(side=cttk.TOP, padx=10, pady=10)
        # position button
        self.bt_add_customer.pack(side=cttk.TOP, padx=10, pady=30)
        self.bt_change_customer.pack(side=cttk.TOP, padx=10)
        self.bt_remove_customer.pack(side=cttk.TOP, padx=10, pady=30)
        self.bt_search_customer.pack(side=cttk.TOP, padx=10)
        self.bt_back_customer.pack(side=cttk.BOTTOM, padx=10, pady=30)

    def new_customer(self):
        """Créer un nouveau client"""
        self.state_customer_menu("disabled")

        dataCustomer.DataCustomer.controllerZipcode = (
            controllerZipcode.ZipCodeController(modelZipcode.ZipCodes())
        )
        dataCustomer.DataCustomer.controllerCustomer = (
            controllerCustomer.CustomerController(modelCustomer.Customers())
        )
        dataCustomer.DataCustomer(self.window, self).show_new_customer()

    def modif_customer(self):
        """Lance la procédure pour modifier un client"""
        self.state_customer_menu("disabled")
        dataCustomer.DataCustomer.controllerZipcode = (
            controllerZipcode.ZipCodeController(modelZipcode.ZipCodes())
        )
        dataCustomer.DataCustomer.controllerCustomer = (
            controllerCustomer.CustomerController(modelCustomer.Customers())
        )
        dataCustomer.DataCustomer(self.window, self).show_modif_customer()

    def delete_customer(self):
        """Lance la procédure pour supprimer un client"""
        self.state_customer_menu("disabled")
        dataCustomer.DataCustomer.controllerZipcode = (
            controllerZipcode.ZipCodeController(modelZipcode.ZipCodes())
        )
        dataCustomer.DataCustomer.controllerCustomer = (
            controllerCustomer.CustomerController(modelCustomer.Customers())
        )
        dataCustomer.DataCustomer(self.window, self).show_delete_customer()

    def search_customer(self):
        """Recherche un client"""
        self.state_customer_menu("disabled")

        dataCustomer.DataCustomer.controllerZipcode = (
            controllerZipcode.ZipCodeController(modelZipcode.ZipCodes())
        )
        dataCustomer.DataCustomer.controllerCustomer = (
            controllerCustomer.CustomerController(modelCustomer.Customers())
        )
        dataCustomer.DataCustomer(self.window, self).show_search_customer()

    def back_main_menu(self):
        """Reviens au menu principale"""
        self.destroy()
        mainMenu.MainMenu(self.window)

    def state_customer_menu(self, state: str):
        """Modifie le state des widgets du menu"""
        self.bt_add_customer.configure(state=state)
        self.bt_change_customer.configure(state=state)
        self.bt_remove_customer.configure(state=state)
        self.bt_search_customer.configure(state=state)
        self.bt_back_customer.configure(state=state)
