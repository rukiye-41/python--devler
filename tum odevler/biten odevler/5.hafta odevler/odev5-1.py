
adam1="""
   +---+
   |   |
   O   |
       |
       |
       |
========="""

adam2="""
   +---+
   |   |
   O   |
   |   |
       |
       |
========="""

adam3="""
   +---+
   |   |
   O   |
  /|   |
       |
       |
========="""

adam4="""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
========="""


adam5="""
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
========="""


adam6="""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
========="""
adam=[adam1,adam2,adam3,adam4,adam5,adam6]

bulunacakKelime='php'
harfHavuzu = []
kalanHak   = 6
k=["_","_","_"]


dongu = 1

while dongu:
    print(' '.join(k),end='\n\n')
    alinanHarf = input('Bir harf giriniz: ')

    try:
        int(alinanHarf)
        print('Doğru bir şeyler girdiğinden emin ol.\n')
    except:
        if len(alinanHarf) > 1:
            print('Harf giriniz!\n')
        else:
            if alinanHarf in harfHavuzu:
                print('Bu harfi zaten girdiniz.\n')
            else:
                bulduk = None
                for i in range(len(bulunacakKelime)):
                    if alinanHarf == bulunacakKelime[i]:
                            bulduk = True
                            k[i] = alinanHarf
                            harfHavuzu.append(alinanHarf)

                            if alinanHarf not in k:
                                print(' '.join(k))
                                print('\nTebrikler kelimeyi buldunuz!')
                else:
                    if bulduk != True:
                        kalanHak -= 1
                        harfHavuzu.append(alinanHarf)
                    print('Yanlış harf. {}\n  Kalan hakkınız:{}\n'.format(adam[0],kalanHak))
                   
                    
                
                if kalanHak == 0:
                    print('Kaybettin. Doğru kelime "{}" idi.\n'.format(bulunacakKelime))
                    break





                        
    
