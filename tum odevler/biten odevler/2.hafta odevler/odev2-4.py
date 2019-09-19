##ODEV: SAYI TAHMIN OYUNU
##    Bir degiskene 1-10 arasinda bir sayi atayin.Kullanicidan bu sayiyi tahmin etmesini isteyin.
##    Kullanici 5 denemede bilirse 1 yildiz kazansin, 3 denemede bilirse 2 yildiz kazansin, 1 denemede bilirse 3 yildiz kazansin.
print("sayi tahmin oyununa has geldiniz....")
sayi=8
hak=0
tahmin=0

while tahmin ==0:
    print("bilgilendirme\n5 deneme hakkiniz vardir\n ilk denemede bilirseniz 3 yildiz kazanirsiniz\n 2ve 3 denemede bilirseniz 2 yildiz kazanirsiniz\n 4 ve 5 denemede bilirseniz 1 yildiz kazanirseniz\n basarilar...")
    tahminin=int(input("lutfen 1-10 arasinda tahmin giriniz:"))
    hak+=1
    if sayi != tahminin:
        print("bilemediniz..")
    elif sayi ==tahminin:
        tahmin=1
        if hak==1:
            print("tebrikler *** yildiz kazandiniz")

        elif hak==3 and hak==2:
            print("tebrikler ** (2 yildiz)kazandiniz")
        elif hak==5 and hak==4:
            print("tebrikler *(1 yildiz) kazandiniz")

        else:
            print("5 denemeden fazla sayi giriginiz icin yildiz kazanamadiniz...")
    
    if sayi != tahmin and hak==5:
        print("deneme hakkiniz bitti")
        tahmin=1
