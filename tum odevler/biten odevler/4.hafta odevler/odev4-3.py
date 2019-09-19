##3-)Kullanıcıdan bir input alınız.
##Girmiş olduğu inputtaki rakamların toplamını veren bir program yazınız.
##(Kullanıcı rakam girmek zorunda değil.
##farklı karakter girişi de yapabilir.)
##Örnek input = "art12kl4*"

metin=input("rakamli bir metin yaziniz:")
toplam=0
for i in metin:
    if i.isnumeric():
        toplam+=int(i)
    
print("metindeki sayilatin toplami :",toplam)
