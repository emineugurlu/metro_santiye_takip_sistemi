# Metro Şantiye Takip Sistemi

Bu proje, metro şantiyelerinde personel, ekipman ve görev takibini dijitalleştirmek için geliştirilmiş bir masaüstü uygulamasıdır. Python programlama dili, Tkinter GUI kütüphanesi ve SQLite veritabanı kullanılarak geliştirilmiştir.

## Proje Yapısı

Kodlama desteği
Harika bir fikir! Metro Şantiye Takip Sistemi projen için sana kapsamlı bir proje dökümanı hazırlayabilir ve başlangıç kodu iskeletini oluşturabilirim.

Metro Şantiye Takip Sistemi Proje Dökümanı
1. Proje Tanımı ve Amacı
Metro Şantiye Takip Sistemi, metro şantiyelerindeki personel, ekipman ve görev yönetimini dijitalleştirmeyi amaçlayan bir masaüstü uygulamasıdır. Günümüzde hala sıklıkla kullanılan kâğıt tabanlı takip yöntemlerinin getirdiği zaman kaybı, hata oranı ve verimsizlik gibi sorunları ortadan kaldırmak için modern, yazılım tabanlı bir çözüm sunar.

Projenin temel amacı, şantiye ortamında daha düzenli, güvenli ve verimli bir çalışma akışı sağlamaktır. Sistem, personel bilgilerinin, ekipman zimmetlemelerinin, görev atamalarının ve acil durum bildirimlerinin kolayca yönetilmesine olanak tanıyacak, böylece şantiye operasyonlarının genel performansını artıracaktır.

2. Hedef Kitle
Bu sistemin birincil hedef kitlesi, metro şantiyelerinde operasyonel süreçleri yöneten ve takip eden profesyonellerdir. Bunlar:

Şantiye Şefleri ve Mühendisler: Günlük operasyonları denetlemek, görev atamak ve genel ilerlemeyi takip etmek için.

Ekipman Sorumluları: Ekipmanların teslimatını, zimmetlenmesini ve iadesini yönetmek için.

İş Güvenliği Uzmanları: Acil durum bildirimlerini kaydetmek ve takip etmek, potansiyel riskleri izlemek için.

Personel Kayıt Görevlileri: Personel bilgilerini kaydetmek, güncellemek ve yönetmek için.

3. Kullanılan Teknolojiler
Proje geliştirme sürecinde aşağıdaki teknoloji ve araçlar kullanılacaktır:

Python: Uygulamanın ana programlama dili olarak kullanılacaktır.

Tkinter: Grafik kullanıcı arayüzü (GUI) geliştirmek için Python'ın standart kütüphanesi.

SQLite: Veri depolama ve yönetimi için hafif, dosya tabanlı bir ilişkisel veritabanı.

CSV Modülü: Raporlama modülü aracılığıyla verileri CSV formatında dışa aktarmak için.

ReportLab (İsteğe Bağlı): Personel ve görev raporlarını PDF formatında oluşturmak için kullanılabilir.

Google Gemini: Geliştirme süreci boyunca kodlama, hata ayıklama ve mimari kararlarında yapay zeka destekli yardım almak için.

Visual Studio Code / PyCharm: Geliştirme ortamı (IDE) olarak tercih edilebilecek güçlü araçlardır.

4. Modül Açıklamaları
Sistem, aşağıda belirtilen temel modüllerden oluşacaktır:

4.1. Personel Takip Modülü
Açıklama: Şantiyede çalışan personelin bilgilerini yönetmek için tasarlanmıştır.

Özellikler:

Personel Bilgileri: Her personel için benzersiz bir ID, ad, görev ve vardiya bilgileri saklanır.

Ekleme: Yeni personel kaydı oluşturma.

Düzenleme: Mevcut personel bilgilerini güncelleme.

Silme: Personel kaydını sistemden kaldırma.

Arama/Filtreleme: Personel listesinde belirli kriterlere göre arama yapma.

4.2. Ekipman Zimmet Modülü
Açıklama: Şantiye ekipmanlarının (kask, telsiz, güvenlik yeleği vb.) takibini ve zimmetlenmesini yönetir.

Özellikler:

Ekipman Bilgileri: Her ekipman için benzersiz bir ID, tür ve zimmetli olduğu kişi bilgileri tutulur.

