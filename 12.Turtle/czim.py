import turtle 
turtle.color('red','brown')
# Kaplumbağayı ileri götür
#turtle.forward(100)  # 100 birim ileri git saga dogru x + yonune gitti
# Kaplumbağayı geri getir
#turtle.backward(50)  # 50 birim geri git
#turtle.right(90)
#turtle.backward(50)
#turtle.left(90)
#turtle.forward(100)
#turtle.shape('turtle')

#def kareCizim(mesafe):
    #for a in range(1,5):
        #turtle.forward(mesafe)
        #turtle.left(90)


turtle.begin_fill()#icini dolduruyor

#kareCizim(50)
#kareCizim(100)
#kareCizim(150)

turtle.shape('blank')
for x in range(2):
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    
turtle.pencolor('red')

turtle.penup()
turtle.goto(75,-80)
turtle.pendown()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill




turtle.end_fill()


#turtle.color('red','brown') #renk veriyor
#turtle.circle(100)

turtle.speed(0)
turtle.bgcolor("white")
turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
for _ in range(2):
    turtle.forward(400)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
turtle.end_fill()
turtle.penup()
turtle.goto(-90, 50)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
turtle.penup()
turtle.goto(-75, 50)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()
turtle.penup()
turtle.goto(-20, 50)
turtle.setheading(0)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
for _ in range(5):
    turtle.forward(60)
    turtle.right(144)
turtle.end_fill()
turtle.hideturtle()
turtle.done()








# Pencereyi açık tut
turtle.done()



