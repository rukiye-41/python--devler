##2.ODEV: SAYI TAHMIN OYUNU
##   Bir degiskene 0-100 arasinda bir deger atayin. 
# Kullanicidan bu sayiyi tahmin etmesini isteyin. 
# Kullaniciyi yaptigi tahminlere gore yonlendirin.
##Kacinci denemede bildigini soyleyin.
##Ornek:
###       sayi = 76
###       kullanicinin tahmini = 5
###       cikti = cok dusuk tahminde bulundun daha yuksek bir sayi girmelisin.
###       kullanicinin tahmini = 95
###       cikti = fazla yukari ciktin biraz asagi in.
###       kullanicinin tahmini = 80
###       cikti = cok yaklastin biraz daha inmelisin
###       kullanicinin tahmini = 73
###       cikti = cok yaklastin biraz daha cikmalisin
###       kullanicinin tahmini = 76
###       cikti= tebrikler sayiyi 5.denemede buldunuz

print("\t sayi tAHMIN OYUNUNNA HOSGELDINIZ")
sayi=45
tahmin=0
print("oyunu oynamak icin 1'e basiniz\n cikmak icin 2'ye basiniz")
secim=input("seciminiz:")
if secim =="1":
    while True:
        tahminim=int(input("tahmininiz:"))
        tahmin+=1
        if tahminim>sayi :
            if tahminim-sayi<=5:
                print(" cok yaklastin Biraz daha asagi inmelisin..")
            else:   
                print("Fazla yukari ciktin daha asagi inmelisin ...")
        elif(tahminim<sayi): 
            if sayi-tahminim<=5:
                print(" cok yaklastin Biraz daha cikmalisin..")
            else:
                print("Fazla asagi indin biraz yukari cikmalisin...") 
        elif tahminim==sayi:
            print(sayi,"sayisini {} denemede bildiniz...".format(tahmin))
            break

if secim =="2":
    print("cikiliyor...")
      
              
    
             
