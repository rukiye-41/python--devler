##odev5-)Futbolcular dosyasındaki futbolcu isimlerini yazdığınız
##program ile Türkçe karakter içermeyecek bir hale getirip
##yeni bir dosyaya kaydediniz.


with open("futbolcular.txt") as file:  # dosyayi actik
  futbolcular=file.read()  #dosya degerlerini strıng seklınde degıskene attık
  
kaynak="şçöğüiŞÇÖĞÜİ"
hedef="scoguiSCOGUI"
tablo=str.maketrans(kaynak,hedef)  # ceviri tablosu olusturduk str.maketrans metodu ile

with open("futbolcularyeni.txt","w") as file:  # dosyayi actik
  file.write(futbolcular.translate(tablo)) #cevirdigimiz stringi yeni dosyaya kaydettik 

