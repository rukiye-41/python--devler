##5-
##Aylik masraf programi
##
##Icerik:
##Aylık giderleri ve bu giderlerin aylik gelire oranini hesaplayan bir program yapmanız istenmektedir.
##
##Yontem:
##Asagida belirtilen harcama kalemlerini ve aylik geliri kullanicidan input ile alip gerekli hesaplamalari yapin
##
##Harcama kalemleri:
##-mutfak, 
##-egitim,
##-giyim, 
##-ulasim.
##
##Sonuc:
##1-Kullanicinin aylik toplam masrafini ve bu masrafin aylik gelirine oranini ekrana printleyin. 
##2- Ayni sonucu “aylikmasraf” isimli bir dosyaya kaydedin.

mutfak=int(input("mutfak gider:"))
eğitim=int(input("eğitim gideri:"))
giyim=int(input("giyim gideri:"))
ulasım=int(input("ulasım gideri:"))
aylıkgelir=int(input("aylık geliri giriniz:"))
toplamgider=mutfak+eğitim+giyim+ulasım
print("toplam aylik gideriniz:",toplamgider)
oran=(toplamgider/aylıkgelir)*100
print(toplamgider,"liranin toplamgiderinize orani:",oran,"dir...") 
dosya = open("aylikMasraf.txt","w")
print("{} aylik toplam giderinizin orani {}  dir..".format(toplamgider,oran),file=dosya)
dosya.close()
