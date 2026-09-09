import json

#İşlemleri tutan sınıf
class Transaction:
    def __init__(self,amount,category,type,date):
        self.amount = amount     #Miktarı
        self.category = category #Kategori
        self.type = type         #Türü
        self.date = date         #Tarih

    def to_dict(self):           #nesneyi JSON’a uygun hale getirir
        return {
            "amount":self.amount,
            "category":self.category,
            "type":self.type,
            "date":self.date
        }

    @staticmethod                 #nesneye (self) ihtiyaç duymayan fonksiyonlarda kullanılır
    def from_dict(data):          #JSON’dan nesne oluşturur 
        return Transaction(
            data["amount"],
            data["category"],
            data["type"],
            data["date"]
        )

    def __str__(self):
        return f"{self.date} - {self.category} ({self.type}): {self.amount} TL"

#Kategorileri tutan sınıf 
class Category:
    def __init__(self,name):
        self.name=name          #Adı
        self.transactions=[]    #İşlemler

    def add_transaction(self,transaction):     #Yeni işlem ekleme fonk.
        self.transactions.append(transaction)

    def total_amount(self):                    #Toplam miktarı dönderen fonk.
        return sum(t.amount for t in self.transactions)

#Projeyi yöneten sınıf
class BudgetManager:
    def __init__(self):
        self.transactions=[]    #İşlemleri saklayan liste
        self.categories={}      #Kategorileri saklayan sözlük

    def add_transaction(self,transaction):     #Yeni işlem ekleme fonk.
        self.transactions.append(transaction)
        if transaction.category not in self.categories:
            self.categories[transaction.category]  =Category(transaction.category)
        self.categories[transaction.category].add_transaction(transaction)

    def summary(self):                          #Özet rapor döndüren fonk.
        total_income =sum(t.amount for t in self.transactions if t.type == "Gelir")
        total_expense =sum(t.amount for t in self.transactions if t.type == "Gider")
        balance=total_income-total_expense
        return f"Gelir : {total_income} TL | Gider : {total_expense} TL | Bakiye : {balance} TL"

    def search_transaction(self, keyword):      #Arama yapan fonk.
        return [
            t for t in self.transactions
            if keyword.lower() in t.category.lower()             # kategoriye göre arama
            or keyword in t.date                                 # tarihe göre arama
            or keyword.lower() in t.type.lower()                 # tür (Gelir/Gider) arama
            or keyword.isdigit() and float(keyword) == t.amount  # miktar arama
        ]

    def delete_transaction(self,index):         #Silme yapan fonk.
        if 0 <= index < len(self.transactions):
            transaction = self.transactions.pop(index)

            # Kategoriden de sil
            if transaction.category in self.categories:
                category = self.categories[transaction.category]
                category.transactions.remove(transaction)

                # Eğer kategori tamamen boşsa kategoriyi de sil
                if not category.transactions:
                    del self.categories[transaction.category]

            return True
        return False
           
    def save_to_file(self, filename="data/data.json"): #verileri JSON dosyasına yazar
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump([t.to_dict() for t in self.transactions], f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f" Dosya kaydedilirken hata oluştu: {e}")


        
    def load_from_file(self, filename="data/data.json"): #JSON dosyasından okur ve nesnelere çevirir
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:  
                    print(" data.json dosyası boş, yeni veriyle başlanıyor.")
                    self.transactions = []
                    self.categories = {}
                    return
                data = json.loads(content)
                self.transactions = [Transaction.from_dict(d) for d in data]

                # Kategorileri yeniden oluştur
                self.categories = {}
                for t in self.transactions:
                    if t.category not in self.categories:
                        self.categories[t.category] = Category(t.category)
                    self.categories[t.category].add_transaction(t)

        except FileNotFoundError:
            print(" data.json bulunamadı, yeni dosya oluşturulacak.")
            self.transactions = []
            self.categories = {}
        except json.JSONDecodeError:
            print(" data.json bozuk, sıfırdan başlatılıyor.")
            self.transactions = []
            self.categories = {}  

#Rapor üretici sınıf (Kategori bazlı özet)
class ReportGenerator:
    def __init__(self,manager):
         self.manager=manager # BudgetManager nesnesini alır, onun verilerini kullanır

    def category_report(self):
        report ="Kategori Bazli Rapor : \n" 
        for name,category in self.manager.categories.items():
            report+=f"-{name} : {category.total_amount()} TL \n"
        return report    
