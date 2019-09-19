##Kullanıcıdan bir input alan ve bu inputun içindeki büyük
#ve küçük harf sayılarının
#veren bir fonksiyon yazınız.


def büyük_küçük_harf():
    yazı=input("yazı griniz:")
    büyük=0
    küçük=0

    for i in yazı:
        if i.isupper():
            büyük+=1
        elif i.islower():
            küçük+=1

    return büyük,küçük
print("büyük küçük harf",büyük_küçük_harf())
