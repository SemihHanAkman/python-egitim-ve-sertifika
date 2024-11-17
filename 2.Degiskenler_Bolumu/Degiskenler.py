#degiskenler: bilgisayar bilimnde niceligin depolanabildigi bir yer alan ifade eder

a = 100 # bu bir degisken
b = 200
toplam = a+b 
print(toplam)


# degiskenlere isim verirken kurallar vardir

ali_akman = 16

#bosluk olamaz srou isareti olmaz python komutu olamaz nokta ile baslayamaz ama altan cizgi ile baslayabilir

# turkce karakter kullanilmamalidir

#kucuk buyuk harf onemi vardi dosya hata vermsin diye ornekleri yazmiyorum


A=3
B=4
C=A
print(C)

A,B = B,A #boylede degisir degiskenler
print(B)
print(A)

#aynisini string degerler icin de yapabiliyoruz


#oparetorler (+ - * /)bildigimiz 4 islem  %> kalan  **> us alma //> tam sayi bolme


sayi1= int(input("bir sayi giriniz"))
sayi2= int(input("bir sayi giriniz"))
Toplam = sayi1 + sayi2
print(sayi1,'+',sayi2,'=',Toplam)


#pythonda islem onceligi

#parentez ici> us alma> carpma> bolme> mod(%)> toplama> cikarma

denem_1=2+3**2

cep=0
cep=cep+10
print(cep)

cep+=10
print(cep)# += cep=cep+10 bunun yaptigi isi yapan operator -= /= ayni durum bunlardada var

# A= A+B > A+=B  x= x - y/2 > x-m y/2

# int tamsayi                                 10
#float ondalikli veri tipi                    3.14
#bool 1 0 veri tipi ikilik sistem             true false 
#str string yani karakter veri tipi           'semih '

d=type(sayi1)#hangi veri tipi  oldugunu gosterecek
print(d)


# = atama opertorudur == esitlik operatorudur

#veri tipi donsumleri int 9.6 dersek 9 alicak float 5 dersek 5.0 alicak

str_degisken=str(4)

print(str_degisken+str_degisken)# str 4 dedigimiz 8 ciktisini vermedi bunu yerine 44 verdi cunku 4 bir tamsayi degil burda bir karakter buyuzden iki tane 4 karakterini yanyana getirdi
