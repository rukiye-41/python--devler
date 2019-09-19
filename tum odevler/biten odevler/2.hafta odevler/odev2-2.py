##2.ODEV: UZAKLIK BIRIMI DONUSUMU
##    Kullanicadan 2 input alinacak:
##        1-km-mil donusumu mu yapmak istiyor, mil-km donusumu mu yapmak istiyor.
##        2-donusturmek istedigi birimin uzunlugu kactir?
##    Donusum yapilacak birimler mil ve kilometre olacak.



print("km'yi mile donusturmek icin 1'e basiniz\n mil'i km'ye donusturmek icin 2'ye basiniz:")

secim=int(input("seciminiz:"))

if secim ==1:
    km=float(input("kilometreyi mile cevir:"))
    a=0.62
    mil=km*a
    print(km,"km", mil, "mil'dir...")

elif secim ==2:
    mil=float(input("mili kilometreye cevir:"))
    a=0.62
    km=mil/a
    print(mil,"mil",  km, "kilometre'dir...")

elif secim ==3:
    print("cikiliyor...")

else:
    print("yanlis secim...")




    
