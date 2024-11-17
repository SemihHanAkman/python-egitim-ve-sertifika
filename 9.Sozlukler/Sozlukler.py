#Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
Mevsim={'kisi':1,'ilkbahar':2,'yaz':3,'sonbahar':4}
#dictinoty
TC=dict([('talat',1234),('ali',12345),('hasan',1236)])#dictonary
s={}
s[1]='bir'
s[2]='iki'
s[3]='uc'
print (s)


s={'bir':1,'iki':2,'uc':3,'dort':4}

s.get('bir',"yok")
1
s.get('uc',"yok")
3
s.get('yedi',"yok")
'yok'
s.pop('uc')

s.keys()

s.values()

s.items()

gun=input("turkce gun adi....")
Tren={'pazartesi':'monday','sali':'tuesaday','carsamba':'wednesday','persembe':'thuesdau','cuma':'friday','cumartesi':'saturday','pazar':'sunday'}
print(Tren.get(gun,'Bu kelime sozlukte yok '))

K={1,'hg','*',325}\

K=set('agstcj743f')

K
type(K)

#bunlar mantiktaki kumlerle ayni kesisim kumesi nbirlesim kumesi gibi kulelerel oynuyoruz

#K1-K2 k1 de olan k2 olamaynlar vs

L=[1,'ata',325,'*']

T=(1,'ata',325,'*') #tuple degistiilemez asagida onu tastikledik

L[0]=23

#T(0)=23  hata vericek