Teslim Alma/Zimmetleme: Bir ekipmanın personele zimmetlenmesini kaydetme.

Teslim Etme/İade: Zimmetli bir ekipmanın personele iadesini kaydetme.

Durum Takibi: Ekipmanların mevcut durumunu (boşta, zimmetli, arızalı vb.) izleme.

4.3. Görev Yönetim Modülü
Açıklama: Şantiye görevlerini planlamak, atamak ve ilerlemesini takip etmek için kullanılır.

Özellikler:

Görev Bilgileri: İş adı, sorumlu kişi, başlama ve bitiş tarihi bilgileri.

Görev Ekleme: Yeni görevler oluşturma ve ilgili personele atama.

Durum Güncelleme: Görevlerin tamamlanma durumunu (başlamadı, devam ediyor, tamamlandı, ertelendi) güncelleme.

Takvim Görünümü (İsteğe Bağlı): Görevleri takvim üzerinde görselleştirme.

4.4. Acil Durum Bildirim Modülü
Açıklama: Şantiyede meydana gelebilecek acil durumları (yangın, göçük, kaza vb.) kaydetmek ve takip etmek için.

Özellikler:

Bildirim Kaydı: Acil durum türü, detaylı açıklama, tarih ve müdahale durumu (beklemede, müdahale edildi, çözüldü) kaydetme.

Görsel/Sesli Uyarı (İsteğe Bağlı): Acil durum bildirildiğinde yöneticilere görsel veya sesli uyarı gönderme.

4.5. Raporlama Modülü
Açıklama: Sisteme girilen verilerden çeşitli raporlar oluşturarak şantiye operasyonları hakkında bilgi edinmeyi sağlar.

Özellikler:

Veri Dışa Aktarma: Personel ve görev bilgilerini CSV formatında dışa aktarma.

PDF Raporlama (İsteğe Bağlı): Belirli kriterlere göre (örneğin haftalık personel devamlılık raporları, aylık görev tamamlama raporları) PDF formatında raporlar oluşturma.

5. Sistem Mimarisi
Metro Şantiye Takip Sistemi, katmanlı bir mimari yaklaşımıyla geliştirilecektir. Bu, kodun daha düzenli, bakımı kolay ve ölçeklenebilir olmasını sağlayacaktır.

Sunum Katmanı (GUI - Tkinter): Kullanıcının sistemle etkileşim kurduğu kısımdır. Tkinter kullanılarak tasarlanacak ve kullanıcının veri girişi yapmasını, raporları görüntülemesini ve sistem fonksiyonlarını tetiklemesini sağlayacaktır.

İş Mantığı Katmanı (Python Modülleri): Uygulamanın temel iş kurallarını ve süreçlerini barındırır. Modül açıklamalarında belirtilen personel takibi, ekipman zimmetleme, görev yönetimi gibi fonksiyonellikler bu katmanda işlenecektir. Bu katman, GUI'den gelen istekleri alır, veritabanı katmanıyla iletişim kurar ve sonuçları GUI'ye geri gönderir.

Veri Erişim Katmanı (SQLite ve database.py): Veritabanı ile doğrudan iletişim kurmaktan sorumlu katmandır. SQL sorgularını oluşturur, veritabanına veri ekler, günceller, siler ve sorgular. database.py dosyası bu katmanın temelini oluşturacaktır.

Veri Akışı:

Kullanıcı, GUI aracılığıyla bir eylem başlatır (örneğin, "Yeni Personel Ekle" düğmesine tıklar).

GUI, bu isteği İş Mantığı Katmanı'na iletir.

İş Mantığı Katmanı, gerekli veri doğrulamasını yapar ve Veri Erişim Katmanı'na veritabanı işlemi için bir talimat gönderir.

Veri Erişim Katmanı, SQLite veritabanı ile etkileşime girer ve işlemi gerçekleştirir.

İşlemin sonucu Veri Erişim Katmanı'ndan İş Mantığı Katmanı'na geri döner.

İş Mantığı Katmanı, gerekirse verileri işler ve sonucu GUI'ye gönderir.

GUI, kullanıcıya işlemin sonucunu (örneğin, "Personel başarıyla eklendi") görüntüler.

6. Veritabanı Şeması (SQLite)
Veritabanı, aşağıdaki tabloları içerecektir:

personnel Tablosu:

id INTEGER PRIMARY KEY AUTOINCREMENT

