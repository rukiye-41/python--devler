##1.ODEV: BURCUN NE?
##    Kullanicidan dogum gununu ve ayini isteyin,
##program hangi burc oldugunu soylesin.

gun=int(input("dogdugunuz gunu giriniz:"))
ay=input("dogdugunuz ayi giriniz:")


if (gun >21) and (ay=="mart") or (gun<20) and (ay=="nisan"):
    burc="koc"

elif (gun>21) and (ay=="nisan") or (gun<20) and (ay=="mayis"):
    burc="boga"

elif (gun>22) and (ay=="mayis") or (gun<20) and (ay=="haziran"):
    burc="ikizler"

elif (gun>23) and (ay=="haziran") or (gun<21) and (ay=="temmuz"):
    burc="yengec"

elif (gun>23) and (ay=="temmuz") or (gun<22) and (ay=="agustos"):
    burc="aslan"

elif (gun>23) and (ay=="agustos") or (gun<22) and (ay=="eylul"):
    burc="basak"

elif (gun>24) and (ay=="eylul") or (gun<22) and (ay=="ekim"):
    burc="terazi"

elif (gun>23) and (ay=="ekim") or (gun<23) and (ay=="kasim"):
    burc="akrep"

elif (gun>22) and (ay=="kasim") or (gun<22) and (ay=="aralik"):
    burc="yay"

elif (gun>21) and (ay=="aralik") or (gun<21) and (ay=="ocak"):
    burc="oglak"

elif (gun>19) and (ay=="ocak") or (gun<20) and (ay=="subat"):
    burc="kova"

else:
    burc="balik"

print(gun,ay,"burcunuz:",burc)   



