import tkinter as tk
from gui import MetroSantiyeApp
from database import Database

def main():
    # Veritabanı bağlantısını başlat
    db = Database("data/santiye.db")
    db.create_tables()

    # Tkinter uygulamasını başlat
    root = tk.Tk()
    app = MetroSantiyeApp(root, db)
    root.mainloop()

if __name__ == "__main__":
    main()