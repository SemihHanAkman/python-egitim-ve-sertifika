import datetime
class Araba():#kendimemze veri tipi olustuyoruz 
     def __init__(self,model,marka,renk):#metot 
        self.model=model
        self.marka=marka
        self.renk=renk
     def aracBilgisi(self):
         print("markasi:",self.marka)
         print("model:",self.model)
         print("renk:",self.renk)
   
     
def a():
    pass
class araba:
    pass
#self # sinifin cicndeki elemalar icin kullanilir
class hayvan():
    tur=cins
    def metot(self):# burya init geliyor
        self.cins="baliklar"
#At=hayvan()
#horoz=hayvan()
#Taksi=Araba()
#kamyon=Araba()
Taksi=Araba(2020,"Fiat","Yesil")
print(Taksi.model)#modeli veriyor
Taksi.aracBilgisi()

Kamyon=Araba(2010,"BMC","Kirmizi")



class araba():#ust sinif
     def __init__(self,model,fiyat):#metot 
        self.model=model
        self.fiyat=fiyat
     def aracBilgisi(self):
         print("fiyat:",self.fiyat)
         print("model:",self.model)
         return(datetime.datetime.now())
class kamyon(araba):#altsinif
    def __init__(self,model,fiyat,renk):#metot
        araba.__init__(self,model,fiyat)
        self.model=model
        self.fiyat=fiyat
    
k1=kamyon(2020,120000,"kirmizi")
print(k1.model)
print(k1.fiyat)
print(k1.renk)


#__name__=='__main__' ana programmi diye bakiyoruz
#import ederkekn kullaniyoruz
#kalitim miras ozellikleri var alt siniflar verekerk yapiyoruz baska siniflerdaki metotolari fonsiyonlari baska islerde kullanabiliriyoruz


    

