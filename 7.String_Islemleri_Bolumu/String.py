# '5' int degir string olarak aliyoruz

k='a'
l='b'


print(type(k)) # tipini goruyouz


#index sayisal elektronikte yada binarydei gibi sayma olayi 0 dan basliyoruz ilk karakter aslinda 0. index oluyor

x='B'
y='T'
z='K'

print(x+y+z)# string topladik

s='python'

s[3:]# dilimleme 3. indexten baslayip sonuna kadar alicak hon ciktisini vermeli
s[:3] # bu da basi alacak
s[1:5] # 1 den baslayip 5 kadar alicak
s[1::5] # 1 den basla sonu onemli degil 2 ser artarak bol
s[::-1] # tersten alicak

Adres='python'
Adres=Adres.replace("python","python1")# stringi degistirdik


yazi='python'
a=''
s=0
for d in 'btk akademi':
    
    if s==7:
        s+=1
        a==d

print(a)


#adres.split() bosluklardan boluyor arguman giresek ona gore boluyor


#len(cumle) diziyi listeyi kac karekterli oldugu soz=yluyor

#cumle.count('a') a yi sayiyor bu da

# iki string ifadeyi karslilastimrak icin

'talat' == 'talat'



#format indexlerin arasina yazdirmak icin kullaniyoruz

String='Ali{}Veli'
A='sevici'
String.format(A)

#reversed ters ceviriyor
#join(reversed())
String.lower() #kucultuyor
String.upper()# buyultuyor

String.swapcase()# ilkini kucuk ikincini buyuk yapiyor


'at' in 'Talat ' #true vericek

