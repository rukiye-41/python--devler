##2
##Kullanıcıdan input ile km cinsinden mesafe bilgisi alıp, bu bilgiyi mile dönüştürün ve sonucu ekrana printleyin.
## 1 km = 0,621371192 mil

km=int(input("gidilen mesafeyi km cinsinden giriniz:"))
#1 km=0.62137119223733 mil eder
a=0.62137119223733
mil=km*a
print(km," kilometrenin   mili:",mil,"dir")
