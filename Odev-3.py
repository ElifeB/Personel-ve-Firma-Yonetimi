class Personel:
    def __init__(self, ad, departman, çalışma_yılı, maaş):
        self.ad = ad
        self.departman = departman
        self.çalışma_yılı = çalışma_yılı
        self.maaş = maaş

class Firma:
    def __init__(self):
        self.personel_listesi = []
    
    def personel_listele(self):
        sorted_personel_listesi = sorted(self.personel_listesi, key=lambda x: x.ad)  # Personel listesini isme göre sırala
        for i, personel in enumerate(sorted_personel_listesi, start=1):
            print(f"{i}) {personel.ad} ({personel.departman}) - Maaş: {personel.maaş}")
        print("\nHangi işlemi yapmak istersiniz?")
        print("1) Zam")
        print("2) Personel Ekleme")
        print("3) Personel Çıkarma")

    def personel_ekle(self, personel):
        self.personel_listesi.append(personel)
        print(f"{personel.ad} eklendi.")

    def personel_çıkar(self, personel_adı):
        for personel in self.personel_listesi:
            if personel.ad.lower() == personel_adı.lower():
                self.personel_listesi.remove(personel)
                print(f"{personel.ad} çıkarıldı.")
                return
        print(f"{personel_adı} isimli personel bulunamadı.")

    def maaş_zammı(self, personel_adı, zam_oranı):
        for personel in self.personel_listesi:
            if personel.ad.lower() == personel_adı.lower():
                personel.maaş *= (1 + zam_oranı / 100)
                print(f"{personel.ad}'ın maaşı %{zam_oranı} oranında artırıldı. Yeni maaş: {personel.maaş}\n")
                return
        print(f"{personel_adı} isimli personel bulunamadı.")

firma = Firma()

personel1 = Personel("Elife", "Bilgisayar Mühendisliği", 3, 3500)
personel2 = Personel("Ahmet", "Makine Mühendisliği", 5, 4000)

firma.personel_ekle(personel1)
firma.personel_ekle(personel2)

while True:
    firma.personel_listele()  # Personel listesini göster

    secim = input("İşlem numarasını girin (Çıkış için 'q' tuşuna basın): ")

    if secim == '1':  # Zam işlemi
        personel_adı = input("Zam yapmak istediğiniz personelin adını girin: ")
        zam_oranı = float(input("Yüzde olarak zam oranını girin: "))
        firma.maaş_zammı(personel_adı, zam_oranı)
    elif secim == '2':  # Personel ekleme işlemi
        ad = input("Yeni personelin adını girin: ")
        departman = input("Departmanını girin: ")
        çalışma_yılı = int(input("Çalışma yılını girin: "))
        maaş = float(input("Maaşını girin: "))
        yeni_personel = Personel(ad, departman, çalışma_yılı, maaş)
        firma.personel_ekle(yeni_personel)
    elif secim == '3':  # Personel çıkarma işlemi
        personel_adı = input("Çıkarmak istediğiniz personelin adını girin: ")
        firma.personel_çıkar(personel_adı)
    elif secim.lower() == 'q':  # Çıkış
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz işlem numarası. Lütfen tekrar deneyin.")
