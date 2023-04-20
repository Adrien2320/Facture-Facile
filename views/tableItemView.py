import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk
import views.dataItemView
import views.dataItemView as dataItem
from models.itemModel import Item
import views.windowView as windowView
import views.menuItemView as menuItem


class TableItem(ttk.Frame):
    table: ttk.Treeview
    bt_confirm_selected : ttk.Button

    def __init__(self, window, controller, menu_item):
        super().__init__(window)
        # variable
        self.window = window
        self.controller = controller
        self.menu_item = menu_item

        self.create_table()
        self.insert_item_in_table()



    def show_search_data(self):
        """ Insert les données récolté dans la vue dataItem """
        try:
            item = self.get_selected()
            views.dataItemView.DataItem(self.window,self.menu_item).set_variable_ttk(item.id_item,item.name_item,item.description_item,item.htva_price,item.tva_tare)
            views.dataItemView.DataItem(self.window,self.menu_item).create_data_item()
            views.dataItemView.DataItem(self.window, self.menu_item).bt_confirm_item.destroy()
        except AttributeError:
            windowView.Window.show_message_failure("Veuillez sélectionnez un élément!")
            menuItem.MenuItem.state_item_menu(self.menu_item, "normal")
