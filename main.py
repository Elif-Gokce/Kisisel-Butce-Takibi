from models import BudgetManager, ReportGenerator,Transaction

if __name__ == "__main__":
    manager =BudgetManager()
    manager.load_from_file()                
    report =ReportGenerator(manager)

    while True:
        print("\n*****Bütçe Takip Menüsü *****")
        print("1-İşlem ekle")
        print("2-İşlemleri Listele")
        print("3-Kategori Raporu")
        print("4-Özet Rapor")
        print("5-İşlem Ara")
        print("6-İşlem Sil")
        print("7-Çıkış")

        choice =input("Seçiminizi girin :")

        if choice == "1":
            try:
                amount = float(input("Miktar : "))
            except ValueError:
                print(" Miktar sayısal olmalı!")
                continue  

            category = input("Kategori : ").strip()
            if not category:
                print(" Kategori boş olamaz.")
                continue

            type_ = input("Tür(Gelir/Gider) : ").capitalize()
            date = input("Tarih (YYYY-AA-GG) : ")

            t = Transaction(amount, category, type_, date)
            manager.add_transaction(t)
            manager.save_to_file()
            print("✅ İşlem eklendi.")
       

        elif choice == "2":
            for i, t in enumerate(manager.transactions):
                print(f"{i}. {t}")

        elif choice == "3":
            print(report.category_report())

        elif choice == "4":
            print(manager.summary())

        elif choice == "5":
            keyword = input("Aramak istediğiniz kelimeyi girin: (kategori/tarih/tür/miktar): ")
            results = manager.search_transaction(keyword)
            if results :
                for r in results:
                    print(r)
            else:
                print("Hiçbir işlem bulunamadı.")

        elif choice == "6":
            for i,t in enumerate(manager.transactions):
                print(f"{i}. {t}")
            index =int(input("Silmek istediğiniz işlem numarsını girin:"))
            if manager.delete_transaction(index):
                 manager.save_to_file()
                 print("İşlem silindi.")
            else:
                print("Geçersiz numara.")

        elif choice == "7":
            manager.save_to_file()
            print("Programdan çıkılıyor...")
            break

        else:
            print("Geçersiz seçim, tekrar deneyiniz.")

        secim = input("\nAna menüye dönmek için Enter’a basın, çıkış için Q yazın: ")
        if secim.lower() == "q":
            print("Programdan çıkılıyor...")
            break