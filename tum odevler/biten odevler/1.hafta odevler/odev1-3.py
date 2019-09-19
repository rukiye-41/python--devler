##3-
##Oğrenci not ortalama programi
##
##Icerik:
##Kullanicidan input ile ad-soyad, vize, final ve ders takip bilgilerini alip bu degerleri yuzdelik oranlarina gore hesaplayin ve yil sonu notunu cikarin.
##
##Yontem:
##-Sinav puanlari ve ders takip puani 0-100 arasidir. 
##-Bir öğrencinin gitmesi gereken toplam ders sayısı 20’dir. Kaçırılan her ders için 5 puan kırılacaktır. (Orn: 3 ders kaciran bir ogrencinin ders takip puani: 100-(3x5)=85 )
##Oranlar :
##- Vize Notu ( 30%)
##- Final Notu (50%)
##- Ders takip (20%)
##
##Sonuc:
##    0.    Output olarak ogrencinin yil sonu puanini ekrana pritleyin. 
##    0.    Ogrenci ad-soyad, vize-final-ders takip bilgilerini ve hesapladiginiz yil sonu puanini “ogrenciNotHesaplama” isimli bir dosyaya kaydedin.

adi=input("ogrencinin adi:")
soyadi=input("ogrencinin soyadi:")
vize=int(input("ogrencinin vize notu:"))
final=int(input("ogrencinin final notu:"))
kacan_ders=int(input("ogrencinin kacirdigi ders:"))
derstakip=(100-(kacan_ders*5))*0.2
yilsonu_notu =vize*0.3+final*0.5+derstakip
print(adi,soyadi,"adli ogrencinin yil sonu ortalamasi:",yilsonu_notu,"dir")
dosya=open("ögrenci Not Hesaplama.txt","w")
print("adı:" ,adı, "soyadı:",soyadı, "yıl sonu notu:",yılsonunotu,sep="",file=dosya)
dosya.close()
