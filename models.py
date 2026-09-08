#İşlemleri tutan sınıf
class Transaction:
    def __init__(self,amount,category,type,date):
        self.amount = amount     #Miktarı
        self.category = category #Kategori
        self.type = type         #Türü
        self.date = date         #Tarih

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

#Rapor üretici sınıf (Kategori bazlı özet)
class ReportGenerator:
    def __init__(self,manager):
         self.manager=manager # BudgetManager nesnesini alır, onun verilerini kullanır

    def category_report(self):
        report ="Kategori Bazli Rapor : \n" 
        for name,category in self.manager.categories.items():
            report+=f"-{name} : {category.total_amount()} TL \n"
        return report    
