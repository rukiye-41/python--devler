##odev2-)Kullanıcıdan bir input alınız. Girmiş olduğu inputta büyük harf sayısı,
##küçük harf sayısı, rakam sayısı ve bunların haricindeki
##özel karakter sayılarını veren bir program yazınız.
kucukharf=0
buyukharf=0
sayi=0
karakter=0
metin=input("lutfen bir metin veya kelime giriniz:")
for i in metin:
    if i.islower():
        kucukharf+=1
    elif i.isnumeric():
        sayi+=1
    elif i.isupper():
        buyukharf+=1
    else:
        karakter+=1

print(metin,"degerinde",kucukharf,"tane kucu harf",buyukharf,"tane buyuk harf",sayi,"tane rakam",karakter,"sembol vardir...")
