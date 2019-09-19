##6.ODEV: ASAL SAYI MI?
##   Kullanicidan aldiginiz sayinin asal sayi olup olmadigini sorgulayan
##bir program yazmanizi istiyoruz.

print("\t asal sayi kontrolu")
sayi=int(input("sayi giriniz:"))
for i in range(2,sayi):
    if sayi % i ==0:
        print("{} asal sayi degildir...".format(sayi))
        break

    else:
        print("{} asal sayidir..".format(sayi))
        break
    
         
