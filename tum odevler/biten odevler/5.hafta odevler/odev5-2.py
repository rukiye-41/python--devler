##*ODEV 2:SAYI TAHMIN OYUNU:*
## Kendiniz 4 basamakli, rakamlari birbirinden farkli ve icerisinde 0 rakaminin yer almadigi bir sayi belirleyin. 
# Kullanicidan bu sayiyi tahmin etmesini isteyin. Yapilan tahmin sonucu kullanicinin, 
# tahminde bulundugu sayidaki rakamlarin degeri ve yeri dogruysa +1, degeri dogru fakat yeri dogru degilse -1 ciktisi verecegiz. 
# Bu sekilde tahminde bulunmaya devam etmesi saglanacak ve 
# sayiyi tam bir sekilde dogru bildiginde gerekli bilgilendirme yapilip oyun bitirilecek.
##
##  Ornek:           sayi = 1234
##
##         yapilan tahmin = 9831
##
##         (Burada "9" ve "8" rakamlari yanlis oldugu icin ciktiya bir etkisi yok. "3" rakaminin yeri dogru oldugu icin +1, "1" rakami sayi icerisinde yer alan fakat yeri yanlis oldugu icin -1 ciktisi verecegiz.)
##
##         ornek output = +1 -1
##
##         yapilan tahmin = 2134
##
##         ("2" ve "1" rakamlari sayi icerisinde yer aldigi fakat yerlerinin yanlis olmasi nedeniyle ikisi icin -1, "3" ve "4" rakamlarinin yerleri de dogru oldugu icin +1 degerleri donecegiz.)
##
##         ornek output = +2 -2
##
##         yapilan tahmin = 9876
##
##         ornek output = +0 -0
##
##         yapilan tahmin = 2146
##
##         ornek output = +0 -3

print("\t***sayi tahmin oyunu***")
print("""Dort basamakli bir sayiyi bulmaya calisiyorsunuz.
Siz bana bi tahminde bulundugunuzda:
 yeri dogru olan rakam icin +
 yeri yanlis rakam icin - 
sayi verecegim.Eger tahminindeki rakamlar sayimla uyusmuyorsa herhangi bir sayi soylemem.
Her rakam sadece bir kere kullanilacak unutma!!
""")

    
sayi=[1,2,3,4]
sayi_degeri=0
sayi_yeri=0
while True:
    tahmin = input("4 basamakli rakamlari farkli bir sayi tahmin ediniz:")
    tahmin = list(tahmin)
    sayi_degeri=0
    sayi_yeri=0
    for i in range(4):
        if sayi[i]==int(tahmin[i]):
            sayi_yeri+=1
    if sayi==[int(i) for i in tahmin]:
         print("{} sayisini dogru tahmin ettiniz.".format(sayi))
         break
    for i in tahmin:
        if int(i) in sayi:
            sayi_degeri+=1
    print("+", rakam_yeri,"-" ,sayi_degeri-sayi_yeri)
    print("Toplam {} adet rakam sayida mecut , {} rakamin yeri dogru:".format(sayi_degeri,sayi_yeri))





