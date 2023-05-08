from views.windowView import Window
import sqlite3
import os

# create db if not exist
if not os.path.exists("data_facture_facile.db"):
    Window.show_message_success("Veuillez Patientez création de la base de données")
    with open("script_db.sql", "r") as sql_file:
        sql_script = sql_file.read()

    db = sqlite3.connect("data_facture_facile.db")
    cursor = db.cursor()
    cursor.executescript(sql_script)
    db.commit()
    db.close()

if __name__ == "__main__":
    view = Window("Facture Facile", 720, 1080)
    view.start_main()
