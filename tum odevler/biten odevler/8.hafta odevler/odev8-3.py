#1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın.
#Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
#Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.
#Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).
print("mükemmel sayı bulma programına hoş geldiniz....")
secenek=("mükemmel sayıyı bulmak için  1'e basınız\nçıkmak için 2'ye basınız\n")
print(secenek)

def mükemmelsayı(sayı):
    toplam=0
    for i in range(1,sayı):
        if sayı%i==0 :
            toplam+=i

    if (sayı > 1000):
        print("1000 'den büyük sayı girmeyınız...")

    if toplam==sayı:
        print(sayı,"mükemmel sayıdır..")
    else:
        print(sayı,"mükemmelsayı değildir..")

while True:
        secim=input("seciminiz:")

        if secim=="1":
            sayı=int(input("sayı giriniz:"))
        mükemmelsayı(sayı)
        continue

        if secim=="2":
            çıkış=input("çıkmak için q'ya basınız..")
            if çıkış=="q":
                print("çıkılıyor..")
                break

        else:
            print("yanlış secim yaptınız..")
