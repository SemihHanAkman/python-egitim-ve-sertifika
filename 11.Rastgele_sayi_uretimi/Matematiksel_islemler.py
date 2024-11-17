import math
import random

abs(-3)
#3 cikti vericek
round(12.3)
#cikti12 vericek yuvarlayacak
max(121212,232332424)
#en buyuk degeri vericek
min(12121,2312313)
#en kucuk degeri vericek
pow(2,3)
#cikti 8 vericek ussunu aliyor
bin(54)
#binary ceviyor
hex(1312)
#hexedecimale ceviriyor
chr(65)
#ascii ceviriyor

#sum(1,32)
#toplayacak
#div()
#sub()

math.sqrt(13)#karekoku aliyor


r=int(input("yaricapi gir...."))
Hacim = (4/3)*math.pi*pow(r,3)
Alan= 4*math.pi*pow(r,2)
print("Kurenin Hacmi..:",Hacim,"m^3")
print("Kurenin yuzey alani...:",Alan,"m^2")

random.random() # random sayi uretiyoruz

random.randint(2,9) # 2 ile 9 arasinda random sayi ureticek

random.randrange(1,13,2) # 1 ile 13 arasinda 2 ser atlayacak

random.uniform(10,11) # 10 11 arasi sayilari uretecek


sayi=random.randint(1,6)
tahmin=int(input("Tahmin et ....."))
skor=5
while sayi!=tahmin:
    if sayi==tahmin:
        print("Kazandiniz",skor)
        break
    else:
        print("olmadi",skor)
        skor-=1
        tahmin=int(input("tahminet "))

Liste = ["Tas","Kagir","Makas"]
pc= random.choice(liste)
player= input('[Tas-Kagir-Makas]')
print("Bu bilgisyar",pc,"secti")
print("ouncu",player,"secti")

if pc==player:
    print("Berabere")
if pc=="Kagit" and player=="Tas":
    print("Kaybettin")
if pc=="Tas" and player=="Makas":
    print("Kaybettin")
if pc=="Kagit" and player=="Tas":
    print("Kaybettin")


