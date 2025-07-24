import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime # Bu satırı eklediğimizden emin olalım!

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
            # Personeli sil
            # FOREIGN KEY ON DELETE SET NULL yaptığımız için ekipman/görev güncellemeleri otomatik olacak.
            self.db.execute_query("DELETE FROM personnel WHERE id=?", (person_id,))
            messagebox.showinfo("Başarılı", "Personel başarıyla silindi.")
            self.load_personnel_data() # Personel listesini yenile
        else:
            messagebox.showinfo("İptal Edildi", "Personel silme işlemi iptal edildi.")

    # --- Ekipman Modülü ---
    def show_equipment_module(self):
        self.clear_content_frame()
        tk.Label(self.content_frame, text="Ekipman Zimmet Modülü", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=20)

        # Ekipman listesi için Treeview
        columns = ("ID", "Ad/Tür", "Zimmetli Kişi (ID)", "Durum")
        self.equipment_tree = ttk.Treeview(self.content_frame, columns=columns, show="headings")
        for col in columns:
            self.equipment_tree.heading(col, text=col)
            self.equipment_tree.column(col, width=120)
        self.equipment_tree.pack(pady=10, padx=10, fill="both", expand=True)

        self.load_equipment_data() # Verileri yükle

        # Düğmeler
        button_frame = tk.Frame(self.content_frame, bg="#ecf0f1")
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Yeni Ekipman Ekle", command=self.add_equipment).pack(side="left", padx=5)
        tk.Button(button_frame, text="Ekipman Düzenle", command=self.edit_equipment).pack(side="left", padx=5)
        tk.Button(button_frame, text="Ekipman Sil", command=self.delete_equipment).pack(side="left", padx=5)
        tk.Button(button_frame, text="Ekipman Zimmetle", command=self.assign_equipment).pack(side="left", padx=10) # Daha geniş ayrım
        tk.Button(button_frame, text="Zimmeti Kaldır", command=self.unassign_equipment).pack(side="left", padx=5)

    def load_equipment_data(self):
        for row in self.equipment_tree.get_children():
            self.equipment_tree.delete(row)
        
        # Ekipman ve zimmetli olduğu personelin adı (JOIN ile)
        equipment = self.db.fetch_all("""
            SELECT 
                e.id, 
                e.name, 
                COALESCE(p.name || ' (ID: ' || p.id || ')', 'Yok') AS assigned_person_info, -- Eğer assigned_to NULL ise 'Yok' göster
                e.status 
            FROM equipment e
            LEFT JOIN personnel p ON e.assigned_to = p.id
        """)
        for eq in equipment:
            self.equipment_tree.insert("", "end", values=eq)

    # --- Ekipman Ekleme ---
    def add_equipment(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Yeni Ekipman Ekle")
        add_window.geometry("300x200")

        tk.Label(add_window, text="Ekipman Adı/Türü:").pack(pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.pack(pady=5, padx=10, fill="x")

        tk.Label(add_window, text="Durum:").pack(pady=5)
        # Durum için seçenekli bir Combobox kullanabiliriz
        status_options = ["Mevcut", "Zimmetli", "Arızalı", "Bakımda"]
        status_combobox = ttk.Combobox(add_window, values=status_options)
        status_combobox.set("Mevcut") # Varsayılan değer
        status_combobox.pack(pady=5, padx=10, fill="x")

        def save():
            name = name_entry.get().strip()
            status = status_combobox.get().strip()
            if name and status:
                self.db.execute_query("INSERT INTO equipment (name, status) VALUES (?, ?)", (name, status))
                messagebox.showinfo("Başarılı", "Ekipman başarıyla eklendi.")
                self.load_equipment_data()
                add_window.destroy()
            else:
                messagebox.showerror("Hata", "Ekipman Adı/Türü ve Durum alanları boş bırakılamaz.")

        tk.Button(add_window, text="Kaydet", command=save, bg="#28a745", fg="white", font=("Arial", 10, "bold")).pack(pady=10)
        tk.Button(add_window, text="İptal", command=add_window.destroy, bg="#dc3545", fg="white", font=("Arial", 10)).pack(pady=5)

    # --- Ekipman Düzenleme ---
    def edit_equipment(self):
        selected_item = self.equipment_tree.focus()
        if not selected_item:
            messagebox.showwarning("Seçim Yok", "Lütfen düzenlemek istediğiniz bir ekipman seçin.")
            return

        values = self.equipment_tree.item(selected_item, 'values')
        equipment_id = values[0]
        
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Ekipman Düzenle")
        edit_window.geometry("300x200")

        tk.Label(edit_window, text="Ekipman Adı/Türü:").pack(pady=5)
        name_entry = tk.Entry(edit_window)
        name_entry.insert(0, values[1])
        name_entry.pack(pady=5, padx=10, fill="x")

        tk.Label(edit_window, text="Durum:").pack(pady=5)
        status_options = ["Mevcut", "Zimmetli", "Arızalı", "Bakımda"]
        status_combobox = ttk.Combobox(edit_window, values=status_options)
        status_combobox.set(values[3]) # Mevcut durumu seç
        status_combobox.pack(pady=5, padx=10, fill="x")

        def save():
            name = name_entry.get().strip()
            status = status_combobox.get().strip()
            if name and status:
                self.db.execute_query("UPDATE equipment SET name=?, status=? WHERE id=?", (name, status, equipment_id))
                messagebox.showinfo("Başarılı", "Ekipman başarıyla güncellendi.")
                self.load_equipment_data()
                edit_window.destroy()
            else:
                messagebox.showerror("Hata", "Ekipman Adı/Türü ve Durum alanları boş bırakılamaz.")

        tk.Button(edit_window, text="Kaydet", command=save, bg="#28a745", fg="white", font=("Arial", 10, "bold")).pack(pady=10)
        tk.Button(edit_window, text="İptal", command=edit_window.destroy, bg="#dc3545", fg="white", font=("Arial", 10)).pack(pady=5)

    # --- Ekipman Silme ---
    def delete_equipment(self):
        selected_item = self.equipment_tree.focus()
        if not selected_item:
            messagebox.showwarning("Seçim Yok", "Lütfen silmek istediğiniz bir ekipman seçin.")
            return

        values = self.equipment_tree.item(selected_item, 'values')
        equipment_id = values[0]
        equipment_name = values[1]

        if messagebox.askyesno("Onay", f"'{equipment_name}' ({equipment_id} ID'li) ekipmanı silmek istediğinizden emin misiniz? Bu işlem geri alınamaz."):
            self.db.execute_query("DELETE FROM equipment WHERE id=?", (equipment_id,))
            messagebox.showinfo("Başarılı", "Ekipman başarıyla silindi.")
            self.load_equipment_data()
        else:
            messagebox.showinfo("İptal Edildi", "Ekipman silme işlemi iptal edildi.")

    # --- Ekipman Zimmetleme ---
    def assign_equipment(self):
        selected_item = self.equipment_tree.focus()
        if not selected_item:
            messagebox.showwarning("Seçim Yok", "Lütfen zimmetlemek istediğiniz bir ekipman seçin.")
            return

        values = self.equipment_tree.item(selected_item, 'values')
        equipment_id = values[0]
        current_status = values[3]

        if current_status == "Zimmetli":
            messagebox.showwarning("Uyarı", "Bu ekipman zaten zimmetli.")
            return

        # Personel seçme penceresi
        assign_window = tk.Toplevel(self.root)
        assign_window.title("Ekipmanı Zimmetle")
        assign_window.geometry("400x300")

        tk.Label(assign_window, text=f"'{values[1]}' adlı ekipmanı kime zimmetleyeceksiniz?", font=("Arial", 10, "bold")).pack(pady=10)

        # Personel listesi için Treeview
        columns = ("ID", "Ad", "Görev")
        personnel_select_tree = ttk.Treeview(assign_window, columns=columns, show="headings")
        for col in columns:
            personnel_select_tree.heading(col, text=col)
            personnel_select_tree.column(col, width=100)
        
        # Sadece tekli seçim yapılmasını sağla (varsayılan genelde "browse" modudur)
        personnel_select_tree.config(selectmode="browse") 

        personnel_select_tree.pack(pady=10, padx=10, fill="both", expand=True)

        # Personel verilerini yükle
        personnel_data = self.db.fetch_all("SELECT id, name, role FROM personnel")
        for p in personnel_data:
            personnel_select_tree.insert("", "end", values=p)

        def save_assignment():
            # Burası önemli: get_selection() veya focus() kullanabiliriz
            # focus() tekli seçimde seçili öğeyi döndürür.
            selected_person_item = personnel_select_tree.focus() 
            
            if not selected_person_item:
                messagebox.showerror("Hata", "Lütfen ekipmanı zimmetleyeceğiniz bir personel seçin.")
                return
            
            # Seçili öğenin verilerini al
            person_values = personnel_select_tree.item(selected_person_item, 'values')
            
            # person_values'ın boş veya eksik olup olmadığını kontrol edelim
            if not person_values or len(person_values) < 2: # En az ID ve Ad olmalı
                messagebox.showerror("Hata", "Seçilen personel verileri alınamadı. Lütfen tekrar deneyin.")
                return

            try:
                person_id = int(person_values[0]) # ID'nin int olduğundan emin olalım
                person_name = person_values[1]

                if messagebox.askyesno("Onay", f"'{values[1]}' ekipmanını '{person_name}' ({person_id} ID'li) kişiye zimmetlemek istediğinizden emin misiniz?"):
                    self.db.execute_query("UPDATE equipment SET assigned_to=?, status='Zimmetli' WHERE id=?", (person_id, equipment_id))
                    messagebox.showinfo("Başarılı", f"Ekipman '{person_name}' kişiye başarıyla zimmetlendi.")
                    self.load_equipment_data()
                    assign_window.destroy()
                else:
                    messagebox.showinfo("İptal Edildi", "Zimmetleme işlemi iptal edildi.")
            except ValueError:
                messagebox.showerror("Hata", "Personel ID'si geçerli değil.")
            except Exception as e:
                messagebox.showerror("Hata", f"Zimmetleme sırasında bir hata oluştu: {e}")


        tk.Button(assign_window, text="Zimmetle", command=save_assignment, bg="#28a745", fg="white", font=("Arial", 10, "bold")).pack(pady=10)
        tk.Button(assign_window, text="İptal", command=assign_window.destroy, bg="#dc3545", fg="white", font=("Arial", 10)).pack(pady=5)

    # --- Zimmeti Kaldırma ---
    def unassign_equipment(self):
        selected_item = self.equipment_tree.focus()
        if not selected_item:
            messagebox.showwarning("Seçim Yok", "Lütfen zimmeti kaldırılacak bir ekipman seçin.")
            return

        values = self.equipment_tree.item(selected_item, 'values')
        equipment_id = values[0]
        assigned_person_info = values[2] # "Ad (ID: X)" veya "Yok"

        if assigned_person_info == "Yok":
            messagebox.showwarning("Uyarı", "Bu ekipman zaten zimmetli değil.")
            return

        if messagebox.askyesno("Onay", f"'{values[1]}' ekipmanının zimmetini kaldırmak istediğinizden emin misiniz?"):
            self.db.execute_query("UPDATE equipment SET assigned_to=NULL, status='Mevcut' WHERE id=?", (equipment_id,))
            messagebox.showinfo("Başarılı", "Ekipman zimmeti başarıyla kaldırıldı.")
            self.load_equipment_data()
        else:
            messagebox.showinfo("İptal Edildi", "Zimmeti kaldırma işlemi iptal edildi.")

    # --- Görevler Modülü ---
    def show_tasks_module(self):
        self.clear_content_frame()
        tk.Label(self.content_frame, text="Görev Yönetim Modülü", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=20)

        # Görev listesi için Treeview
        columns = ("ID", "Görev Adı", "Atanan Kişi (ID)", "Bitiş Tarihi", "Durum")
        self.tasks_tree = ttk.Treeview(self.content_frame, columns=columns, show="headings")
        for col in columns:
            self.tasks_tree.heading(col, text=col)
            self.tasks_tree.column(col, width=120)
        self.tasks_tree.pack(pady=10, padx=10, fill="both", expand=True)

        self.load_tasks_data() # Verileri yükle

        # Düğmeler
        button_frame = tk.Frame(self.content_frame, bg="#ecf0f1")
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Yeni Görev Ekle", command=self.add_task).pack(side="left", padx=5)
        tk.Button(button_frame, text="Görevi Düzenle", command=self.edit_task).pack(side="left", padx=5)
        tk.Button(button_frame, text="Görevi Sil", command=self.delete_task).pack(side="left", padx=5)
        tk.Button(button_frame, text="Tamamlandı Olarak İşaretle", command=self.mark_task_completed).pack(side="left", padx=10)
        
    def load_tasks_data(self):
        for row in self.tasks_tree.get_children():
            self.tasks_tree.delete(row)
        
        # Görev ve atandığı personelin adı (JOIN ile)
        tasks = self.db.fetch_all("""
            SELECT 
                t.id, 
                t.task_name, 
                COALESCE(p.name || ' (ID: ' || p.id || ')', 'Atanmadı') AS assigned_person_info, -- Eğer assigned_person NULL ise 'Atanmadı' göster
                t.deadline,
                t.status
            FROM tasks t
            LEFT JOIN personnel p ON t.assigned_person = p.id
        """)
        for task in tasks:
            # Duruma göre renkler atayabiliriz (isteğe bağlı, sonra da yapılabilir)
            # Örneğin, 'Tamamlandı' için yeşil, 'Beklemede' için turuncu vb.
            # Şu an için sadece ekleyelim:
            self.tasks_tree.insert("", "end", values=task)

    # --- Görev Ekleme ---
    def add_task(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Yeni Görev Ekle")
        add_window.geometry("400x350")

        tk.Label(add_window, text="Görev Adı:").pack(pady=5)
        task_name_entry = tk.Entry(add_window)
        task_name_entry.pack(pady=5, padx=10, fill="x")

        tk.Label(add_window, text="Bitiş Tarihi (YYYY-MM-DD):").pack(pady=5)
        deadline_entry = tk.Entry(add_window)
        deadline_entry.pack(pady=5, padx=10, fill="x")
        # Örnek tarih formatı için placeholder
        deadline_entry.insert(0, "YYYY-MM-DD")
        deadline_entry.bind("<FocusIn>", lambda event: deadline_entry.delete(0, "end") if deadline_entry.get() == "YYYY-MM-DD" else None)

        tk.Label(add_window, text="Durum:").pack(pady=5)
        status_options = ["Beklemede", "Devam Ediyor", "Tamamlandı", "İptal Edildi"]
        status_combobox = ttk.Combobox(add_window, values=status_options)
        status_combobox.set("Beklemede") # Varsayılan değer
        status_combobox.pack(pady=5, padx=10, fill="x")

        tk.Label(add_window, text="Atanacak Personel:").pack(pady=5)
        
        # Personel seçimi için Combobox
        # Önce tüm personeli çekelim
        personnel_data = self.db.fetch_all("SELECT id, name FROM personnel")
        personnel_dict = {f"{p[1]} (ID: {p[0]})": p[0] for p in personnel_data} # "Ad (ID: X)": ID
        personnel_names = list(personnel_dict.keys())
        personnel_names.insert(0, "Atama Yok") # İlk seçenek olarak atanmamış olsun

        assigned_person_combobox = ttk.Combobox(add_window, values=personnel_names)
        assigned_person_combobox.set("Atama Yok")
        assigned_person_combobox.pack(pady=5, padx=10, fill="x")

        def save():
            task_name = task_name_entry.get().strip()
            deadline = deadline_entry.get().strip()
            status = status_combobox.get().strip()
            selected_person_text = assigned_person_combobox.get()
            
            assigned_person_id = None
            if selected_person_text != "Atama Yok":
                try:
                    # 'Ad (ID: X)' formatından ID'yi çek
                    person_id_str = selected_person_text.split('(ID: ')[1].rstrip(')')
                    assigned_person_id = int(person_id_str)
                except (IndexError, ValueError):
                    messagebox.showerror("Hata", "Geçersiz personel seçimi formatı.")
                    return

            if task_name and deadline and status:
                self.db.execute_query(
                    "INSERT INTO tasks (task_name, assigned_person, deadline, status) VALUES (?, ?, ?, ?)", 
                    (task_name, assigned_person_id, deadline, status)
                )
                messagebox.showinfo("Başarılı", "Görev başarıyla eklendi.")
                self.load_tasks_data()
                add_window.destroy()
            else:
                messagebox.showerror("Hata", "Görev Adı, Bitiş Tarihi ve Durum alanları boş bırakılamaz.")

        tk.Button(add_window, text="Kaydet", command=save, bg="#28a745", fg="white", font=("Arial", 10, "bold")).pack(pady=10)
        tk.Button(add_window, text="İptal", command=add_window.destroy, bg="#dc3545", fg="white", font=("Arial", 10)).pack(pady=5)

    # --- Görev Düzenleme ---
    def edit_task(self):
        selected_item = self.tasks_tree.focus()
        if not selected_item:
            messagebox.showwarning("Seçim Yok", "Lütfen düzenlemek istediğiniz bir görev seçin.")
            return

        values = self.tasks_tree.item(selected_item, 'values')
        task_id = values[0]
        
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Görevi Düzenle")
        edit_window.geometry("400x350")

        tk.Label(edit_window, text="Görev Adı:").pack(pady=5)
        task_name_entry = tk.Entry(edit_window)
        task_name_entry.insert(0, values[1])
        task_name_entry.pack(pady=5, padx=10, fill="x")

        tk.Label(edit_window, text="Bitiş Tarihi (YYYY-MM-DD):").pack(pady=5)
        deadline_entry = tk.Entry(edit_window)
        deadline_entry.insert(0, values[3])
        deadline_entry.pack(pady=5, padx=10, fill="x")

        tk.Label(edit_window, text="Durum:").pack(pady=5)
        status_options = ["Beklemede", "Devam Ediyor", "Tamamlandı", "İptal Edildi"]
        status_combobox = ttk.Combobox(edit_window, values=status_options)
        status_combobox.set(values[4]) # Mevcut durumu seç
        status_combobox.pack(pady=5, padx=10, fill="x")

        tk.Label(edit_window, text="Atanacak Personel:").pack(pady=5)
        personnel_data = self.db.fetch_all("SELECT id, name FROM personnel")
        personnel_dict = {f"{p[1]} (ID: {p[0]})": p[0] for p in personnel_data}
        personnel_names = list(personnel_dict.keys())
        personnel_names.insert(0, "Atama Yok")

        assigned_person_combobox = ttk.Combobox(edit_window, values=personnel_names)
        # Mevcut atanan kişiyi combobox'ta seçili hale getir
        current_assigned = values[2] # 'Ad (ID: X)' veya 'Atanmadı'
        if current_assigned == "Atanmadı":
            assigned_person_combobox.set("Atama Yok")
        else:
            # Sadece 'Ad (ID: X)' kısmını al ve combobox'ta ara
            # Eğer tam eşleşme yoksa varsayılana düşsün
            if current_assigned in personnel_names:
                assigned_person_combobox.set(current_assigned)
            else:
                assigned_person_combobox.set("Atama Yok") # Bulunamazsa varsayılan

        assigned_person_combobox.pack(pady=5, padx=10, fill="x")

        def save():
            task_name = task_name_entry.get().strip()
            deadline = deadline_entry.get().strip()
            status = status_combobox.get().strip()
            selected_person_text = assigned_person_combobox.get()
            
            assigned_person_id = None
            if selected_person_text != "Atama Yok":
                try:
                    person_id_str = selected_person_text.split('(ID: ')[1].rstrip(')')
                    assigned_person_id = int(person_id_str)
                except (IndexError, ValueError):
                    messagebox.showerror("Hata", "Geçersiz personel seçimi formatı.")
                    return

            if task_name and deadline and status:
                self.db.execute_query(
                    "UPDATE tasks SET task_name=?, assigned_person=?, deadline=?, status=? WHERE id=?", 
                    (task_name, assigned_person_id, deadline, status, task_id)
                )
                messagebox.showinfo("Başarılı", "Görev başarıyla güncellendi.")
                self.load_tasks_data()
                edit_window.destroy()
            else:
                messagebox.showerror("Hata", "Görev Adı, Bitiş Tarihi ve Durum alanları boş bırakılamaz.")

        tk.Button(edit_window, text="Kaydet", command=save, bg="#28a745", fg="white", font=("Arial", 10, "bold")).pack(pady=10)
        tk.Button(edit_window, text="İptal", command=edit_window.destroy, bg="#dc3545", fg="white", font=("Arial", 10)).pack(pady=5)

    # --- Görev Silme ---
    def delete_task(self):
        selected_item = self.tasks_tree.focus()
        if not selected_item:
            messagebox.showwarning("Seçim Yok", "Lütfen silmek istediğiniz bir görev seçin.")
            return

        values = self.tasks_tree.item(selected_item, 'values')
        task_id = values[0]
        task_name = values[1]

        if messagebox.askyesno("Onay", f"'{task_name}' ({task_id} ID'li) görevi silmek istediğinizden emin misiniz? Bu işlem geri alınamaz."):
            self.db.execute_query("DELETE FROM tasks WHERE id=?", (task_id,))
            messagebox.showinfo("Başarılı", "Görev başarıyla silindi.")
            self.load_tasks_data()
        else:
            messagebox.showinfo("İptal Edildi", "Görev silme işlemi iptal edildi.")

    # --- Görevi Tamamlandı Olarak İşaretle ---
    def mark_task_completed(self):
        selected_item = self.tasks_tree.focus()
        if not selected_item:
            messagebox.showwarning("Seçim Yok", "Lütfen tamamlandı olarak işaretlemek istediğiniz bir görev seçin.")
            return

        values = self.tasks_tree.item(selected_item, 'values')
        task_id = values[0]
        current_status = values[4]

        if current_status == "Tamamlandı":
            messagebox.showwarning("Uyarı", "Bu görev zaten tamamlandı olarak işaretlenmiş.")
            return

        if messagebox.askyesno("Onay", f"'{values[1]}' görevini tamamlandı olarak işaretlemek istediğinizden emin misiniz?"):
            self.db.execute_query("UPDATE tasks SET status='Tamamlandı' WHERE id=?", (task_id,))
            messagebox.showinfo("Başarılı", "Görev başarıyla tamamlandı olarak işaretlendi.")
            self.load_tasks_data()
        else:
            messagebox.showinfo("İptal Edildi", "Görev durumu güncelleme işlemi iptal edildi.")

    # --- Acil Durum Bildirim Modülü ---
    # --- Acil Durum Bildirim Modülü ---
    def show_emergency_module(self):
        self.clear_content_frame()
        tk.Label(self.content_frame, text="Acil Durum Bildirim Modülü", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=20)

        # Acil durum listesi için Treeview
        columns = ("ID", "Tarih", "Saat", "Tür", "Açıklama", "Etkilenen Personel (ID)", "Etkilenen Ekipman (ID)", "Alınan Aksiyon")
        self.emergency_tree = ttk.Treeview(self.content_frame, columns=columns, show="headings")
        for col in columns:
            self.emergency_tree.heading(col, text=col)
            self.emergency_tree.column(col, width=120)
        self.emergency_tree.pack(pady=10, padx=10, fill="both", expand=True)

        self.load_emergency_data() # Verileri yükle

        # Düğmeler
        button_frame = tk.Frame(self.content_frame, bg="#ecf0f1")
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Yeni Acil Durum Kaydı", command=self.add_emergency).pack(side="left", padx=5)
        tk.Button(button_frame, text="Acil Durum Düzenle", command=self.edit_emergency).pack(side="left", padx=5)
        tk.Button(button_frame, text="Acil Durum Sil", command=self.delete_emergency).pack(side="left", padx=5)
    # gui.py dosyası

    # ... (diğer kodlar) ...

    def load_emergency_data(self):
        # Treeview'i temizle
        for i in self.emergency_tree.get_children():
            self.emergency_tree.delete(i)

        # Veritabanından acil durum verilerini çek
        emergency_data = self.db.fetch_all("""
            SELECT
                e.id,
                e.date,
                e.time,
                e.event_type, -- Burası 'event_type' olarak düzeltildi
                e.description,
                e.affected_personnel_ids,
                e.affected_equipment_ids,
                e.action_taken
            FROM
                emergency_events e
            ORDER BY
                e.date DESC, e.time DESC
        """)

        # Verileri Treeview'e ekle
        for row in emergency_data:
            self.emergency_tree.insert("", "end", values=row)


    def add_emergency(self):
        # Yeni Acil Durum Kaydı için pencere oluştur
        add_window = tk.Toplevel(self.root)
        add_window.title("Yeni Acil Durum Kaydı Ekle")
        add_window.geometry("400x450")
        add_window.transient(self.root) # Ana pencerenin üzerinde kalmasını sağlar
        add_window.grab_set() # Ana pencereyle etkileşimi engeller

        tk.Label(add_window, text="Tarih (YYYY-MM-DD):").pack(pady=5)
        date_entry = tk.Entry(add_window)
        date_entry.insert(0, datetime.now().strftime("%Y-%m-%d")) # Otomatik bugünün tarihini ekle
        date_entry.pack(pady=5)

        tk.Label(add_window, text="Saat (HH:MM):").pack(pady=5)
        time_entry = tk.Entry(add_window)
        time_entry.insert(0, datetime.now().strftime("%H:%M")) # Otomatik şu anki saati ekle
        time_entry.pack(pady=5)

        tk.Label(add_window, text="Acil Durum Türü:").pack(pady=5)
        event_type_entry = tk.Entry(add_window)
        event_type_entry.pack(pady=5)

        tk.Label(add_window, text="Açıklama:").pack(pady=5)
        description_entry = tk.Entry(add_window)
        description_entry.pack(pady=5)

        tk.Label(add_window, text="Etkilenen Personel ID'leri (virgülle ayır):").pack(pady=5)
        personnel_ids_entry = tk.Entry(add_window)
        personnel_ids_entry.pack(pady=5)

        tk.Label(add_window, text="Etkilenen Ekipman ID'leri (virgülle ayır):").pack(pady=5)
        equipment_ids_entry = tk.Entry(add_window)
        equipment_ids_entry.pack(pady=5)

        tk.Label(add_window, text="Alınan Aksiyon:").pack(pady=5)
        action_taken_entry = tk.Entry(add_window)
        action_taken_entry.pack(pady=5)

        def save_emergency():
            date = date_entry.get()
            time = time_entry.get()
            event_type = event_type_entry.get()
            description = description_entry.get()
            personnel_ids = personnel_ids_entry.get()
            equipment_ids = equipment_ids_entry.get()
            action_taken = action_taken_entry.get()

            if not all([date, time, event_type, description, action_taken]):
                messagebox.showwarning("Eksik Bilgi", "Lütfen tüm zorunlu alanları doldurun.")
                return

            try:
                self.db.execute_query("""
                    INSERT INTO emergency_events (date, time, event_type, description, affected_personnel_ids, affected_equipment_ids, action_taken)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (date, time, event_type, description, personnel_ids, equipment_ids, action_taken))
                messagebox.showinfo("Başarılı", "Acil durum kaydı başarıyla eklendi.")
                self.load_emergency_data() # Listeyi güncelle
                add_window.destroy() # Pencereyi kapat
            except Exception as e:
                messagebox.showerror("Hata", f"Acil durum kaydı eklenirken bir hata oluştu: {e}")

       # Kaydet butonu
        save_button = tk.Button(add_window, text="Kaydet", command=save_emergency,
                                bg="#28a745", fg="white", font=("Arial", 10, "bold"),
                                padx=15, pady=8, bd=0, relief="flat") # image_652ae5.png'deki butona daha çok benzemesi için stil eklendi
        save_button.pack(pady=20) # Butonun altına biraz daha boşluk bırakmak için
    def edit_emergency(self):
        selected_item = self.emergency_tree.focus()
        if not selected_item:
            messagebox.showwarning("Seçim Yok", "Lütfen düzenlemek için bir acil durum kaydı seçin.")
            return

        values = self.emergency_tree.item(selected_item, 'values')
        emergency_id = values[0] # ID her zaman ilk sütunda

        # Düzenleme penceresi oluştur
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Acil Durum Kaydını Düzenle")
        edit_window.geometry("400x450")
        edit_window.transient(self.root)
        edit_window.grab_set()

        tk.Label(edit_window, text="Tarih (YYYY-MM-DD):").pack(pady=5)
        date_entry = tk.Entry(edit_window)
        date_entry.insert(0, values[1])
        date_entry.pack(pady=5)

        tk.Label(edit_window, text="Saat (HH:MM):").pack(pady=5)
        time_entry = tk.Entry(edit_window)
        time_entry.insert(0, values[2])
        time_entry.pack(pady=5)

        tk.Label(edit_window, text="Acil Durum Türü:").pack(pady=5)
        event_type_entry = tk.Entry(edit_window)
        event_type_entry.insert(0, values[3])
        event_type_entry.pack(pady=5)

        tk.Label(edit_window, text="Açıklama:").pack(pady=5)
        description_entry = tk.Entry(edit_window)
        description_entry.insert(0, values[4])
        description_entry.pack(pady=5)

        tk.Label(edit_window, text="Etkilenen Personel ID'leri (virgülle ayır):").pack(pady=5)
        personnel_ids_entry = tk.Entry(edit_window)
        personnel_ids_entry.insert(0, values[5])
        personnel_ids_entry.pack(pady=5)

        tk.Label(edit_window, text="Etkilenen Ekipman ID'leri (virgülle ayır):").pack(pady=5)
        equipment_ids_entry = tk.Entry(edit_window)
        equipment_ids_entry.insert(0, values[6])
        equipment_ids_entry.pack(pady=5)

        tk.Label(edit_window, text="Alınan Aksiyon:").pack(pady=5)
        action_taken_entry = tk.Entry(edit_window)
        action_taken_entry.insert(0, values[7])
        action_taken_entry.pack(pady=5)

        def save_edited_emergency():
            date = date_entry.get()
            time = time_entry.get()
            event_type = event_type_entry.get()
            description = description_entry.get()
            personnel_ids = personnel_ids_entry.get()
            equipment_ids = equipment_ids_entry.get()
            action_taken = action_taken_entry.get()

            if not all([date, time, event_type, description, action_taken]):
                messagebox.showwarning("Eksik Bilgi", "Lütfen tüm zorunlu alanları doldurun.")
                return

            try:
                self.db.execute_query("""
                    UPDATE emergency_events
                    SET date=?, time=?, event_type=?, description=?, affected_personnel_ids=?, affected_equipment_ids=?, action_taken=?
                    WHERE id=?
                """, (date, time, event_type, description, personnel_ids, equipment_ids, action_taken, emergency_id))
                messagebox.showinfo("Başarılı", "Acil durum kaydı başarıyla güncellendi.")
                self.load_emergency_data() # Listeyi güncelle
                edit_window.destroy()
            except Exception as e:
                messagebox.showerror("Hata", f"Acil durum kaydı güncellenirken bir hata oluştu: {e}")

        save_button = tk.Button(edit_window, text="Kaydet", command=save_edited_emergency,
                                bg="#28a745", fg="white", font=("Arial", 10, "bold"),
                                padx=15, pady=8, bd=0, relief="flat") # Daha estetik görünmesi için padx, pady, bd ve relief eklendi
        save_button.pack(pady=20) # Daha fazla boşluk bırakmak için pady değeri artırıldı

    def delete_emergency(self):
        selected_item = self.emergency_tree.focus()
        if not selected_item:
            messagebox.showwarning("Seçim Yok", "Lütfen silmek için bir acil durum kaydı seçin.")
            return

        confirm = messagebox.askyesno("Silme Onayı", "Seçili acil durum kaydını silmek istediğinizden emin misiniz?")
        if confirm:
            values = self.emergency_tree.item(selected_item, 'values')
            emergency_id = values[0]
            try:
                self.db.execute_query("DELETE FROM emergency_events WHERE id=?", (emergency_id,))
                messagebox.showinfo("Başarılı", "Acil durum kaydı başarıyla silindi.")
                self.load_emergency_data() # Listeyi güncelle
            except Exception as e:
                messagebox.showerror("Hata", f"Acil durum kaydı silinirken bir hata oluştu: {e}")

    # ... (diğer kodlar) ...
    # --- Acil Durum Düzenleme ---
    
    # --- Raporlar Modülü ---
    def show_reports_module(self):
        self.clear_content_frame()
        tk.Label(self.content_frame, text="Raporlar Modülü", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=20)
        
        # Buraya raporlama ile ilgili widget'ları ekleyebilirsiniz.
        # Örneğin, farklı rapor türleri için butonlar veya tarih seçiciler.
        tk.Label(self.content_frame, text="Bu bölümde çeşitli raporları görüntüleyebilir ve dışa aktarabilirsiniz.", bg="#ecf0f1").pack(pady=10)
        tk.Label(self.content_frame, text="Geliştirme aşamasındadır...", bg="#ecf0f1", fg="gray").pack(pady=5)