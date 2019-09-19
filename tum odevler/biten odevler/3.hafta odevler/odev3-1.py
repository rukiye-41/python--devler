##1.ODEV: HESAP OLUSTURMA
##Kullanicidan, kullanici adi ve parola olusturarak hesap olusturmasini isteyin.
##Bu aldiginiz bilgileri bir dosyaya yazdirin.
#Her gırıste dosyadakı bılgıler sıfırlanmasın kayıt bılgılerı dosyaya eklenmeye devam etsın.
#Kullanici daha once girilmis olan bir kullanici adiyla hesap olusturmak isterse,
##bu kullanici adinin daha once secildigini ve baska bir kullanici adiyla hesap olusturmasini isteyin.

print("\t HesapOlustur \n")
print("hesap olusturmak icin 1'e basiniz cikmak icin 2'e basiniz:")
secim=input("seciminiz:")


if secim =="1":
    while True:
        kullanici_adi=input("lutfen kullanici adi olusturunuz: ")
        parola=input("lutfen bir parola olusturunuz:  ")

        file=open("hesapolusturma.txt","r+")
        veri=file.read()
        if kullanici_adi in veri:
            print("bu kullanici adi zaten alinmis")

        else:
            file=open("hesapolusturma.txt","a")
            veri=kullanici_adi+"\n"+parola
            file.write(veri)
            file.close()
            print("hesap olusturuldu..")
            break

elif secim =="2":
    print("program kapatiliyor...")

else:
    print("yanlis bir islem yaptiniz...")


