# database.py dosyası

import sqlite3
from tkinter import messagebox # <-- Bu satırı ekledik
# from datetime import datetime # datetime modülü burada direkt kullanılmadığı için kaldırabiliriz, ama kalsa da sorun olmaz.

class Database: # Sınıf adını sizdeki gibi 'Database' olarak bıraktık
    def __init__(self, db_name="data/santiye.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self._connect()
        # self.create_tables() # Bu satırı __init__ metodunun içinde tutmuştuk.
        # Hata mesajınızda "Database' object has no attribute 'create_tables'" dediği için,
        # create_tables metodunun kendisinin sınıfın içinde tanımlı olmadığından şüpheleniyorum.
        # Lütfen aşağıdaki create_tables metodunun tamamen kopyalandığından emin olun.
        self.create_tables() # <-- Bu satırın burada olması gerekiyor, metot aşağıda tanımlı

    def _connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            # print("Veritabanı bağlantısı başarılı.") # Kullanıcıya göstermeyeceğiz
        except sqlite3.Error as e:
            messagebox.showerror("Veritabanı Bağlantı Hatası", f"Veritabanına bağlanılamadı: {e}\nUygulama kapatılacak.")
            exit() # Bağlantı kurulamadıysa uygulamayı kapat

    def create_tables(self): # <-- Bu metodun burada, 'Database' sınıfının içinde tanımlı olduğundan emin olun!
        """Uygulamanın ihtiyaç duyduğu tüm tabloları oluşturur."""
        try:
            # Personel tablosu
            # database.py dosyasındaki create_tables metodunun içindeki 'personnel' tablosu
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS personnel (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    surname TEXT,    -- Bu satırın varlığı ve 'TEXT' tipi önemli!
                    role TEXT NOT NULL,
                    shift TEXT,
                    phone TEXT,      -- Bu satırın varlığı ve 'TEXT' tipi önemli!
                    email TEXT       -- Bu satırın varlığı ve 'TEXT' tipi önemli!
                )
            ''')
            # Ekipman tablosu
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS equipment (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    assigned_to INTEGER,
                    status TEXT NOT NULL,
                    last_maintenance_date TEXT,
                    FOREIGN KEY (assigned_to) REFERENCES personnel(id) ON DELETE SET NULL
                )
            ''')
            
            # Görevler tablosu
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_name TEXT NOT NULL,
                    description TEXT,
                    start_date TEXT,
                    end_date TEXT,
                    assigned_person INTEGER,
                    status TEXT NOT NULL DEFAULT 'Pending',
                    FOREIGN KEY (assigned_person) REFERENCES personnel(id) ON DELETE SET NULL
                )
            ''')
            
            # Acil Durum Bildirimleri tablosu
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS emergency_events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    time TEXT NOT NULL,
                    event_type TEXT NOT NULL,
                    description TEXT,
                    affected_personnel_ids TEXT,
                    affected_equipment_ids TEXT,
                    action_taken TEXT,
                    status TEXT DEFAULT 'Open'
                )
            """)
            
            self.conn.commit()
            # print("Veritabanı tabloları kontrol edildi/oluşturuldu.") # Kullanıcıya göstermeyeceğiz
        except sqlite3.Error as e:
            messagebox.showerror("Veritabanı Tablo Oluşturma Hatası", f"Tablolar oluşturulurken hata oluştu: {e}")

    def execute_query(self, query, params=()):
        try:
            if self.conn:
                self.cursor.execute(query, params)
                self.conn.commit()
                return True
            else:
                messagebox.showerror("Veritabanı Hatası", "Veritabanı bağlantısı açık değil.")
                return False
        except sqlite3.Error as e:
            messagebox.showerror("Sorgu Yürütme Hatası", f"Sorgu çalıştırılırken hata oluştu: {e}\nSorgu: {query}\nParametreler: {params}")
            return False

    def fetch_all(self, query, params=()):
        try:
            if self.conn:
                self.cursor.execute(query, params)
                return self.cursor.fetchall()
            else:
                messagebox.showerror("Veritabanı Hatası", "Veritabanı bağlantısı açık değil.")
                return []
        except sqlite3.Error as e:
            messagebox.showerror("Veri Çekme Hatası", f"Veri alınırken hata oluştu: {e}\nSorgu: {query}\nParametreler: {params}")
            return []

    def fetch_one(self, query, params=()):
        try:
            if self.conn:
                self.cursor.execute(query, params)
                return self.cursor.fetchone()
            else:
                messagebox.showerror("Veritabanı Hatası", "Veritabanı bağlantısı açık değil.")
                return None
        except sqlite3.Error as e:
            messagebox.showerror("Tekli Veri Çekme Hatası", f"Tekli veri alınırken hata oluştu: {e}\nSorgu: {query}\nParametreler: {params}")
            return None

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None
            # print("Veritabanı bağlantısı kapatıldı.") # Kullanıcıya göstermeyeceğiz