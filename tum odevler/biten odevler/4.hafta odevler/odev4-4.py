##4-)Futbolcular dosyasındaki futbolculardan ismi sesli harf ile
##başlayanları ayrı bir dosyaya yazdırınız.


with open("futbolcular.txt")as file:##dasyayi actik
    liste=file.readlines()##degerleri listeledik
sesli_harfler="AaEeIiOoUu" ##sesli harleri degisken aldik
for i in liste:##listedeki elemanlari kontrol icin for dongusunu aldik
    for a in sesli_harfler:##sesli harfler tek tek kontrol etmek icin dongu icine aldik
        if i.startswith(a):##eger i ilk harfi sesli harler icinden biri ise
            print(i)##yazdiriyoruz
            with open("seslifutbolcular.txt","a")as dosya: ##dosyayi actik
                      dasya.write(i)##dasyaya yazdir
        
