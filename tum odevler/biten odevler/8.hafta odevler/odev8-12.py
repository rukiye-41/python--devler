##Verilen inputların tersten de aynı olup olmadığını
##kontrol eden bir fonksiyon yazınız.
##örnek: madam, taco cat, utrecht sonuç: True, True, False



def ters_duz():
    yazı=input("kelime giriniz:")
    for i in reversed(yazı):
        print(*reversed(yazı),sep="-")
        return yazı
ters_duz()
