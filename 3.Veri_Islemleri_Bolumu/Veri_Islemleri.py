# klavyeden veri cekme inputtur
a= input("biseyler giriniz ")

b= int(input("biseyler giriniz ")) # int deger alicak sadece 


#print cikti verir

print('a','b','c',sep=',')# sep ayrac olarak kullaniliyor virgulle ayiracak

print("btk"*3) #uc kere yazdiracak

print(10 + 20) #direkt toplama yapti

print("btk\nAkademi")# alt alta yazar
print("btk\tAkademi") #bosluklu yazar
# \ yazdirmak icin iki tane koymak gerekir
A=10
print("A={0}".format(A)) #format direkt a cekip yerine yazar


#printle czim yapma

print(" ___\n/* *\\\n \./")


#printle balik cizilecek


ort=0
y1=int(input("bir sayi girinzi:"))
y2=int(input("bir sayi girinzi:"))

ortlama=(y1+y2)/2

print("ortalaminiz={0}".format(ortlama))


current_date= 2024
dt=int(input("dogum yili girinzi:"))

yas=current_date-dt

print("yasiniz={0} ".format(yas))
