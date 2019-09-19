####3.ODEV: LISTE AYIKLAMA
####Ekte gonderilmis olan text dosyasinda
##3 takimin futbolcularinin isimlerive takimlari yer almaktadir.
##Sizden 3 tane dosya olusturmanizi
####ve bu 3 dosyaya futbolculari takimlarina gore ayirmanizi istiyoruz.
##Ayrica kaynak dosyanin bulunamamasi durumunda da gerekli uyariyi yapmalisiniz.

file=open("futbolcular.txt","r") ##ayiklayacigimiz dosyayi actik
veri=file.readliens()  ##dosya icindekileri satir satir liste seklinde veri degiskenine atadik
for i in veri:   #veri listesindeki elemanlari tek tek gostermek icin for dongusu actik
    if "besiktas" in i:  #eger listenin elemaninda yani bir satirlarinda besiktas varsa
        file1=open("bjk.txt","a")  ##bjk.txt dosyasini ac 
        file1.write(i)  ##listedeki veriyi bu dosyaya yaz

    elif "fenerbahce" in i:    ## eger listenin elemaninda yani bir satirlarinda Fenerbahce varsa
        file2=open("fb.txt","a") ##fb.txt dosyasini ac
        file2.write(i)  ##listedeki veriyi bu dosyaya yaz
    elif "galatasaray" in i:##eger listenin elemaninda yani bir satirlarinda galatasarat varsa
        file3=open("gs.txt","a")##gs.txt dosyasini ac
        file3.write(i)##listedeki veriyi bu dosyaya yaz
    else:
        print("kaynak dosyalar bulunamiyor...")

file.close()  ##dosyalari kapatiyoruz
file1.close()
file2.close()
file3.close()
print("dosyaniz ayiklandi")
