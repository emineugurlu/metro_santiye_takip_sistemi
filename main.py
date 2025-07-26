import tkinter as tk
from gui import MetroSantiyeApp
# from database import Database # Bu satıra artık main.py'de ihtiyacınız yok, çünkü db nesnesi gui.py içinde oluşturulacak.

def main():
    # Veritabanı bağlantısını burada başlatmaya gerek yok.
    # Bu işlem MetroSantiyeApp sınıfının içinde yapılacak.
    # db = Database("data/santiye.db") # Bu satırı kaldırın veya yorum satırı yapın
    # db.create_tables() # Bu satırı kaldırın veya yorum satırı yapın

    # Tkinter uygulamasını başlat
    root = tk.Tk()
    
    # MetroSantiyeApp sınıfını başlatırken SADECE 'root' nesnesini gönderin.
    # Veritabanı bağlantısı MetroSantiyeApp sınıfının kendi içinde yönetiliyor.
    app = MetroSantiyeApp(root) # <-- SADECE root argümanı olmalı!
    
    root.mainloop()

if __name__ == "__main__":
    main()