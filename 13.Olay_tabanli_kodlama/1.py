import turtle
import time
import random

# Genel ayarlar
Liste = []
skor = 0
maxSkor = 0
#pensize(3)
#win=Screen()
#win.setup(700,700)

#def nokta(x,y):
 #   goto(x,y)

#win.onclick(nokta)#tiklama oldugunda fonksiyonu calistiri
#mainloop()



"""
shape("turtle")
pensize(3)
win=Screen()
win.setup(700,700)

def solaDon():
    left(90)
    write("soladon")
def sagaDon():
    right(90)
    write("sagadon")

def ileri():
    forward(10)
def geri():
    backward(10)

win.onkeypress(solaDon,'Left')
win.onkeypress(sagaDon,'Right')
win.onkeypress(ileri,'Up')
win.onkeypress(geri,'Down')

win.listen()# benim tuslari bamami bekleycek
win.mainloop()
"""




w = turtle.Screen()
w.title("Yılan Oyunu")
w.setup(600, 600)
w.bgcolor("blue")
w.tracer(0)

# Yılan başı
yn = turtle.Turtle()
yn.speed(0)
yn.shape("circle")
yn.color("red")
yn.penup()
yn.goto(0, 0)
yn.yon = "dur"

# Yem
yem = turtle.Turtle()
yem.speed(0)
yem.shape("circle")
yem.color("brown")
yem.penup()
yem.goto(0, 100)

# Hareket fonksiyonu
def hareket():
    if yn.yon == "ust":
        y = yn.ycor()
        yn.sety(y + 20)
    if yn.yon == "alt":
        y = yn.ycor()
        yn.sety(y - 20)
    if yn.yon == "sag":
        x = yn.xcor()
        yn.setx(x + 20)
    if yn.yon == "sol":
        x = yn.xcor()
        yn.setx(x - 20)

# Yön değiştirme fonksiyonları
def yukariGit():
    if yn.yon != "alt":
        yn.yon = "ust"

def asagiGit():
    if yn.yon != "ust":
        yn.yon = "alt"

def sagaGit():
    if yn.yon != "sol":
        yn.yon = "sag"

def solaGit():
    if yn.yon != "sag":
        yn.yon = "sol"

# Klavye dinleyicisi
w.listen()
w.onkeypress(yukariGit, "Up")
w.onkeypress(asagiGit, "Down")
w.onkeypress(sagaGit, "Right")
w.onkeypress(solaGit, "Left")

# Yem yeme ve skor güncelleme
def ye():
    global skor, maxSkor
    if yn.distance(yem) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        yem.goto(x, y)
        kuyruk = turtle.Turtle()
        kuyruk.speed(0)
        kuyruk.shape("circle")
        kuyruk.color("white")
        kuyruk.penup()
        Liste.append(kuyruk)
        skor += 5
        if skor > maxSkor:
            maxSkor = skor
        w.title(f"Skor: {skor} En büyük skor: {maxSkor}")

    # Kuyruk hareketi
    uzunluk = len(Liste)
    for indis in range(uzunluk - 1, 0, -1):
        x = Liste[indis - 1].xcor()
        y = Liste[indis - 1].ycor()
        Liste[indis].goto(x, y)

    if len(Liste) > 0:
        x = yn.xcor()
        y = yn.ycor()
        Liste[0].goto(x, y)

# Başlangıç konumuna dönme
def baslangic():
    global skor
    time.sleep(0.5)
    yn.goto(0, 0)
    yn.yon = "dur"
    for eklem in Liste:
        eklem.goto(1000, 1000)
    Liste.clear()
    skor = 0
    w.title(f"Skor: {skor} En büyük skor: {maxSkor}")

# Ana oyun döngüsü
while True:
    w.update()
    hareket()
    ye()
    # Sınır kontrolü
    if yn.xcor() > 290 or yn.xcor() < -290 or yn.ycor() > 290 or yn.ycor() < -290:
        baslangic()
    # Kuyruğa çarpma kontrolü
    for eklem in Liste:
        if eklem.distance(yn) < 20:
            baslangic()
    time.sleep(0.1)







        
