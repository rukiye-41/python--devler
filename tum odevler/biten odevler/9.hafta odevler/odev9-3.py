##ODEV 3: pzt = [ { 'isim': 'Fonksiyonlara calis', 'sure': 180 }, { 'isim': 'ornek coz', 'sure': 120 }, { 'isim': 'odev kontrol', 'sure': 20 }, { 'isim': 'bayramlasma', 'sure': 200 } ]
##
##sali = [ { 'isim': 'gelecek haftaya hazirlik', 'sure': 240 }, { 'isim': 'ornek cozumlerine devam et', 'sure': 180 }, { 'isim': 'kahve molasi', 'sure': 10 }, { 'isim': 'kitap oku', 'sure': 200 }, { 'isim': 'spor yap', 'sure': 40 } ]
##
##Not: Sureler dakika cinsindendir!
##
##Map, filter ve reduce kullanarak yukarida belirtilen iki gunluk plan neticesinde kac puan kazanilacagini hesaplayan bir program yaziniz.

##
##•	Map ile sureleri saat cinsine donusturun.

from functools import reduce



pzt = [ { 'isim': 'Fonksiyonlara calis', 'sure': 180 },
        { 'isim': 'ornek coz', 'sure': 120 },
        { 'isim': 'odev kontrol', 'sure': 20 },
        { 'isim': 'bayramlasma', 'sure': 200 } ]

sali = [ { 'isim': 'gelecek haftaya hazirlik', 'sure': 240 },
         { 'isim': 'ornek cozumlerine devam et', 'sure': 180 },
         { 'isim': 'kahve molasi', 'sure': 10 },
         { 'isim': 'kitap oku', 'sure': 200 },
         { 'isim': 'spor yap', 'sure': 40 } ]


a=reduce(lambda sayi1,sayi2:sayi1+sayi2,(map(lambda sayi: round(sayi*20),list(filter(lambda sayi:sayi>2,list(map(lambda sozluk:sozluk["sure"]/60,pzt)))))))
### Map ile sureler saat cinsinden yuvarlandi
### Filter ile saat 2den buyuk ise degerler filtrelendi
### Reduce ile 2den buyuk tum sureler toplandi
### round ile sayilari float deger vermesini engelledim

b=reduce(lambda sayi1,sayi2:sayi1+sayi2,(map(lambda sayi: round(sayi*20),list(filter(lambda sayi:sayi>2,list(map(lambda sozluk:sozluk["sure"]/60,sali)))))))
##print("Toplam puan:",(a+b)*20)  
print("pazartesi puani:",a)
print("sali puani:",b)
print("toplam puan:",a+b)




