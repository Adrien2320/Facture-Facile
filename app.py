from views.windowView import Window
import sqlite3
import os


def start_load_screen(message: str):
    pass


def stop_load_screen():
    pass


def create_dataBase():
    with open("script_db.sql", "r") as sql_file:
        sql_script = sql_file.read()

    db = sqlite3.connect("data_facture_facile.db")
    cursor = db.cursor()
    cursor.executescript(sql_script)
    db.commit()
    db.close()


# create db if not exist
if not os.path.exists("data_facture_facile.db"):
    start_load_screen("Veuillez Patientez création de la base de données")
    create_dataBase()

if __name__ == "__main__":
    view = Window("Facture Facile", 720, 1080)
    view.start_main()
