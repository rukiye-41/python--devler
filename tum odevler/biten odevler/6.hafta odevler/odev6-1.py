#ODEV 1: Sayi Tahmin
#-Kullanicidan aklindan 0-100 araliginda bir sayi tutmasini isteyin.
#-Yazdiginiz kod ile bu sayiyi tahmin etmeye calisin.
##-Tahmin sonucunda, kullanicidan alacaginiz input, pc'nin tahmin ettigi sayi kullanicinin belirledigi 
#sayidan buyukse kullanici daha dusuk sayi tahmin etmelisin manasinda "-" seklinde olsun, pc'nin tahmin 
#ettigi sayi kullanicinin belirledigi sayidan kucukse "+" seklinde olsun.
#-Pc'nin tahmini dogru oldugunda da kullanicidan bunu belirtebilecegi bir input isteyin.
#-Gelistireceginiz algoritma sayesinde kullanicinin belirledigi sayiyi en az hamlede bilmeye calisin :)
#
#Ornek:
#
#Kullanicinin aklindan tuttugu sayi: 56 (kullanicidan bunun icin bir input almayacagiz sadece 
#aklinizdan bir sayi belirlemis iseniz oyunumuza baslayabiliriz seklinde bir input alabiliriz. 
#Yani belirledigi sayiyi sisteme girmesini istemiyoruz.)
#
#Pc'nin tahmini = 89
#Kullanicinin inputu = -
#Pc'nin tahmini = 45
#Kullanicinin inputu = +
#Pc'nin tahmini = 56
#Kullanicinin inputu = "Enter"
#
import random
print("0-100 arasında bir sayi tutunuz.")
input("Oyunumuza enter'a basarak baslayabiliriz...")
tahmin=random.randint(0,100)
hak=0
üstsınır=100
altsınır=0
while True:
    hak+=1
    print("pc tahmini:  ",tahmin)
    kontrol=input("kullanıcı onayı:  ")
    tahmin=random.randint(0,100)
    if kontrol=="-":     ###büyük oldu
        üstsınır+=(tahmin)
    if kontrol=="+":    ##küçük oldu
        altsınır+=(tahmin)
    if kontrol=="enter":
        print(hak,"tahminde bildim..")
        break
