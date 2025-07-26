# modules/personnel_module.py

import tkinter as tk
from tkinter import ttk, messagebox
from database import Database # database.py dosyasındaki Database sınıfını import ediyoruz

class PersonnelModule(ttk.Frame):
    def __init__(self, parent, db_manager):
        """
        Personel Yönetimi Modülü için arayüzü ve mantığı oluşturur.
        parent: Bu modülün ekleneceği ana Tkinter widget'ı (genellikle ttk.Notebook sekmesi)
        db_manager: Database sınıfının bir örneği
        """
        super().__init__(parent)
        self.db = db_manager # Database sınıfı örneğini alıyoruz
        
        self.current_personnel_id = None # Seçilen personelin ID'sini tutar (güncelleme/silme için)

        self.create_widgets() # Arayüz elementlerini oluşturur
        self.load_personnel() # Uygulama başladığında/modül seçildiğinde personelleri yükler

    def create_widgets(self):
        """Personel modülünün UI elementlerini (giriş alanları, butonlar, Treeview) oluşturur."""

        # Ana çerçevenin grid ayarları (içindeki widget'ların genişlemesi için)
        self.columnconfigure(0, weight=1) # Tek sütunun yatayda genişlemesini sağlar
        self.rowconfigure(1, weight=1)    # Treeview'ın olduğu ikinci satırın dikeyde genişlemesini sağlar

        # --- Personel Bilgi Giriş ve Buton Çerçevesi (Üst Kısım) ---
        input_frame = ttk.LabelFrame(self, text="Personel Bilgileri")
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew") # Yatayda genişle

        # Giriş çerçevesinin içindeki grid ayarları
        input_frame.columnconfigure(1, weight=1) # Giriş alanlarının olduğu sütunlar genişlesin
        input_frame.columnconfigure(3, weight=1) 
        
        # Personel Bilgi Giriş Alanları
        self.personnel_entries = {} # Giriş alanlarını depolamak için sözlük
        labels_and_positions = [
            ("Ad:", "name", 0, 0), ("Soyad:", "surname", 0, 2),
            ("Görev:", "role", 1, 0), ("Vardiya:", "shift", 1, 2),
            ("Telefon:", "phone", 2, 0), ("E-posta:", "email", 2, 2)
        ]
        for text, key, row, col in labels_and_positions:
            ttk.Label(input_frame, text=text).grid(row=row, column=col, padx=5, pady=5, sticky="w")
            entry = ttk.Entry(input_frame, width=35) # Genişlik biraz artırıldı
            entry.grid(row=row, column=col+1, padx=5, pady=5, sticky="ew")
            self.personnel_entries[key] = entry # Sözlük anahtarı olarak 'key' (name, role, vb.) kullanılıyor

        # --- Buton Çerçevesi ---
        button_frame = ttk.Frame(input_frame)
        button_frame.grid(row=3, column=0, columnspan=4, pady=10) # Tüm giriş alanlarını kaplayan satırın altına, 4 sütunu da kapla
        
        ttk.Button(button_frame, text="Yeni Personel Ekle", command=self.add_personnel).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Seçileni Güncelle", command=self.update_personnel).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Seçileni Sil", command=self.delete_personnel).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Alanları Temizle", command=self.clear_personnel_entries).pack(side="left", padx=5)

        # --- Personel Listesi (Treeview) ---
        tree_frame = ttk.Frame(self)
        tree_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew") # Dikey ve yatayda genişle

        # Treeview'ın kendisinin çerçeve içinde genişlemesi için
        tree_frame.columnconfigure(0, weight=1)
        tree_frame.rowconfigure(0, weight=1)

        self.personnel_tree = ttk.Treeview(
            tree_frame, 
            columns=("ID", "Ad", "Soyad", "Görev", "Vardiya", "Telefon", "E-posta"), 
            show="headings", # Sadece başlıkları göster (indeks numaralarını gizle)
            selectmode="browse" # Tekli seçim modu
        )
        self.personnel_tree.grid(row=0, column=0, sticky="nsew") # Çerçeve içinde tüm alanı kapla

        # Sütun Başlıkları ve Genişlikleri
        tree_columns = {
            "ID": {"width": 40, "anchor": "center"},
            "Ad": {"width": 120, "anchor": "w"},
            "Soyad": {"width": 120, "anchor": "w"},
            "Görev": {"width": 150, "anchor": "w"},
            "Vardiya": {"width": 100, "anchor": "center"},
            "Telefon": {"width": 120, "anchor": "center"},
            "E-posta": {"width": 200, "anchor": "w"}
        }

        for col_name, config in tree_columns.items():
            self.personnel_tree.heading(col_name, text=col_name, anchor=config.get("anchor", "center"))
            self.personnel_tree.column(col_name, width=config["width"], minwidth=config["width"], anchor=config.get("anchor", "center"))

        # Scrollbar'lar
        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.personnel_tree.yview)
        vsb.grid(row=0, column=1, sticky="ns")
        self.personnel_tree.configure(yscrollcommand=vsb.set)

        hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.personnel_tree.xview)
        hsb.grid(row=1, column=0, sticky="ew")
        self.personnel_tree.configure(xscrollcommand=hsb.set)

        # Treeview'da seçim yapıldığında olay yakalama
        self.personnel_tree.bind("<<TreeviewSelect>>", self.on_personnel_select)

    def load_personnel(self):
        """Veritabanından personel verilerini yükler ve Treeview'ı günceller."""
        for item in self.personnel_tree.get_children():
            self.personnel_tree.delete(item) # Mevcut verileri temizle
        
        personeller = self.db.fetch_all("SELECT id, name, surname, role, shift, phone, email FROM personnel ORDER BY id DESC")
        # NOT: database.py'de personel tablosuna 'surname', 'phone', 'email' sütunlarını eklediğimizden emin olun.
        # Şu anki database.py'ye baktığımda 'ad', 'soyad', 'gorev', 'vardiya', 'telefon', 'eposta' olması lazım.
        # Bu kısımda veritabanı ile uyumsuzluk olabilir, aşağıda DÜZELTME NOTU var.
        
        if personeller:
            for personel in personeller:
                self.personnel_tree.insert("", "end", values=personel)
        else:
            messagebox.showinfo("Bilgi", "Veritabanında personel bulunamadı.")


    def add_personnel(self):
        """Giriş alanlarındaki bilgileri kullanarak yeni personel ekler."""
        # Sözlükten verileri çekiyoruz
        name = self.personnel_entries["name"].get().strip()
        surname = self.personnel_entries["surname"].get().strip()
        role = self.personnel_entries["role"].get().strip()
        shift = self.personnel_entries["shift"].get().strip()
        phone = self.personnel_entries["phone"].get().strip()
        email = self.personnel_entries["email"].get().strip()

        if not name or not surname:
            messagebox.showwarning("Giriş Hatası", "Ad ve Soyad boş bırakılamaz.")
            return

        # Veritabanına ekleme sorgusu
        # Sütun isimleri sizin database.py'deki 'personnel' tablosuyla uyumlu olmalı!
        # Benim database.py önerimde ad, soyad, gorev, vardiya, telefon, eposta vardı.
        # Sizin verdiğiniz database.py'de name, role, shift vardı.
        # Şimdi bu kodda 'name', 'surname', 'role', 'shift', 'phone', 'email' kullanıyorum,
        # lütfen Database sınıfındaki 'personnel' tablosunun sütunlarını da buna göre güncelleyelim.
        
        # DÜZELTME NOTU: database.py'deki 'personnel' tablosunu şu sütunlara sahip olacak şekilde güncelleyin:
        # id, name, surname, role, shift, phone, email
        
        query = "INSERT INTO personnel (name, surname, role, shift, phone, email) VALUES (?, ?, ?, ?, ?, ?)"
        params = (name, surname, role, shift, phone, email)

        if self.db.execute_query(query, params):
            messagebox.showinfo("Başarılı", "Personel başarıyla eklendi.")
            self.clear_personnel_entries()
            self.load_personnel()
        else:
            messagebox.showerror("Hata", "Personel eklenirken bir hata oluştu.")


    def update_personnel(self):
        """Seçili personelin bilgilerini günceller."""
        selected_item = self.personnel_tree.focus()
        if not selected_item:
            messagebox.showwarning("Seçim Yok", "Lütfen güncellemek için bir personel seçin.")
            return
        
        # Seçilen personelin ID'sini al
        personnel_id = self.personnel_tree.item(selected_item, 'values')[0]
        
        name = self.personnel_entries["name"].get().strip()
        surname = self.personnel_entries["surname"].get().strip()
        role = self.personnel_entries["role"].get().strip()
        shift = self.personnel_entries["shift"].get().strip()
        phone = self.personnel_entries["phone"].get().strip()
        email = self.personnel_entries["email"].get().strip()

        if not name or not surname:
            messagebox.showwarning("Giriş Hatası", "Ad ve Soyad boş bırakılamaz.")
            return

        query = "UPDATE personnel SET name=?, surname=?, role=?, shift=?, phone=?, email=? WHERE id=?"
        params = (name, surname, role, shift, phone, email, personnel_id)

        if self.db.execute_query(query, params):
            messagebox.showinfo("Başarılı", "Personel başarıyla güncellendi.")
            self.clear_personnel_entries()
            self.load_personnel()
        else:
            messagebox.showerror("Hata", "Personel güncellenirken bir hata oluştu.")

    def delete_personnel(self):
        """Seçili personeli veritabanından siler."""
        selected_item = self.personnel_tree.focus()
        if not selected_item:
            messagebox.showwarning("Seçim Yok", "Lütfen silmek için bir personel seçin.")
            return

        personnel_id = self.personnel_tree.item(selected_item, 'values')[0]
        personnel_name = self.personnel_entries["name"].get() + " " + self.personnel_entries["surname"].get()

        if messagebox.askyesno("Onay", f"'{personnel_name}' adlı personeli silmek istediğinizden emin misiniz?"):
            if self.db.execute_query("DELETE FROM personnel WHERE id=?", (personnel_id,)):
                messagebox.showinfo("Başarılı", "Personel başarıyla silindi.")
                self.load_personnel()
                self.clear_personnel_entries()
            else:
                messagebox.showerror("Hata", "Personel silinirken bir hata oluştu.")

    def on_personnel_select(self, event):
        """Treeview'da bir personel seçildiğinde giriş alanlarını doldurur."""
        selected_item = self.personnel_tree.focus()
        if selected_item:
            values = self.personnel_tree.item(selected_item, 'values')
            self.current_personnel_id = values[0] # Seçilen personelin ID'sini sakla

            # Giriş alanlarını doldur
            self.personnel_entries["name"].delete(0, tk.END)
            self.personnel_entries["name"].insert(0, values[1]) # Ad
            self.personnel_entries["surname"].delete(0, tk.END)
            self.personnel_entries["surname"].insert(0, values[2]) # Soyad
            self.personnel_entries["role"].delete(0, tk.END)
            self.personnel_entries["role"].insert(0, values[3]) # Görev
            self.personnel_entries["shift"].delete(0, tk.END)
            self.personnel_entries["shift"].insert(0, values[4]) # Vardiya
            self.personnel_entries["phone"].delete(0, tk.END)
            self.personnel_entries["phone"].insert(0, values[5]) # Telefon
            self.personnel_entries["email"].delete(0, tk.END)
            self.personnel_entries["email"].insert(0, values[6]) # E-posta
        else:
            self.clear_personnel_entries() # Seçim kaldırıldıysa alanları temizle

    def clear_personnel_entries(self):
        """Personel bilgi giriş alanlarını temizler ve current_personnel_id'yi sıfırlar."""
        self.current_personnel_id = None
        for entry in self.personnel_entries.values():
            entry.delete(0, tk.END)