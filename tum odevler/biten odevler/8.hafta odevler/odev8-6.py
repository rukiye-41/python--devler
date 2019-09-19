##Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın. Örnek: 97 ---------> Doksan Yedi

def sayılar():
    birler = {"0":"","1":"Bir","2":"Iki","3":"Uc","4":"Dort","5":"Bes","6":"Alti","7":"Yedi","8":"Sekiz","9":"Dokuz"}
    onlar = {"1":"On","2":"Yirmi","3":"Otuz","4":"Kirk","5":"Elli","6":"Altmis","7":"Yetmis","8":"Seksen","9":"Doksan"}


    sayı  = input("Sayiyi Giriniz :")

    if len(sayı)==1:
        sayı=birler[sayı[0]]
        return sayı

    if len (sayı)==2:
        sayı=onlar[sayı[0]]+birler[sayı[1]]
        return sayı
    continue






print(sayılar())