name TEXT NOT NULL

role TEXT NOT NULL

shift TEXT

equipment Tablosu:

id INTEGER PRIMARY KEY AUTOINCREMENT

name TEXT NOT NULL

assigned_to INTEGER -- FOREIGN KEY to personnel.id, NULL if not assigned

status TEXT NOT NULL -- e.g., 'Mevcut', 'Zimmetli', 'Arızalı'

tasks Tablosu:

id INTEGER PRIMARY KEY AUTOINCREMENT

task_name TEXT NOT NULL

assigned_person INTEGER -- FOREIGN KEY to personnel.id

deadline TEXT -- YYYY-MM-DD formatında

status TEXT NOT NULL -- e.g., 'Başlamadı', 'Devam Ediyor', 'Tamamlandı'

emergency_reports Tablosu:

id INTEGER PRIMARY KEY AUTOINCREMENT

report_type TEXT NOT NULL -- e.g., 'Yangın', 'Göçük', 'Kaza'

description TEXT

date TEXT NOT NULL -- YYYY-MM-DD HH:MM:SS formatında

handled TEXT NOT NULL -- e.g., 'Beklemede', 'Müdahale Edildi', 'Çözüldü'

7. Örnek Ekran Görüntüsü (Açıklama)
Uygulama başlatıldığında, ana pencere sol tarafta bir navigasyon menüsü (Personel, Ekipman, Görevler, Acil Durumlar, Raporlar gibi) içerecektir. Sağ tarafta ise seçilen modüle göre dinamik olarak değişen içerik alanı bulunacaktır.

Örneğin, Personel Takip Modülü seçildiğinde:

Sağ taraftaki içerik alanında, mevcut personelin bir listesi (ID, Ad, Görev, Vardiya sütunları ile bir tablo/liste görünümü) görüntülenecektir.

Listenin üzerinde veya altında "Yeni Personel Ekle", "Seçili Personeli Düzenle", "Seçili Personeli Sil" ve "Ara" gibi düğmeler bulunacaktır.

"Yeni Personel Ekle" düğmesine tıklandığında, yeni bir pencere veya pop-up açılarak personel adı, görevi ve vardiyası gibi bilgilerin girileceği form alanları sunulacaktır.

Her modül, benzer bir arayüz mantığıyla (liste görünümü, ekleme/düzenleme/silme düğmeleri ve arama/filtreleme seçenekleri) tasarlanacaktır.

8. Kullanım Senaryoları (Örnek İşlem Akışı)
Senaryo 1: Yeni Personel Kaydı Ekleme
Şantiye şefi, uygulamayı başlatır.

Sol menüden "Personel" modülünü seçer.

"Yeni Personel Ekle" düğmesine tıklar.

Açılan form penceresine personelin adını ("Ayşe Yılmaz"), görevini ("İnşaat Mühendisi") ve vardiyasını ("Gündüz") girer.

"Kaydet" düğmesine tıklar.

Sistem, yeni personeli veritabanına ekler ve personel listesini günceller. "Personel başarıyla eklendi" mesajı görünür.

Senaryo 2: Ekipman Zimmetleme
Ekipman sorumlusu, uygulamayı başlatır.

Sol menüden "Ekipman" modülünü seçer.

Ekipman listesinden zimmetlenecek "Telsiz - ID: 005" ekipmanını seçer.

"Zimmetle" düğmesine tıklar.

Açılan pencereden "Ayşe Yılmaz" personelini seçer (personel arayüzünden seçilebilir veya ID girilebilir).

"Zimmetle" düğmesine tıklar.

Sistem, telsizi Ayşe Yılmaz'a zimmetler ve ekipmanın durumunu "Zimmetli" olarak günceller.

Senaryo 3: Görev Durumu Güncelleme
Şantiye şefi, uygulamayı başlatır.

Sol menüden "Görevler" modülünü seçer.

"Temel Kazısı" adlı görevi listeden bulur ve seçer.

"Durumu Güncelle" düğmesine tıklar.

Açılan durum seçeneklerinden "Tamamlandı"yı seçer.

"Kaydet" düğmesine tıklar.

Sistem, görevin durumunu "Tamamlandı" olarak günceller ve görev listesini yeniler.

9. Kurulum ve Çalıştırma Talimatları
Projenin kurulumu ve çalıştırılması için aşağıdaki adımlar takip edilmelidir:

