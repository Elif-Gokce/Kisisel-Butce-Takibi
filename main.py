from models import BudgetManager, ReportGenerator,Transaction

if __name__ == "__main__":
    manager =BudgetManager()
    manager.load_from_file()                
    report =ReportGenerator(manager)

    while True:
        try:
            print("\n*****Bütçe Takip Menüsü *****")
            print("1-İşlem ekle")
            print("2-İşlemleri Listele")
            print("3-Kategori Raporu")
            print("4-Özet Rapor")
            print("5-İşlem Ara")
            print("6-İşlem Sil")
            print("7-Çıkış")

            choice =input("Seçiminizi girin :")

            if choice not in ["1","2","3","4","5","6","7"]:
                print(" Geçersiz seçim, lütfen 1-7 arasında bir değer girin.")
                continue


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

                from datetime import datetime
                date = input("Tarih (YYYY-AA-GG) : ")
                try:
                    datetime.strptime(date, "%Y-%m-%d")
                except ValueError:
                    print(" Tarih formatı yanlış! Örn: 2026-09-10")
                    continue

                t = Transaction(amount, category, type_, date)
                manager.add_transaction(t)
                manager.save_to_file()
                print("İşlem eklendi.")
        

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
                for i, t in enumerate(manager.transactions):
                    print(f"{i}. {t}")

                try:
                    index = int(input("Silmek istediğiniz işlem numarasını girin: "))
                    if not (0 <= index < len(manager.transactions)):
                        print(" Geçersiz numara.")
                        continue
                except ValueError:
                    print(" Lütfen sayı girin.")
                    continue

                if manager.delete_transaction(index):
                    manager.save_to_file()
                    print(" İşlem silindi.")
                else:
                    print(" Silme başarısız.")                            

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
        except Exception as e:
            print(f" Beklenmeyen hata oluştu: {e}")
            break


