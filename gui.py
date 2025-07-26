# gui.py

import tkinter as tk
from tkinter import ttk
from database import Database # database.py dosyasındaki Database sınıfını import ediyoruz

# Modül sınıflarını import et
from modules.personnel_module import PersonnelModule
# Diğer modüller daha sonra eklenecek:
# from modules.task_module import TaskModule
# from modules.equipment_module import EquipmentModule
# from modules.emergency_module import EmergencyModule
# from modules.reports_module import ReportsModule

class MetroSantiyeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Metro Şantiye Yönetim Sistemi")
        self.root.geometry("1200x800") # Başlangıç pencere boyutu
        self.root.minsize(1000, 700) # Minimum pencere boyutu

        # Uygulama genelinde kullanılacak bir ttk stili ayarla
        self.style = ttk.Style()
        # Modern bir tema seçimi
        # 'clam', 'alt', 'default', 'xpnative' gibi yerleşik temaları deneyebilirsiniz.
        self.style.theme_use('clam') 
        
        # Eğer daha estetik temalar istiyorsanız (örn: Azure, Forest),
        # bunları projeye dahil etmeniz ve aşağıdaki gibi aktif etmeniz gerekir:
        # self.root.tk.call("source", "path/to/Azure-ttk-theme/azure.tcl")
        # self.style.theme_use("azure dark") # veya "azure light"

        # Veritabanı bağlantısını başlat
        self.db = Database("data/santiye.db") 

        self.create_main_layout()
    
    def create_main_layout(self):
        """Ana uygulama düzenini (sol menü ve sağ içerik alanı) oluşturur."""
        # Ana Frame - Sol menü ve içerik alanı için
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)

        # Ana Frame'in grid ayarları:
        # 0. sütun (menü) sabit genişlikte, 1. sütun (notebook) genişlesin
        main_frame.grid_columnconfigure(0, weight=0) # Menü sütunu sabit
        main_frame.grid_columnconfigure(1, weight=1) # İçerik sütunu genişlesin
        main_frame.grid_rowconfigure(0, weight=1)    # Tek satır dikeyde genişlesin

        # --- Sol Menü (Navigasyon Butonları) ---
        nav_frame = ttk.Frame(main_frame, width=180, relief="raised", borderwidth=1)
        nav_frame.grid(row=0, column=0, sticky="ns", padx=5, pady=5) # Dikeyde yapış
        nav_frame.pack_propagate(False) # Frame'in boyutunu çocuk widget'lara göre ayarlamasını engeller

        ttk.Label(nav_frame, text="Yönetim Menüsü", font=("Arial", 12, "bold")).pack(pady=10)

        # --- Ana İçerik Alanı (Notebook / Sekmeler) ---
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=0, column=1, sticky="nsew", padx=5, pady=5) # Tüm boş alanı kapla

        self.modules = {} # Modül örneklerini saklayacak sözlük

        # --- Sekmelerin Oluşturulması ve Modüllerin Eklenmesi ---
        # Her bir modül kendi ttk.Frame'i olduğu için doğrudan notebook'a eklenebilir.

        # Personel Modülü Sekmesi
        self.personnel_frame = PersonnelModule(self.notebook, self.db)
        self.notebook.add(self.personnel_frame, text="Personel Yönetimi", compound="left") # compound ile ileride ikon eklenebilir
        self.modules["personnel"] = self.personnel_frame # Sözlüğe ekle

        # Görevler Modülü Sekmesi (Şimdilik boş, daha sonra dolduracağız)
        self.task_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.task_frame, text="Görevler")
        ttk.Label(self.task_frame, text="Görevler Modülü Buraya Gelecek", font=("Arial", 16)).pack(expand=True)
        self.modules["tasks"] = self.task_frame

        # Ekipman Modülü Sekmesi (Şimdilik boş)
        self.equipment_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.equipment_frame, text="Ekipman Yönetimi")
        ttk.Label(self.equipment_frame, text="Ekipman Yönetimi Modülü Buraya Gelecek", font=("Arial", 16)).pack(expand=True)
        self.modules["equipment"] = self.equipment_frame

        # Acil Durum Modülü Sekmesi (Şimdilik boş)
        self.emergency_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.emergency_frame, text="Acil Durumlar")
        ttk.Label(self.emergency_frame, text="Acil Durumlar Modülü Buraya Gelecek", font=("Arial", 16)).pack(expand=True)
        self.modules["emergency"] = self.emergency_frame

        # Raporlar Modülü Sekmesi (Şimdilik boş)
        self.reports_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.reports_frame, text="Raporlar")
        ttk.Label(self.reports_frame, text="Raporlar Modülü Buraya Gelecek", font=("Arial", 16)).pack(expand=True)
        self.modules["reports"] = self.reports_frame


        # --- Sol Menüdeki Butonlar ---
        # Bu butonlar, notebook'taki ilgili sekmeyi seçecek
        ttk.Button(nav_frame, text="Personel", command=lambda: self.notebook.select(self.modules["personnel"])).pack(fill="x", pady=5, padx=10)
        ttk.Button(nav_frame, text="Görevler", command=lambda: self.notebook.select(self.modules["tasks"])).pack(fill="x", pady=5, padx=10)
        ttk.Button(nav_frame, text="Ekipman", command=lambda: self.notebook.select(self.modules["equipment"])).pack(fill="x", pady=5, padx=10)
        ttk.Button(nav_frame, text="Acil Durumlar", command=lambda: self.notebook.select(self.modules["emergency"])).pack(fill="x", pady=5, padx=10)
        ttk.Button(nav_frame, text="Raporlar", command=lambda: self.notebook.select(self.modules["reports"])).pack(fill="x", pady=5, padx=10)


    def __del__(self):
        """Uygulama kapanırken veritabanı bağlantısını güvenli bir şekilde kapatır."""
        if hasattr(self, 'db') and self.db:
            self.db.close()