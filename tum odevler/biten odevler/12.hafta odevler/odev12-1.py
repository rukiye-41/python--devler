##Tasit isimli bir sinif tanimlayiniz.
##Bu sinif icerisinde sinif ozelligi (class method) olarak
##tasit_miktari isimli bir bos liste tanimlayiniz.
##Bu tasit sinifinin motor_gucu,
##koltuk_sayisi,
##km_durumu, modeli,
##satis_yili
##gibi obje ozellikleri(instance attributes) olsun.
##Ve her orneklenme durumunda bu ozellikler parametre olarak verilsin.
##Ayrica her ornekte degismeyecek sekilde;
##tekerlek sayisi isimli bir ornek niteligi tanimlayin ve degeri 4 olsun.
##Ayrica bu objenin su methodlari olmalidir:
##
##1.koltuk sayisini goster(tasitin koltuk sayisini ekrana yazdirmali  
##2.modelini goster (tasitin modelini ekrana yazdirmali)
##3. km_durumunu al (tasitin kilometre durumunu return etmeli) 
##4. tasit miktarini_guncelle. Sinif her orneklendiginde tasit miktarini 1 artirmali.
##
##- bu sinifa ait ozellik olan tasit_miktari’ni sinif disarisindan ulasilamayacak sekilde gizleyiniz.
##- class method olarak tasit_miktarini gosterecek bir method tanimlayiniz.
##Sorunun devaminda, bir Araba sinifi tanimlayiniz ve bu sinifi, Tasit sinifindan miras aliniz. Tasit sinifindan miras aldiginiz init fonksiyonunu muhafaza ediniz ve max_hiz isimli bir ornek niteligi tanimlayiniz ve bu nitelik her orneklenme durumunda parametre olarak verilsin. Bu sinifta su methodlari tanimlayiniz;
##
##1.arabayi_durdur (“araba durdu” seklinde ekrana yazsin)
##2. gaza_bas(“araba hizlaniyor” seklinde ekrana yazsin)
##3.  arabayi_yavaslat(“araba yavasliyor” seklinde ekrana yazsin)
##4. arabanin_durumunu goster(bir kosul durumu yaziniz;eger Araba sinifi Tasit sinifinin alt sinifi ise 
##“Bu sinif Tasit sinifindan miras alinmistir” seklinde cikti versin. Degilse ‘ Araba sinifi Tasit sinifindan 
##miras alinmamistir.’ seklinde yazsin)
##Ayrica bu Araba sinifinda; modelini goster isimli Tasit sinifina ait methodu override ediniz ve ‘Araba sinifinin methodu….’ seklinde ekrana cikti veriniz ve modeli yazdiriniz.
##
##


class tasit():
    tasit_miktari = []

    def __init__(self, motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili):
        self.motor_gucu = motor_gucu
        self.koltuk_sayisi = koltuk_sayisi
        self.km_durumu = km_durumu
        self.modeli = modeli
        self.satis_yili = satis_yili
        self.tekerlek_sayisi = 4

    def modeli_goster(self):
        print("arabanin modeli", self.modeli)

    def koltuk_sayisigoster(self):
        print("arabanin toplam koltuk sayisi:", self.koltuk_sayisi)

    def km_durumugoster(self):
        return print("arabanin km durumu:", self.km_durumu)

    def goruntule(self):
        print("tasitin motor gucu:",self.motor_gucu,"\n","tasitin modeli:",self.modeli,"\n","tasitin koltuk sayisi:",self.koltuk_sayisi,"\n","tasitin km durumu:",self.km_durumu,"\n","tasitin satilis yili:",self.satis_yili)


    @classmethod
    def tasit_miktarini_goster(cls):
        return len(cls.tasit_miktati)


class araba(tasit):
    def __init__(self, motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili, max_hiz, fren, hafif_fren):
        super().__init__(motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili)
        self.max_hiz = max_hiz
        self.fren = fren
        self.hafif_fren = hafif_fren

    def arabayi_durdur(self):
        print("araba durdu..", self.fren)

    def gaza_bas(self):
        print("arabanin max hizi:", self.max_hiz)
        print("arabanin hizlaniyor..")

    def arabayi_yavaslat(self):
        print("araba yavasliyor..", self.hafif_fren)

    def durum(self):
        if isinstance(araba, tasit):
            print("Bu sinif Tasit sinifindan miras alinmistir")
        else:
            print("Araba sinifi Tasit sinifindan miras alinmamistir.")

    def modeli_goster(self):
        print("araba sinifinin modeli")
        super().modeli_goster()

    def goster(self):
        print("arabanin motor gucu:",self.motor_gucu,"\n","arabanin modeli:",self.modeli,"\n","arabanin koltuk sayisi:",self.koltuk_sayisi,"\n","arabanin km durumu:",self.km_durumu,"\n","arabanin satilis yili:",self.satis_yili,"\n","arabanin max. hiz:",self.max_hiz,"\n","en dusuk fren seviyesi:",self.fren,"\n","arabanin hafif fren seviyesi:",self.hafif_fren)


toyoto=araba(2,5,150.000,"toyoto aygo",2018,300,0,5)
mercedes=tasit(2.2,7,200.000," S-Klasse",2015)
bwm=araba(6,5,0," Gran Turismo",2019,600,0,5)
ferrari=araba(800,5,4.670,"812 Superfast 6.5",2018,250,0,5)

print(toyoto.tekerlek_sayisi)
mercedes.koltuk_sayisigoster()
bwm.km_durumugoster()
ferrari.durum()
print(toyoto.goster)
toyoto.modeli_goster()