Python Kurulumu: Sisteminizde Python 3.x kurulu olmalıdır. python --version komutu ile kontrol edebilirsiniz.

Gereksinimlerin Kurulumu: Projenin bağımlılıklarını (örneğin ReportLab eğer kullanılacaksa) kurmak için aşağıdaki komutu çalıştırın:

Bash

pip install ReportLab # Eğer ReportLab kullanılacaksa
(Tkinter ve SQLite Python ile birlikte gelir, ekstra kurulum gerektirmez.)

Proje Klasörünü İndirme/Kopyalama: Proje dosyalarını (main.py, database.py vb.) bilgisayarınızda bir klasöre kopyalayın.

Uygulamayı Çalıştırma: Terminal veya komut istemcisini açarak projenin ana dizinine gidin ve aşağıdaki komutu çalıştırın:

Bash

python main.py
Bu komut, uygulamanın GUI'sini başlatacaktır.

10. Sonuç ve Geliştirme Önerileri
Metro Şantiye Takip Sistemi, şantiye yönetimi süreçlerini dijitalleştirerek verimliliği ve güvenliği artırmayı hedefleyen güçlü bir başlangıç noktasıdır. Mevcut modüller, temel takip ihtiyaçlarını karşılayacaktır.

Gelecekteki Geliştirme Önerileri:

Kullanıcı Rolleri ve Yetkilendirme: Farklı kullanıcılar (şantiye şefi, ekipman sorumlusu) için farklı erişim seviyeleri tanımlama.

Loglama ve Denetim Kayıtları: Sistemdeki tüm önemli eylemlerin (kim ne zaman hangi değişikliği yaptı) kaydını tutma.

Gelişmiş Raporlama: Özelleştirilebilir raporlar, grafiksel gösterimler ve periyodik raporların otomatik oluşturulması.

Bildirim Sistemi: Görev son teslim tarihleri veya acil durumlar için dahili bildirimler.

Görsel Şantiye Planı Entegrasyonu: Ekipmanların veya personelin şantiye planı üzerinde konumlandırılması.

Mobil Uygulama Entegrasyonu: Mobil cihazlardan temel bilgilere erişim ve güncelleme yeteneği.

Bulut Senkronizasyonu: Verilerin birden fazla cihaz veya konum arasında senkronize edilmesi için bulut tabanlı bir çözümle entegrasyon.

Proje Başlangıç Kodu İskeleti
İşte belirtilen dosya yapısına uygun olarak projenin başlangıç kodu iskeleti. Bu iskelet, modüller arasındaki temel bağlantıları ve veritabanı etkileşimini gösterir.

metro_santiye_takip/
├── main.py
├── database.py
├── gui.py
├── models.py
├── reports.py
├── assets/
└── data/
└── README.md
main.py
Python

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

