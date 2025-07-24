import sqlite3

class Database:
    def __init__(self, db_name="data/santiye.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self._connect()

    def _connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Veritabanı bağlantı hatası: {e}")

    def create_tables(self):
        # Personel tablosu
        # 'AUTOINCREMENT' kelimesini kaldırıyoruz.
        # Böylece SQLite boş ID'leri tekrar kullanabilir.
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS personnel (
                id INTEGER PRIMARY KEY, -- AUTOINCREMENT kaldırıldı
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
                FOREIGN KEY (assigned_to) REFERENCES personnel(id)
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
        # Acil durum raporları tablosu
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS emergency_reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                report_type TEXT NOT NULL,
                description TEXT,
                date TEXT NOT NULL,
                handled TEXT NOT NULL
            )
        ''')
        self.conn.commit()
        print("Veritabanı tabloları kontrol edildi/oluşturuldu.")


    def execute_query(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Sorgu hatası: {e}")
            return False

    def fetch_all(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def close(self):
        if self.conn:
            self.conn.close()
            print("Veritabanı bağlantısı kapatıldı.")