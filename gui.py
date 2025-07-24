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
        add_window.geometry("300x250") # Pencere boyutunu biraz büyüttüm

        # Etiketler ve Giriş Alanları
        tk.Label(add_window, text="Ad:").pack(pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.pack(pady=5, padx=10, fill="x")

        tk.Label(add_window, text="Görev:").pack(pady=5)
        role_entry = tk.Entry(add_window)
        role_entry.pack(pady=5, padx=10, fill="x")

        tk.Label(add_window, text="Vardiya:").pack(pady=5)
        shift_entry = tk.Entry(add_window)
        shift_entry.pack(pady=5, padx=10, fill="x")

        # Kaydet butonu
        def save():
            name = name_entry.get().strip() # Boşlukları temizle
            role = role_entry.get().strip()
            shift = shift_entry.get().strip()

            if name and role: # Ad ve Görev alanlarının boş olup olmadığını kontrol et
                self.db.execute_query("INSERT INTO personnel (name, role, shift) VALUES (?, ?, ?)", (name, role, shift))
                messagebox.showinfo("Başarılı", "Personel başarıyla eklendi.")
                self.load_personnel_data() # Personel listesini yenile
                add_window.destroy() # Pencereyi kapat
            else:
                messagebox.showerror("Hata", "Ad ve Görev alanları boş bırakılamaz.")

        tk.Button(add_window, text="Kaydet", command=save, bg="#28a745", fg="white", font=("Arial", 10, "bold")).pack(pady=10)
        tk.Button(add_window, text="İptal", command=add_window.destroy, bg="#dc3545", fg="white", font=("Arial", 10)).pack(pady=5)
    def edit_personnel(self):
        selected_item = self.personnel_tree.focus() # Seçili öğeyi al
        if not selected_item: # Hiçbir öğe seçili değilse uyar
            messagebox.showwarning("Seçim Yok", "Lütfen düzenlemek istediğiniz bir personel seçin.")
            return

        values = self.personnel_tree.item(selected_item, 'values') # Seçili öğenin değerlerini al
        person_id = values[0] # ID ilk değer

        # Düzenleme penceresi oluştur
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Personel Düzenle")
        edit_window.geometry("300x250") # Pencere boyutunu ayarla

        # Etiketler ve Giriş Alanları, mevcut değerlerle doldur
        tk.Label(edit_window, text="Ad:").pack(pady=5)
        name_entry = tk.Entry(edit_window)
        name_entry.insert(0, values[1]) # Mevcut adı önceden doldur
        name_entry.pack(pady=5, padx=10, fill="x")

        tk.Label(edit_window, text="Görev:").pack(pady=5)
        role_entry = tk.Entry(edit_window)
        role_entry.insert(0, values[2]) # Mevcut görevi önceden doldur
        role_entry.pack(pady=5, padx=10, fill="x")

        tk.Label(edit_window, text="Vardiya:").pack(pady=5)
        shift_entry = tk.Entry(edit_window)
        shift_entry.insert(0, values[3]) # Mevcut vardiyayı önceden doldur
        shift_entry.pack(pady=5, padx=10, fill="x")

        # Kaydet butonu
        def save():
            name = name_entry.get().strip()
            role = role_entry.get().strip()
            shift = shift_entry.get().strip()

            if name and role: # Ad ve Görev alanlarının boş olup olmadığını kontrol et
                self.db.execute_query("UPDATE personnel SET name=?, role=?, shift=? WHERE id=?", (name, role, shift, person_id))
                messagebox.showinfo("Başarılı", "Personel başarıyla güncellendi.")
                self.load_personnel_data() # Personel listesini yenile
                edit_window.destroy() # Pencereyi kapat
            else:
                messagebox.showerror("Hata", "Ad ve Görev alanları boş bırakılamaz.")

        tk.Button(edit_window, text="Kaydet", command=save, bg="#28a745", fg="white", font=("Arial", 10, "bold")).pack(pady=10)
        tk.Button(edit_window, text="İptal", command=edit_window.destroy, bg="#dc3545", fg="white", font=("Arial", 10)).pack(pady=5)

    def delete_personnel(self):
        selected_item = self.personnel_tree.focus() # Seçili öğeyi al
        if not selected_item: # Hiçbir öğe seçili değilse uyar
            messagebox.showwarning("Seçim Yok", "Lütfen silmek istediğiniz bir personel seçin.")
            return

        values = self.personnel_tree.item(selected_item, 'values') # Seçili öğenin değerlerini al
        person_id = values[0]
        person_name = values[1]

        # Kullanıcıya onay sor
        if messagebox.askyesno("Onay", f"'{person_name}' ({person_id} ID'li) personeli silmek istediğinizden emin misiniz? Bu işlem geri alınamaz."):
            # Önce bu personele atanmış ekipmanları veya görevleri güncelle
            # FOREIGN KEY ON DELETE SET NULL yaptığımız için bu satırlar aslında çok gerekli değil
            # ancak ek bir güvenlik katmanı olarak düşünülebilir veya başka durumlar için faydalı olabilir.
            # Örneğin, sildikten sonra ne olduğunu kullanıcıya bildirmek için.
            self.db.execute_query("UPDATE equipment SET assigned_to = NULL WHERE assigned_to = ?", (person_id,))
            self.db.execute_query("UPDATE tasks SET assigned_person = NULL WHERE assigned_person = ?", (person_id,))

            # Personeli sil
            self.db.execute_query("DELETE FROM personnel WHERE id=?", (person_id,))
            messagebox.showinfo("Başarılı", "Personel başarıyla silindi.")
            self.load_personnel_data() # Personel listesini yenile
        else:
            messagebox.showinfo("İptal Edildi", "Personel silme işlemi iptal edildi.")
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