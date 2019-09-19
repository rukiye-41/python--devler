##Bir sayinin tam bolenlerini bulan fonksiyon yazınız.


def tam_bölensayı(sayı):
    tam_bölen=[]
    sayac=0
    tumu=[]

    if (sayı==0):
        print("sıfırın tam böleni yoktur..")
    if (sayı==1):

        print("birin tam böleni yoktur..")

    else:
        for i in range(2,sayı):
            if (sayı%i==0):
              tam_bölen.append(i)
              sayac+=1
              tumu=[tam_bölen,sayac]

        return tumu
print("bir sayının tam bölenlerini bulma programına hoş geldiniz....")
secenek=("bir sayını tam bölenlerini bukmak için  1'e basınız\nçıkmak için 2'ye basınız\n")
print(secenek)
while True:
    try:

        secim=input("seciminiz:")

        if secim=="1":
            gelensayı=int(input("tam bölen sayı giriniz:"))
            ayır=tam_bölensayı(gelensayı)

            if(gelensayı < 0):
                print("negatif sayı girmeyiniz")

            elif (gelensayı==1):
                print("birin tam böleni kendisidir..")

            else:
                tambölenler=ayır[0]
                print("tam bölen sayılar:{}'dır".format(tambölenler))
                continue

        if secim=="2":
            çıkıs=(input("çıkmak için q'ya basınız.."))

            if çıkıs=="q":
                print("çıkılıyor...")
                break
        else:
            print("yanlış seçim tekrar seciniz..")


    except ValueError:
        print("tekrar..")
tam_bölensayı
