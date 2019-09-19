##4-
##Faiz hesaplama programi
##
##Icerik:
##Kullanicidan gerekli bilgileri alip faiz tutarini hesaplayin.
##
##Yontem:
##Bu programi calistirabilmeniz icin asagida belirtilen bilgileri input yardimi ile kullanicidan almaniz gerekmektedir. 
##    ⁃    Ana para
##    ⁃    Faiz suresi (yil)
##    ⁃    Faiz orani
##
##Faiz hesaplama formulu:
##Ana para x faiz suresi x faiz orani / 100
##
##Sonuc:
##Gerekli islemleri yaptiktan sonra output olarak toplam faiz tutarini, aylik ve gunluk ortalama faiz tutarini, toplam para miktarini (faiz+ana para);
## 1) print ile ekrana yazin,
## 2) ”faizHesaplama” isimli bir dosyaya

ana_para=float(input("ana para miktarinizi giriniz:  "))
faiz_suresi=float(input("faiz suresini yil olarak giriniz:  "))
faiz_orani=float(input("faiz oranini giriniz:  "))

faiz=(ana_para*faiz_suresi*faiz_orani)/100
print("yillik ",faiz,"faiz miktaridir...")

aylik_faiz=faiz/(faiz_suresi*12)
print("aylik",aylik_faiz,"faiz miktaridir..")

gunluk_faiz=faiz/(faiz_suresi*366)
print("gunluk",gunluk_faiz,"faiz miktaridir..")

dosya=open("Faiz Hesaplama.txt","w")
print("yillik" ,faiz, "aylik",aylik_faiz, "gunluk",gunluk_faiz,sep="",file=dosya)
dosya.close()
