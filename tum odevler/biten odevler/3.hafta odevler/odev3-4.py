##4.ODEV: ALAN-HACIM HESAPLAMA
##   Karenin, ucgenin ve diktortgenin alanlarini hesaplayan,
##kup,kure ve koni seklinde olan cisimlerin hacmini hesaplayan
##bir program yazmanizi istiyoruz.
# Kullanicidan hangi seklin alanini veya
##hangi sekildeki cismin hacmini hesaplamak istedigini sormalisiniz ve
##o islem icin gereken verileri isteyip hesaplamayi yapmalisiniz.
###Tum bu islemleri yaparken hata alinabilecek durumlari ongorerek
##gerekli onlemleri almalisiniz.

menu="""
1-Alan islemleri
2-Hacim islemleri
3-Cikis
"""

alan_hesap="""
\t\tALAN HESAPLAMALARI
\t3.Kare
\t4.Ucgen
\t5.Dikdortgen"""

hacim_hesap="""
\t\tHACIM HESAPLAMALARI
\t6. Kup
\t7. Kure
\t8. Koni"""
print(menu)
while True:
    print(menu)
    secim=input("yapmak ıstedıgınız alanın secımını yapınız:")
    if secim =="1":
        print(alan_hesap)
        secim2=input("istediginiz alan hasebi icin secim yapiniz:")
        if secim2 == "3":
            kenar=float(input("karenin bir kenar uzunlugunuz giriniz:"))
            kare_alan=kenar**2
            print("bir kenari {} olan karenin alani () 'dir".format(kenar,kare_alan))

        elif secim2 =="4":
            kenar=float(input("ucgenin bir kenar uzunlugunu giriniz:"))
            yukseklik=float(input("yukseklik degerini giriniz:"))
            ucgen_alan=kenar*yukseklik/2
            print("bu ucgenin alani {}'dir...".format(ucgen_alan))
        elif secim2 =="5":
            kenar1=float(input("kisa kenar uzunlugu giriniz:"))
            kenar2=float(input("uzun kenar uzunlugu giriniz:"))
            dikdortgen_alan=kenar1*kenar2
            print(dikdortgen_alan,"dikdortgenin alanidir.")
        else:
            print("yanlis secim....")

    elif secim =="2":
        print(hacim_hesap)
        secim3=input("yapmak istediginiz islemi seciniz:")
        if secim3 =="6":
            kup_kenar=float(input("kupun bir kenar uzunlugunu giriniz:"))
            kup_hacim=kup+kenar**3
            print("bu kupun hacmi :",kup_hacmi)

        elif secim3 =="7":
            kure_yaricap=float(input("kurenin yaricapini giriniz:"))
            kure_hacim=(4/3)*(22/7)*(r**3)
            print("kurenin hacmi :",kure_hacim)

        elif secim3 =="8":
            yaricap=float(input("koninin yari capini giriniz:"))
            yukseklik=float(input("koninin yuksekligini giriniz:"))
            koni_hacim=(1/3)*(27/7)*(yapicap**2)*yukseklik
            print("koninin hacmi :",koni_hacim)

        else:
            print("yanlis secim...")

    else:
        print("yanlis islem yaptiniz...")
            
            
            
            
            
            
        
            
            
            
            
            
