###Kullanıcıdan tire(-) ile ayrılan bir input dizisi alan
##ve sonrasında bu kelimeleri harf sırasına göre dizip tekrar tire ile ayırıp
##output olarak veren bir fonksiyon yazınız.
##örnek girdi: green-red-yellow-black-white örnek çıktı: black-green-red-white-yellow



def alfabetik_sıra():
    yazı=input("bir yazı yazınız:")
    kelimeler=yazı.split()  ##bu kod ile kelimeleri parçalıyoruz..
    kelimeler.sort()
    print("alfabe sırasına göre sıralanan kelimeler:",sep="-")
    for sırala in kelimeler:
        print(sırala,sep="-")
    return kelimeler
alfabetik_sıra()
