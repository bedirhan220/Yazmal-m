class ogrenci:
    def __init__(self,AdSoyad = [],sınıf = [],yas = [],vize = [],final = []):
        self.AdSoyad = AdSoyad
        self.sınıf = sınıf
        self.yas = yas
        self.vize = vize
        self.final = final

    def ogren(self):
        As= input("ogrenci ismini ve soyismini giriniz")
        snf = int(input("ogrencinin snıfını giriniz"))
        ys = int(input("ogrencinin  yasını giriniz"))
        vz = int(input("ogrencinin  vize notunu giriniz"))
        fn = int(input("ogrencinin  final notunu giriniz"))
        self.AdSoyad.append(As)
        self.sınıf.append(snf)
        self.yas.append(ys)
        self.vize.append(vz)
        self.final.append(fn)
        while True:
            print("ogrencinin adı ve soyadı:",self.AdSoyad)
            print("ogrencinin sınıfı:", self.sınıf)
            print("ogrencinin yaşı:", self.yas)
            print("ogrencinin vize notu:", self.vize)
            print("ogrencinin final notu:", self.final)
            break



    def secim(self):
        sec = int(input("seciminizi giriniz"))
        while sec < 1 or sec > 5:
            sec = int(input("yanlıs girdin bi daha gir"))
        return sec

    def menu(self):
        print("1 - ogrenci bilgileri giriş sistemi")
        print("2 - ogrencinin geçip geçmediğini öğrenmek için  basınız")
        print("3-sistemi kapatmak için q ya basınız")
        print("4-sistem bilgilerini  sıfırlamak için basınız")

    def ortalama(self):
        ogr = int(input("kacıncı ogrencinin ortalamsını görmek istiyorsunuz"))
        ort = self.vize[ogr]  + self.final[ogr]
        if ort > 50:
            print("seçtiğin öğrenci geçti")
        else:
            print("kalmış")

    def kapat(self):
         print("sistem kapandı")
         return False

    def sıfırla(self):
        self.final.clear()
        self.vize.clear()
        print(self.final)
        print(self.vize)


Ogrenci   = ogrenci()

while True:
    Ogrenci.menu()
    secimm = Ogrenci.secim()

    if secimm == 1:
        Ogrenci.ogren()
    elif secimm == 2:
        Ogrenci.ortalama()
    elif secimm == 3:
        Ogrenci.kapat()
    elif secimm == 4:
        Ogrenci.sıfırla()


