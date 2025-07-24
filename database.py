# database.py dosyası

import sqlite3

class Database:
    def __init__(self, db_name="data/santiye.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self._connect()
        self.create_tables() # __init__ içinde create_tables'ı çağırmayı unutma

    def _connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print("Veritabanı bağlantısı başarılı.")
        except sqlite3.Error as e:
            print(f"Veritabanı bağlantı hatası: {e}")

    def create_tables(self):
        # Personel tablosu
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS personnel (
                id INTEGER PRIMARY KEY AUTOINCREMENT, -- SQLite'da INTEGER PRIMARY KEY otomatik AUTOINCREMENT yapar, ama belirtmekte sakınca yok. Daha önce kaldırılmıştı, geri ekledim.
                name TEXT NOT NULL,
                role TEXT NOT NULL,
                shift TEXT
            )
        ''')
        
        # Ekipman tablosu
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS equipment (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                assigned_to INTEGER,
                status TEXT NOT NULL,
                FOREIGN KEY (assigned_to) REFERENCES personnel(id) ON DELETE SET NULL -- ON DELETE SET NULL eklendi
            )
        ''')
        # Görevler tablosu
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_name TEXT NOT NULL,
                assigned_person INTEGER,
                deadline TEXT,
                status TEXT NOT NULL,
                FOREIGN KEY (assigned_person) REFERENCES personnel(id) ON DELETE SET NULL
            )
        ''')
        # Acil Durum Bildirimleri tablosu - Bu kısmı DÜZELTİYORUZ!
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS emergency_events (  -- Tablo adını 'emergency_events' olarak değiştirdik
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                time TEXT NOT NULL,
                event_type TEXT NOT NULL,                  -- Sütun adını 'event_type' olarak değiştirdik
                description TEXT,
                affected_personnel_ids TEXT,               -- Bu sütun eklendi
                affected_equipment_ids TEXT,               -- Bu sütun eklendi
                action_taken TEXT                          -- Bu sütun eklendi
            )
        """)
        self.conn.commit()
        print("Veritabanı tabloları kontrol edildi/oluşturuldu.")

    # Diğer fonksiyonlar aynı kalacak

    def execute_query(self, query, params=()):
        try:
            if self.conn: # Bağlantının açık olduğundan emin ol
                self.cursor.execute(query, params)
                self.conn.commit()
                return True
            else:
                print("Hata: Veritabanı bağlantısı açık değil.")
                return False
        except sqlite3.Error as e:
            print(f"Sorgu hatası: {e}")
            return False

    def fetch_all(self, query, params=()):
        try:
            if self.conn:
                self.cursor.execute(query, params)
                return self.cursor.fetchall()
            else:
                print("Hata: Veritabanı bağlantısı açık değil.")
                return []
        except sqlite3.Error as e:
            print(f"Sorgu hatası: {e}")
            return []

    def fetch_one(self, query, params=()):
        try:
            if self.conn:
                self.cursor.execute(query, params)
                return self.cursor.fetchone()
            else:
                print("Hata: Veritabanı bağlantısı açık değil.")
                return None
        except sqlite3.Error as e:
            print(f"Sorgu hatası: {e}")
            return None

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None # Bağlantıyı kapatınca None yapalım
            self.cursor = None # İmleci de None yapalım
            print("Veritabanı bağlantısı kapatıldı.")