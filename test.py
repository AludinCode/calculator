x = int(input("x değişkeni ne olsun istersiniz"))
y = int(input("y değişkeni ne olsun istersiniz"))
islem = input("hangi işlemi yapmak istersiniz {toplama - çıkarma - çarpma - bölme}")

if (islem == "toplama"):
 toplam = x + y
 print("toplam: ", toplam)

elif (islem == "çıkarma"):
 fark = x - y
 print("fark: ", fark)

elif (islem == "çarpma"):
    carpim = x * y
    print("çarpım :", carpim)

elif (islem == "bölme"):
    bölüm = x / y
    print("bölüm: ", bölüm)