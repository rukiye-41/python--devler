##Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

print("2 sayının ebob'unu bulan programa hoş geldiniz..")
seçenek=("işlem yapmak için 1'e basınız\nçıkmak için 2'ye basınız\n")
print(seçenek)

def ebob(sayı1,sayı2):
    if(sayı1 > sayı2):
        küçük=sayı2
    else:
        küçük=sayı1
    i=küçük

    while(i >0):
        if(sayı1%i==0 and sayı2%i==0):
            return i
        i-=1

while True:
    secim=input("seciminiz:")
    if secim=="1":
        sayı1=int(input("1. sayıyı giriniz:"))
        sayı2=int(input("2. sayıyı giriniz:"))
        print("{} ve{}'nin ebobu={}".format(sayı1,sayı2,ebob(sayı1,sayı2)))
        continue
    if secim=="2":
        çıkış=input("çıkmak için q'ya basınız..")
        if çıkış=="q":
            print("çıkılıyor..")
            break
    else:
        print("yanlış secim yaptınız...")
