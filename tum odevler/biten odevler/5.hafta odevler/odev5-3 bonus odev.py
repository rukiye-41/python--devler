###*BONUS ODEV:*
### İki liste tanımlayın.
##  # İlk liste 1'den 10'a kadar sayılardan oluşturun.
##  # İkinci listeyi sırasıyla a'dan başlayarak 10 harf ile oluşturun.
##  # İki liste için de döngü kurup, iki listenin elemanlarının bütün kombinasyonlarından oluşan iki yeni liste oluşturun.
##​
##  # 3'er elemanli versiyonunda cıktı olarak bu şekilde bir çıktı beklenmektedir:
##​
##  # 1. [1a, 1b, 1c, 2a, 2b, 2c, 3a, 3b, 3c]
##  # 2. [a1, a2, a3, b1, b2, b3, c1, c2, c3]


sayilar=["1","2","3","4","5","6","7","8","9","10"]   
harfler=['a','b','c',"d","e","f","g","h","i","j"]   
yeni_liste=[sayı+harf for sayı in sayilar for harf in harfler]
yeni_liste1=[harf+sayı for harf in harfler for sayı in sayilar]
print("yeni_liste",yeni_liste)
print("yeni_liste1",yeni_liste1)
