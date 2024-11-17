# print range input bunlar fonksiyonlar am pyhton kendisinde var bizim kendi fonksiyonlarimizi yazamaliyiz

def topla():
    print("toplama islemi ")
    print("ornegin",5,"+",7,"=",13)

topla()


def selamlama(isim):
    print("sayin",isim,"restorana hosgeldin ")
while True:
    Ad=input("Isminiz nedir ?")
    if(Ad=="dur"):
        break
    selamlama(Ad)


def alan (u,g):
    A=u*g
    return A
def cevre(u,g):
    C=2*(u+g)
    return C

u=int(input("dikdortgenin uzun kenari"))
g=int(input("genislik"))
print("dikdoetgenin alani",alan(u,g))
print("dikdortgenin cevresi",cevre(u,g))


#global bir fonksiyondaki degeri baska bir fonkisyonda yada yerde ulasmak istiyorsak global yapmamiz lazim


def toplama():
    global a
    global b
    
    print("toplama islemi ")
    print("ornegin",5,"+",7,"=",13)

toplama()



def carpma(): # icini bisey yazmadan gecmek isitoyrsak hata almayiz sonra donup kodumuzu yazabiliriz
    pass
def bolme():
    pass


dolar=lambda Tl: Tl/40 # boyle kisa isleri lambda fonksiyonu ile yapabiliriz ekstra def yazmamiza gerek yok
TL= int(input("kac tl ise onu giriniz "))
print(Tl,"lira",dolar,"dolar eder ")












