from view.view import MainView
from model.model import Data
from controller.controller import Controller

if __name__ == '__main__':
    view = MainView("Facture Facile",720,1080)
    data = Data()
    controller = Controller(view,data)

    view.controller =controller

    view.start_main_view()
