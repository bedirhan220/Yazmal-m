class market:
    ade = 0
    def __init__(self, barkod=[], fiyat=[], ad=[]):
        self.barkod = barkod
        self.fiyat = fiyat
        self.ad = ad

class depo(market):
    def __init__(self, barkod=[], fiyat=[], ad=[], adet=[] ):
        super().__init__(barkod=[], fiyat=[], ad=[])
        self.adet = adet

    def yeni_urun_girisi(self):
        yeni_barkod = int(input("yeni gireceginiz ürürün barkod numarasını giriniz"))
        yeni_fiyat = int(input("yeni gireceginiz ürünün fiyatını giriniz"))
        yeni_ad = input("yeni gireceiğiniz ürünün çeşidinin adını girinizz")
        self.barkod.append(yeni_barkod)
        self.fiyat.append(yeni_fiyat)
        self.ad.append(yeni_ad)
        print(self.barkod)
        print(self.fiyat)
        print(self.ad)
        self.ade = self.ade + 1
        self.adet.append(self.ade)
        print(self.adet)

    def depo_girisi(self):
        eleman = int(input("kacınccı elamanı secmek istiyorsunuz"))
        print(self.barkod[eleman])

    def depo_cıkısı(self):
        barkod_cıkısı = int(input("depodan silmek istediginiz ürünün barkod numarasını giriniz"))
        if barkod_cıkısı in self.barkod:
            print("sildiginiz urun",self.ad)
            self.barkod.remove(barkod_cıkısı)
        else:
            print("tekrar hatalı giris")

    def menu(self):
        print("1-genel urun girisi")
        print("2-depoya ürün girişi")
        print("3-depodan ürün çıkışı")
        print("4-kapat")

    def secim(self):
        sec = int(input("seciminizi giriniz"))
        while sec < 1 or sec > 5:
            sec = int(input("yanlıs girdin bi daha gir"))
        return sec

    def kapat(self):
        return False

urun = depo()
while True:
    urun.menu()
    secimm = urun.secim()
    if secimm == 1:
        urun.yeni_urun_girisi()
    elif secimm == 2:
        urun.depo_girisi()
    elif secimm == 3:
        urun.depo_cıkısı()
    elif secimm == 4:
        urun.kapat()



