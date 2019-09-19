##3.ODEV: PAROLA KARAKTER KONTROLU
##Kullanicidan 3-18 karakter arasinda bir username olusturmasini isteyin.
##Sonrasinda kullanicidan 6 ile 12 karakter araliginda bir parola olusturmasini isteyin.
##Olusturulan parolanin 6dan kisa ya da uzun olmasi durumlarinda gerekli uyarilari yapin. 
##Iki durumun sartlari da saglaniyorsa username ve parolayi hem ekrana printleyin hem de bir dosyaya kaydedin.



isim=input("kullanici adi giriniz:")
uzunluk=len(isim)
mesaj="isim toplam :",uzunluk,"den olusuyor"


if uzunluk <3:
    print("kullanici adi 3 karakterden fazla olmali...")
elif uzunluk >18:
    print("kullanici adi 18 karakterden az olmali...")
else:
    mesaj==uzunluk
    print("sifreniz uygundur...")
sifre=input("parola giriniz:")
uzunluk=len(sifre)
mesaj="sifreniz toplam :",uzunluk,"den olusuyor"
if uzunluk <6:
    print("sifreniz 6 karakterden fazla olmali...")
elif uzunluk >12:
        print("sifreniz 12 karakterden kisa olmali...")
else:
    mesaj==uzunluk
    print("sifreniz uygundur...")

print("Kullanici adiniz:{}, Parolaniz:{}".format(isim,sifre))


dosya=open("KullaniciadiParola.txt","w")
print(isim,sifre,file=dosya)
  
           


