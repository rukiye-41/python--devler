##ODEV 2: Verilen bir sayi listesinin elemanlarindan
##tek olanlari ikiyle carpan ve
##hepsini toplayip sonucu veren bir fonksiyon yaziniz.
##Map, filter ve reduce kullaniniz.


from functools import reduce

liste=list(range(20))

cevap= reduce(lambda a,b:a+b,map(lambda a:a*2,(filter(lambda a:a%2!=0,liste))))

print("listedeki tek  sayilarin iki ile carpilip toplam sunucu {} sayisidir..".format(cevap))


