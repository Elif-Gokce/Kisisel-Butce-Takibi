# Kişisel Bütçe Takibi

Bu proje, konsol tabanlı bir **kişisel bütçe takip uygulamasıdır**. Kullanıcılar gelir ve gider işlemlerini ekleyebilir, listeleyebilir, arayabilir, güncelleyebilir ve silebilir. Ayrıca kategori bazlı raporlar ve genel özet raporları görüntüleyebilirler. Veriler **JSON dosyasında kalıcı olarak saklanır**, böylece program kapatılıp açıldığında işlemler kaybolmaz.

---

## 🚀 Nasıl Çalıştırılır?

1. Projeyi bilgisayarınıza indirin .
2. Python 3.x yüklü olduğundan emin olun.
3. Terminal veya komut satırında aşağıdaki komutu çalıştırın:

```bash
python main.py
```
4. Program açıldığında menüden seçim yaparak işlemleri gerçekleştirebilirsiniz.

## ✅ Özellikler
- Gelir ve gider işlemleri ekleme
- İşlemleri listeleme
- Kategori bazlı rapor
- Özet rapor (toplam gelir, gider, bakiye)
- İşlem güncelleme
- İşlem arama
- İşlem silme
- JSON dosyasında kalıcı veri saklama
  
## 📚 Kullanılan Konular
### OOP (Nesne Tabanlı Programlama)

- **Transaction sınıfı** → Tek bir işlem (gelir/gider) bilgisini tutar.

- **BudgetManager sınıfı** → İşlemleri yönetir (ekleme, silme, güncelleme, arama, dosya kaydetme/yükleme).

- **Category sınıfı** → Kategori bazlı işlemleri ve toplamları tutar.

- **ReportGenerator** sınıfı → Raporlama işlemlerini yapar.

### Konsol tabanlı menü
- while True döngüsü ile kullanıcıya seçenek sunulur.

### Dosya işlemleri 
- JSON formatında veri kaydı (data/data.json).

### Hata yönetimi (try/except) 

- Dosya bulunamadığında yeni dosya oluşturma.

- Geçersiz girişlerde kullanıcıya uyarı verme (örneğin miktar sayısal değilse, tarih formatı yanlışsa).

### Veri yapıları 

- Liste (transactions)

- Sözlük (categories)

#### Arama özelliği 
- Kullanıcı kategori, tarih, tür veya miktara göre arama yapabilir.

### Raporlama 

- Özet rapor (toplam gelir, gider, bakiye)

- Kategori bazlı rapor (her kategori için gelir/gider/net)

## 🛠️ Kullanılan Teknolojiler
- Python 
- JSON
- OOP 

##  Veri Kaynağı
Veriler `data/data.json` dosyasında saklanır. Program kapatılıp açıldığında işlemler bu dosyadan yüklenir.

## 📁 Proje Dizin Yapısı
```text
 .           
 ├── data/         
 │   └── data.json               
 ├── .gitignore          
 ├──  main.py   
 ├──  models.py             
 └──  README.md
```

## 📸 Örnek Ekran Görüntüsü
### Ana Menü

<img width="1280" height="258" alt="image" src="https://github.com/user-attachments/assets/9ec3f29f-3d86-4fe5-9f93-aa172b30857a" />

### İşlem Ekle ve İşlem Listele 

<img width="1277" height="542" alt="image" src="https://github.com/user-attachments/assets/b5d911f7-82c4-440d-a431-cd2c82a445d9" />

### Kategori Raporu
<img width="1280" height="342" alt="image" src="https://github.com/user-attachments/assets/9723aaf1-8ccd-42a5-ad9c-ade610cc4b92" />

### Özet Raporu
<img width="1280" height="341" alt="image" src="https://github.com/user-attachments/assets/86359bd3-fd16-4c69-8ad7-43429acbe27f" />

### İşlem Güncelle
<img width="1280" height="641" alt="image" src="https://github.com/user-attachments/assets/cbdee970-ab7d-4d77-8b84-86969f1e20df" />

### İşlem Ara
<img width="1280" height="251" alt="image" src="https://github.com/user-attachments/assets/92e48cd4-9b3a-4ab9-8d42-7a809480a90c" />

### İşlem Sil
<img width="1278" height="581" alt="image" src="https://github.com/user-attachments/assets/32d13b32-6635-4470-bb87-54a219a1f18c" />












