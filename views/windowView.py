import ttkbootstrap as ttk
import ttkbootstrap.dialogs as dialogs
import views.mainMenuView


class Window(ttk.Window):
    def __init__(self, title: str, height: int, width: int):
        """ Constructeur de la fenêtre """
        # Paramètre object lui-même
        super().__init__(themename="superhero")
        self.title(title)
        self.minsize(width, height)
        # création du menu principale
        views.mainMenuView.MainMenu(self)

    def start_main(self):
        """ Lance la fenêtre """
        self.mainloop()

    @staticmethod
    def show_message_success(text: str):
        """Message pour confirmer une action"""
        dialogs.Messagebox.show_info(text, "Réussi")

    @staticmethod
    def show_message_failure(text: str):
        """Message pour avertir qu'une action à échouer"""
        dialogs.Messagebox.show_info(text, "Echec")

    @staticmethod
    def show_message_error(text: str):
        """Message qui avertir qu'il y a un bug dans l'application"""
        dialogs.Messagebox.show_error(text, "Erreur")
