##5.ODEV: ATM
##Kullanicinin hesabinda 1000 € olsun.
##Kullaniciya hangi islemi yapmak istedigini sorun.
##Kullanicinin yapabilecegi islemler:
##        1-bakiye kontrolu
##        2-para yatirma
##        3-para cekme
##    Kullanici hesabinda olan paradan fazla para cekmek isterse uyarin ve
##islemi yapamayacagini soyleyin.
##    2. ve 3. islemler sonucunda guncel bakiyeyi kullaniciya gosterin.
##Baska bir islem yapmak isteyip istemedigini sorun.


bakiye=1000
kontrol=0

while kontrol ==0:
    print("""bakiye kontrolu icin 1'e basiniz
        para yatirma icin 2'ye basiniz
        para cekmek icin icin 3'e basiniz
        cikmak icin 4' e basiniz""")
    secim=int(input("seciminiz:"))
    if secim ==1:
        print("toplam bakiyeniz",bakiye,"€ dur")

    elif secim ==2:
        para=float(input("yatirmak istediginiz para miktarini giriniz:"))
        bakiye+=para
        print("bakiyenize {} € yatirildi..".format(para))
        print("toplam bakiyeniz",bakiye,"€ dur")
    elif secim == 3:
        para=float(input("cekmek istediginiz para miktarini giriniz:"))
        if bakiye<para:
            print("boyle bir islem yapamazsiniz...")
        else:
            bakiye-=para
            print("bakiyenizden {} € cekildi..".format(para))
            print("toplam bakiyeniz",bakiye,"€ dur")
            

    elif secim ==4:
        kontrol=1
    else:
        print("""bakiye kontrolu icin 1'e basiniz
        para yatirma icin 2'ye basiniz
        para cekmek icin icin 3'e basiniz
        cikmak icin q ya basiniz""")
        

