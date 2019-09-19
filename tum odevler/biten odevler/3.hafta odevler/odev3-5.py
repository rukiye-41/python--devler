##5.ODEV: FIZZ BUZZ
##   1'den 100'e kadar sayilari yazdirin.
##Fakat 3'e tam bolunen sayilarin yerine FIZZ,
##5'e tam bolunen sayilarin yerine BUZZ,
##hem 3'e hem de 5'e tam bolunebilen sayilarin yerine FIZZBUZZ yazsin.



for i in range(1,101):
    if i %3==0 and i%5==0:
        print("FIZZBUZZ")
    elif i%3==0:
        print("FIZZ")
    elif i%5==0:
        print("BUZZ")
    else:   # hic biri degilse sayiyi yazdir
        print(i)
    
    
