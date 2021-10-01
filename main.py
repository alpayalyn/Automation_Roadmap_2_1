
"""Class oluştur, ogrenci sınıfı
-ogrenciAdı
-ogrenciSoyadı
-ogrenciSınıf

bu sınıflardan nesne oluştururken parametre üreteceğiz
"""
"""
Soru adında bir sınıf olacak
-NetSayısı() fonk olacak
-Hesapla() fonk olacak. Hesapla net sayısını alıp öğrencinin puanını alır Her net 2 puan
"""
"""
En sonda öğrenci bilgileri ve puan konsolda gösterilecek
"""

class ogrenciSiniffi:

    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinifi):
        self.ogrenciAdi = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.ogrenciSinifi = ogrenciSinifi

    def bilgilerigöster(self):
        print(""" 
              ogrenciAdi : {}
              ogrenciSoyadi : {}
              ogrenciSinif : {}
              """.format(self.ogrenciAdi, self.ogrenciSoyadi, self.ogrenciSinifi))

class Soru:

    def __init__(self, ogrencidogru, ogrenciyanlis):
        self.Dogru = ogrencidogru
        self.Yanlis = ogrenciyanlis
        self.ToplamNet = 0
        self.ToplamPuan = 0

    def NetSayisi(self):

        Yanlis_Net1 = int(self.Yanlis / 4)
        self.ToplamNet = self.Dogru - self.Yanlis - Yanlis_Net1

        print("""
              ogrenciDogruSayisi : {}
              ogrenciYanlisSayisi : {}
              ogrenciNetSayisi : {}
              """.format(self.Dogru, self.Yanlis, self.ToplamNet))

    def Calculate(self):

        self.ToplamPuan = self.ToplamNet * 2
        print(""" 
              ogrenciToplamPuani : {}
              """.format(self.ToplamPuan))


ogrenciismi = input("Öğrenci ismi giriniz:")
ogrencisoyismi = input("Öğrenci soyismi giriniz:")
ogrencisinifi = input("Öğrenci sinifini giriniz:")
ogrencidogru = int(input("Öğrenci doğru sayısını giriniz:"))
ogrenciyanlis = int(input("Öğrenci yanlış sayısını giriniz:"))


ogrenci1 = ogrenciSiniffi(ogrenciismi, ogrencisoyismi, ogrencisinifi)
ogrenci1.bilgilerigöster()

ogrenci2 = Soru(ogrencidogru, ogrenciyanlis)
ogrenci2.NetSayisi()
ogrenci2.Calculate()
