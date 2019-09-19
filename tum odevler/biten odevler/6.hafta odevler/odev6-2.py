##ODEV 2: XOX Oyunu
##
##		Kitapta yer alan XOX oyunu iki kisinin karsilikli oynayabilecegi sekilde duzenlenmis. Sizden bu oyunu 
##
##		kullanicinin bilgisayara karsi oynayabilecegi versiyonunu yapmanizi istiyoruz. Ayrica gelistireceginiz 
##
##		algoritma sayesinde bilgisayarin tamamen rastgele hamleler yapmasindan ziyade mantikli hamleler yapmasini 
##
##		saglamanizi istiyoruz. Ornegin bilgisayarin "O" hamlesini yaptigini varsayalim: 
##
##					X O _  
##
##					_ X _   
##
##					_ _ _
##
##
##		seklinde olusan bir durumda hamle sirasi bilgisayarda ve bilgisayar kaybetmemek icin sag-alt koseye "O" 
##
##		koymalidir.
##
##
##
##
##
##		Farkli bir ihtimal:
##
##					O X X 
##
##					O _ X 
##
##					_ _ _ 
##
##
##
##		boyle bir durumda da hamle sirasi bilgisayarda ve bilgisayar kazanma hamlesi olarak sol-alt koseye "O" koyarak 
##
##		oyunu bitirmelidir.
##
import random

print("X-O-X oyununa hosgeldiniz...")


tablo=[["__","__","__",],
       ["__","__","__",],
       ["__","__","__"]]

##for i in tablo:
##  print("\t".expandtabs(30), *i, end="\n"*2)
##  
ayir=0
print("  0  1  2")
for i in tablo:
    print(str(ayir)+" "+" ".join(i))
    ayir+=1

tablo2=[[[0,0],[1,0],[2,0]],
        [[0,1],[1,1],[2,1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]]]


x_durumu = []
o_durumu = []
sira=1
while True:
    if sira%2==0:
        print("bilgisayarda sira")
        simge="x".center(3)
        a=str(random.randint(0,2)).ljust(30)
        b=str(random.randint(0,2)).ljust(30)
    else:
        print("kullanici sirasi")
        simge="o".center(3)
        a=input("1-3 arasinda bir satir giriniz:".ljust(30))
        b=input("1-3 arasinda bir sutun giriniz:".ljust(30))
    print("simge:",simge,"\n")

    if a =="q":
        break
    if b == "q":
        break

    a=int(a)
    b=int(b)
##    print("a alindi {} b alindi {}".format(a,b))

    if tablo [a][b]== "__":
##        print("a eklendi",a,"b eklendi",b)
        tablo[a][b]=simge

        if simge =="x".center(3):
            x_durumu+=[[a,b]]
##            print(" x in durumu : {}".format(x_durumu))
        elif simge == "o".center(3):
            o_durumu+=[[a,b]]
##            print(" o nun durumu :{}".format(o_durumu))
        sira+=1
    else:
        print("orasi dolu bos yer seciniz...")

##    for i in tablo:
##      print("\t".expandtabs(30), *i, end="\n"*2)
##    
    ayir=0
    print("  0  1  2")
    for i in tablo:
        print(str(ayir)+" "+" ".join(i))
        ayir+=1
    for i in tablo2:
        o=[ j for j in i if j in o_durumu]
        x=[ j for j in i if j in x_durumu]
        if len(o)==len(i):
            print("siz kazandiniz...")
            quit()
        if len(x)==len(i):
            print("bilgisayar kazandi....")
            quit()

        if len(o_durumu)==4 and len(x_durumu)==5:   
          print("BERABERE KALDIK...")
          quit()
    








