# main.py

import tkinter as tk
from gui import MetroSantiyeApp # gui.py dosyasındaki ana uygulamayı import ediyoruz

if __name__ == "__main__":
    root = tk.Tk()
    app = MetroSantiyeApp(root)
    root.mainloop()