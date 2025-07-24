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