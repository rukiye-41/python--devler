##Pozitif bir tamsayının faktöriyelini alan bir fonksiyon yazınız.

print("bir sayının faktoriyelini bulma programı..")
secenek=("hesaop yapmak için 1'e basınız\nçıkmak için 2'ye basınız:")
print(secenek)



def faktoriyel(sayı):
    çarpım=1
    for i in range(1,sayı+1):
        çarpım*=i
        print("faktoriyel:",çarpım)
    return çarpım



while True:
    secim=input("seçiminiz:")
    if secim=="1":
        sayı=int(input("faktoriyelini bulmak icin bir sayi giriniz:"))
    faktoriyel(sayı)
    continue
    if secim=="2":
        çıkış=input("çıkmak içinq'ya basınız:")
        if çıkış=="q":
            print("çıkılıyor..")
            break
    else:
        print("yanlış secim yaptınız..")
