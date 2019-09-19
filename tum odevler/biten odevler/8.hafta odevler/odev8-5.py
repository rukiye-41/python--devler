##Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.print("2 sayının ekok'unu bulan programa hoş geldiniz..")

seçenek=("işlem yapmak için 1'e basınız\nçıkmak için 2'ye basınız\n")
print(seçenek)


def ekok(sayı1,sayı2):
    if (sayı1 > sayı2):
        büyük=sayı1
    else:
        büyük=sayı2
    i=büyük
    while(i<sayı1*sayı2):
        if(i%sayı1==0 and i %sayı2==0):
            return i
        i+=1
    return (sayı1*sayı2)
while True:
    secim=input("seciminiz:")
    if secim=="1":
        sayı1=int(input("1. sayıyı giriniz:"))
        sayı2=int(input("2. sayıyı giriniz:"))
        print("{} ve {} ' nin ekoku = {}".format(sayı1,sayı2,ekok(sayı1,sayı2)))
        continue
    if secim=="2":
        çıkış=input("çıkmak için q'ya basınız:")
        if çıkış =="q":
            print("çıkılıyor..")
            break
    else:
        print("yanlış seçım yaptınız...")
