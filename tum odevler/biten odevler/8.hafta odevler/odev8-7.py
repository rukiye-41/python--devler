#1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)

def pisagor(sayı):
    for a in range(sayı):
         for b in range(1,a):
                c=(a*a+b*b)**0.5
                if c%1==0:
                    print(a,b,int(c))
pisagor(100)