database.py
Python

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
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS personnel (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
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
                FOREIGN KEY (assigned_person) REFERENCES personnel(id)
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

gui.py
Python

import tkinter as tk
from tkinter import ttk, messagebox
# Diğer modülleri burada import edebiliriz (models, reports vb.)

class MetroSantiyeApp:
    def __init__(self, root, db):
        self.root = root
        self.root.title("Metro Şantiye Takip Sistemi")
        self.db = db

        self.create_widgets()

    def create_widgets(self):
        # Sol menü çerçevesi
        self.menu_frame = tk.Frame(self.root, width=200, bg="#2c3e50")
        self.menu_frame.pack(side="left", fill="y")

        # İçerik çerçevesi
        self.content_frame = tk.Frame(self.root, bg="#ecf0f1")
        self.content_frame.pack(side="right", fill="both", expand=True)

        # Menü düğmeleri
        tk.Button(self.menu_frame, text="Personel", command=self.show_personnel_module,
                  font=("Arial", 12), bg="#34495e", fg="white", bd=0, padx=10, pady=10).pack(fill="x", pady=5)
        tk.Button(self.menu_frame, text="Ekipman", command=self.show_equipment_module,
                  font=("Arial", 12), bg="#34495e", fg="white", bd=0, padx=10, pady=10).pack(fill="x", pady=5)
        tk.Button(self.menu_frame, text="Görevler", command=self.show_tasks_module,
                  font=("Arial", 12), bg="#34495e", fg="white", bd=0, padx=10, pady=10).pack(fill="x", pady=5)
        tk.Button(self.menu_frame, text="Acil Durum", command=self.show_emergency_module,
                  font=("Arial", 12), bg="#34495e", fg="white", bd=0, padx=10, pady=10).pack(fill="x", pady=5)
        tk.Button(self.menu_frame, text="Raporlar", command=self.show_reports_module,
                  font=("Arial", 12), bg="#34495e", fg="white", bd=0, padx=10, pady=10).pack(fill="x", pady=5)
        
        # Başlangıçta personel modülünü göster
        self.show_personnel_module()

    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    # --- Personel Modülü ---
    def show_personnel_module(self):
        self.clear_content_frame()
        tk.Label(self.content_frame, text="Personel Takip Modülü", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=20)

        # Personel listesi için Treeview
        columns = ("ID", "Ad", "Görev", "Vardiya")
        self.personnel_tree = ttk.Treeview(self.content_frame, columns=columns, show="headings")
        for col in columns:
            self.personnel_tree.heading(col, text=col)
            self.personnel_tree.column(col, width=100)
        self.personnel_tree.pack(pady=10, padx=10, fill="both", expand=True)

        self.load_personnel_data()

        # Düğmeler
        button_frame = tk.Frame(self.content_frame, bg="#ecf0f1")
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Yeni Personel Ekle", command=self.add_personnel).pack(side="left", padx=5)
        tk.Button(button_frame, text="Personel Düzenle", command=self.edit_personnel).pack(side="left", padx=5)
        tk.Button(button_frame, text="Personel Sil", command=self.delete_personnel).pack(side="left", padx=5)

    def load_personnel_data(self):
        for row in self.personnel_tree.get_children():
            self.personnel_tree.delete(row)
        personnel = self.db.fetch_all("SELECT id, name, role, shift FROM personnel")
        for p in personnel:
            self.personnel_tree.insert("", "end", values=p)

    def add_personnel(self):
        # Yeni personel ekleme penceresi/dialogu
        add_window = tk.Toplevel(self.root)
        add_window.title("Yeni Personel Ekle")
        add_window.geometry("300x200")

        tk.Label(add_window, text="Ad:").pack(pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.pack(pady=5)

        tk.Label(add_window, text="Görev:").pack(pady=5)
        role_entry = tk.Entry(add_window)
        role_entry.pack(pady=5)

        tk.Label(add_window, text="Vardiya:").pack(pady=5)
        shift_entry = tk.Entry(add_window)
        shift_entry.pack(pady=5)

        def save():
            name = name_entry.get()
            role = role_entry.get()
            shift = shift_entry.get()
            if name and role:
                self.db.execute_query("INSERT INTO personnel (name, role, shift) VALUES (?, ?, ?)", (name, role, shift))
                messagebox.showinfo("Başarılı", "Personel başarıyla eklendi.")
                self.load_personnel_data()
                add_window.destroy()
            else:
                messagebox.showerror("Hata", "Ad ve Görev alanları boş bırakılamaz.")

        tk.Button(add_window, text="Kaydet", command=save).pack(pady=10)

    def edit_personnel(self):
        selected_item = self.personnel_tree.focus()
        if not selected_item:
            messagebox.showwarning("Seçim Yok", "Lütfen düzenlemek istediğiniz bir personel seçin.")
            return

        values = self.personnel_tree.item(selected_item, 'values')
        person_id = values[0]

        edit_window = tk.Toplevel(self.root)
        edit_window.title("Personel Düzenle")
        edit_window.geometry("300x200")

        tk.Label(edit_window, text="Ad:").pack(pady=5)
        name_entry = tk.Entry(edit_window)
        name_entry.insert(0, values[1])
        name_entry.pack(pady=5)

        tk.Label(edit_window, text="Görev:").pack(pady=5)
        role_entry = tk.Entry(edit_window)
        role_entry.insert(0, values[2])
        role_entry.pack(pady=5)

        tk.Label(edit_window, text="Vardiya:").pack(pady=5)
        shift_entry = tk.Entry(edit_window)
        shift_entry.insert(0, values[3])
        shift_entry.pack(pady=5)

        def save():
            name = name_entry.get()
            role = role_entry.get()
            shift = shift_entry.get()
            if name and role:
                self.db.execute_query("UPDATE personnel SET name=?, role=?, shift=? WHERE id=?", (name, role, shift, person_id))
                messagebox.showinfo("Başarılı", "Personel başarıyla güncellendi.")
                self.load_personnel_data()
                edit_window.destroy()
            else:
                messagebox.showerror("Hata", "Ad ve Görev alanları boş bırakılamaz.")

        tk.Button(edit_window, text="Kaydet", command=save).pack(pady=10)


    def delete_personnel(self):
        selected_item = self.personnel_tree.focus()
        if not selected_item:
            messagebox.showwarning("Seçim Yok", "Lütfen silmek istediğiniz bir personel seçin.")
            return

        values = self.personnel_tree.item(selected_item, 'values')
        person_id = values[0]

        if messagebox.askyesno("Onay", f"'{values[1]}' adlı personeli silmek istediğinizden emin misiniz?"):
            # Personel silinmeden önce zimmetli ekipmanı veya atanmış görevi olup olmadığı kontrol edilebilir
            # Basitlik adına burada doğrudan silme işlemi yapılıyor.
            self.db.execute_query("DELETE FROM personnel WHERE id=?", (person_id,))
            messagebox.showinfo("Başarılı", "Personel başarıyla silindi.")
            self.load_personnel_data()

    # --- Diğer Modüller (geçici yer tutucular) ---
    def show_equipment_module(self):
        self.clear_content_frame()
        tk.Label(self.content_frame, text="Ekipman Zimmet Modülü", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=20)
        tk.Label(self.content_frame, text="Bu bölüm ekipman yönetimi özelliklerini içerecektir.", bg="#ecf0f1").pack(pady=10)

    def show_tasks_module(self):
        self.clear_content_frame()
        tk.Label(self.content_frame, text="Görev Yönetim Modülü", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=20)
        tk.Label(self.content_frame, text="Bu bölüm görev yönetimi özelliklerini içerecektir.", bg="#ecf0f1").pack(pady=10)

    def show_emergency_module(self):
        self.clear_content_frame()
        tk.Label(self.content_frame, text="Acil Durum Bildirim Modülü", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=20)
        tk.Label(self.content_frame, text="Bu bölüm acil durum bildirimlerini içerecektir.", bg="#ecf0f1").pack(pady=10)

    def show_reports_module(self):
        self.clear_content_frame()
        tk.Label(self.content_frame, text="Raporlama Modülü", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=20)
        tk.Label(self.content_frame, text="Bu bölüm CSV/PDF raporlama özelliklerini içerecektir.", bg="#ecf0f1").pack(pady=10)

models.py
Python

# Bu dosya, veritabanı tablolarına karşılık gelen Python sınıflarını içerebilir.
# ORM (Object-Relational Mapping) kullanılıyorsa daha karmaşık olabilir.
# Tkinter uygulamaları için bu katman genellikle database.py ile entegre çalışır.

# Örnek bir Personel sınıfı (şu anlık kullanılmayacak ama mimaride yer alabilir)
class Personnel:
    def __init__(self, id, name, role, shift):
        self.id = id
        self.name = name
        self.role = role
        self.shift = shift

    def __repr__(self):
        return f"Personel(ID: {self.id}, Ad: {self.name}, Görev: {self.role}, Vardiya: {self.shift})"

# Diğer modeller (Equipment, Task, EmergencyReport) buraya eklenebilir.
reports.py
Python

import csv
import os
# from reportlab.lib.pagesizes import letter # Eğer ReportLab kullanılacaksa
# from reportlab.pdfgen import canvas # Eğer ReportLab kullanılacaksa

class ReportGenerator:
    def __init__(self, db):
        self.db = db
        # Raporların kaydedileceği dizini kontrol et
        self.report_dir = "data/reports"
        if not os.path.exists(self.report_dir):
            os.makedirs(self.report_dir)

    def export_personnel_to_csv(self, filename="personel_raporu.csv"):
        data = self.db.fetch_all("SELECT id, name, role, shift FROM personnel")
        if not data:
            print("Dışa aktarılacak personel verisi bulunamadı.")
            return False

        file_path = os.path.join(self.report_dir, filename)
        try:
            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Ad", "Görev", "Vardiya"]) # Başlık satırı
                writer.writerows(data)
            print(f"Personel verileri '{file_path}' adresine başarıyla aktarıldı.")
            return True
        except IOError as e:
            print(f"CSV dışa aktarma hatası: {e}")
            return False

    def export_tasks_to_csv(self, filename="gorev_raporu.csv"):
        data = self.db.fetch_all("SELECT id, task_name, assigned_person, deadline, status FROM tasks")
        if not data:
            print("Dışa aktarılacak görev verisi bulunamadı.")
            return False

        file_path = os.path.join(self.report_dir, filename)
        try:
            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Görev Adı", "Atanan Kişi (ID)", "Son Tarih", "Durum"]) # Başlık satırı
                writer.writerows(data)
            print(f"Görev verileri '{file_path}' adresine başarıyla aktarıldı.")
            return True
        except IOError as e:
            print(f"CSV dışa aktarma hatası: {e}")
            return False

    # def generate_personnel_pdf(self, filename="personel_raporu.pdf"):
    #     c = canvas.Canvas(os.path.join(self.report_dir, filename), pagesize=letter)
    #     c.drawString(100, 750, "Metro Şantiye Personel Raporu")
    #     # PDF oluşturma mantığı buraya gelecek
    #     c.save()
    #     print(f"PDF raporu '{filename}' adresine oluşturuldu.")

README.md
Markdown

# Metro Şantiye Takip Sistemi

Bu proje, metro şantiyelerinde personel, ekipman ve görev takibini dijitalleştirmek için geliştirilmiş bir masaüstü uygulamasıdır. Python programlama dili, Tkinter GUI kütüphanesi ve SQLite veritabanı kullanılarak geliştirilmiştir.

## Proje Yapısı

metro_santiye_takip/
├── main.py             # Uygulamanın ana başlangıç noktası
├── database.py         # SQLite veritabanı bağlantı ve işlem yönetimi
├── gui.py              # Tkinter ile grafik kullanıcı arayüzü bileşenleri
├── models.py           # Veritabanı tablolarına karşılık gelen veri modelleri (isteğe bağlı/genişletilebilir)
├── reports.py          # CSV ve PDF raporlama fonksiyonları
├── assets/             # Uygulama ikonları, resimler vb. (Henüz boş)
├── data/               # SQLite veritabanı dosyaları ve rapor çıktıları (varsayılan olarak santiye.db)
└── README.md           # Proje hakkında bilgiler

## Kurulum ve Çalıştırma

1.  **Python Kurulumu:** Sisteminizde Python 3.x yüklü olduğundan emin olun.
    ```bash
    python --version
    ```
2.  **Bağımlılıklar:** Proje, standart Python kütüphaneleri olan `tkinter` ve `sqlite3`'ü kullanır. Ek olarak `csv` modülü de Python'ın yerleşik bir parçasıdır. Eğer PDF raporlama için `ReportLab` kullanmak isterseniz:
    ```bash
    pip install ReportLab
    ```
3.  **Projeyi Kopyalayın:** Bu repoyu yerel diskinize kopyalayın veya indirin.
4.  **Uygulamayı Çalıştırın:** Proje ana dizinine (`metro_santiye_takip/`) gidin ve aşağıdaki komutu çalıştırın:
    ```bash
    python main.py
    ## Özellikler

* **Personel Takibi:** Personel bilgilerini ekleme, düzenleme, silme.
* **Ekipman Zimmetleme:** Ekipmanların zimmetlenmesi ve iadesinin takibi.
* **Görev Yönetimi:** Görev oluşturma, atama ve durum takibi.
* **Acil Durum Bildirimi:** Acil durumları kaydetme ve müdahale durumlarını takip etme.
* **Raporlama:** Personel ve görev verilerini CSV formatında dışa aktarma. (İsteğe bağlı PDF raporlama)

## Geliştirme Notları

* **Veritabanı:** `data/santiye.db` dosyasında saklanır. Uygulama ilk çalıştığında gerekli tablolar otomatik olarak oluşturulur.
* **GUI:** Tkinter kullanılarak geliştirilmiştir. Modüler bir yapı hedeflenmiştir.
* **Genişletilebilirlik:** Her bir modül, gelecekte yeni özelliklerle kolayca genişletilebilir şekilde tasarlanmıştır.

## Katkıda Bulunma

Geliştirme sürecine katkıda bulunmak isterseniz, lütfen bir Pull Request oluşturmadan önce sorunları veya önerileri tartışmak için bir Issue açın.