#listeler birden fazla elamini bir arada ttuan eleman

liste=['ali','can']

print(liste)

liste2="pyhthon "  # bu da bir listedir


print('ali' in liste ) # true false cevabi vericek

# range istenilen aralikta bir liste yad sayi urtemek icin kullaanilir


range(6) #0dan 6 kadar 6 alti dahil degil

range(1,10,2)# 1 den 10 kadar 2ser artsin artim degerini - yazarsak ve 10 1 -2 olarak yazarsan geriye gider

for a in range (0,5):
    print(a)

for i in range(1,30): # 1 den 30 kadar tek sailari alma 
    if (i % 2 ==1):
        print(i)



#-----------------------------------------------------------------------------------------------------------------------------------------------


# while dongusu dongusu sayisi degisibelen belli olmayan bir sat saglandigida donguden cikan dongudur


x=1
print ("cikis icin sifira bas ")

while (x!=0 ):
    x=int(input("sayi giriniz "))
    print("sayi giriniz=", x*x)



while True:
    D=int(inpit("bir sayi giriniz "))
    print("karesi",D*D)
    if (D==0):
        break #break donguyu kiriyor



for A in range(100):
    if (A%7==0):
        continue # devam et kale alma demek stiyor
    print(A)



#---------------------------------------------------------------------------------------------------------
#ic ice donguler
    
for B in range (1,11):
    for b in range (1,11):
        print(B,"X",b,"=",B*b)
    print("\n")





