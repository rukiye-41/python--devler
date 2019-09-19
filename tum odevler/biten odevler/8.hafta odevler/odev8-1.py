#Asal sayi olup olmadigini kontrol eden fonksiyon yazınız.
#asalsayı=sadece kendisi ve 1 sayısına bölünebilen 1'den büyük pozitiftam sayılara denir

print("asal sayı hesaplama programına hoş geldiniz....")
secenek=("asalsayı hesaplamak için 1'e basınız\nçıkmak için 2'ye basınız\n")
print(secenek)

def asalsayı_kontrol(sayı):
    if(sayı >1):   #1 asal sayıdeğildir. sayı birden küçükse asalsayı olmadıgını söyleyeceğiz.
        for i in range(2,sayı):    #eger sayımız birden büyükse kontrol et dedik.. kalansız bölünmesi için
            if (sayı%i==0):
                return False
        return True
    else:
        return False
while (True):
    secim=input("seciminiz:")
    if secim=="1":
        sayı=(int(input("kontrol etmek istediğiniz sayıyı giriniz:")))
        print(asalsayı_kontrol(sayı))
        continue
    if secim=="2":
        çıkış=(input("çıkmak için 2'e basınız"))
        if çıkış=="2":
            print("çıkılıyor..")
            break
    else:
        print("yanlış seçim tekrar seçiniz..")

asalsayı_kontrol(sayı)
