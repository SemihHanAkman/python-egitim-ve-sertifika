liste=['ali',5,'a','ali','5','a'] # bu  gosterim listedir
liste[2]# a yi vermeli
liste.index(5) # besinci indexte ne var diye sorgulatiyor
liste.index('5')#  5 kacinca indexte
# srtingde yapilan islmeler burdada var
# listeye eleman ekleme
liste.append(7) # yedi eklendi
liste.insert(2,9)# ikinci indexse 9 koydu

len(liste)#listenin uzunlugunu gosteriyor
liste.count(5)# 5 ten ne kadar var oldugunu gosteriyor

#listeler=liste+liste1 listeler birlesti
#liste.extend(liste1) liste1 i listeye ekledik


#liste ters cevirme
Liste1=liste.reverse()


#max(liste) min(liste) en kucuk ve enbuyuk sayilari bulabilirz

#string listeye cevirsdik
kelime='BTKAKADEMI'
L=[]
L=list(kelime)
L.remove('A')# Ayi sildik
L.pop(2)# 2.indexsi sildi
L.clear()# kopmle sildi

1 in L # varsa true diyecek

L.sort# kucukten buyuge siraladik

Gun=['pazartesi','sali','carsamba','persembe','cuma','cumartesi','pazar']
for i, deger  in enumerate(Gun):
    print(str(i+1)+".gun "+deger)


