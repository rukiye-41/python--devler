##Verilen bir listenin içindeki özgün elemanları ayırıp
##yeni bir liste olarak veren bir fonksiyon yazınız.
##Örnek Liste : [1,2,3,3,3,3,4,5,5] Özgün Liste : [1, 2, 3, 4, 5]

def coklu_sayılar(sayılar):
    liste=[]
    for i in sayılar:
        if i not in liste:
            liste.append(i)
    return liste
liste1=[1,2,2,5,5,6,8,8,10,10,23,23]
print(coklu_sayılar(liste1))
