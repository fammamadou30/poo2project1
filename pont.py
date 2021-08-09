from turtle import *

turtle=Turtle()
miniTr=Turtle()
turtle.color('blue')
turtle.pensize(4)
miniTr.color("blue")
miniTr.pensize(6)
turtle.speed("fastest")
miniTr.speed("fastest")
def elipse(posx,posy):
    turtle.penup()
    turtle.sety(posy)
    turtle.setx(posx)
    turtle.pendown()
    turtle.left(90)
    turtle.circle(90,45)
    turtle.circle(195,90)
    turtle.circle(90,45)
    turtle.left(90)


elipse(478,0)
elipse(150,0)
elipse(-178,0)

def unTriangle(longueurCote):
    for i in range(3):
        turtle.forward(longueurCote)
        turtle.left(360/3)


def miniTriangle(longueurCote):
    
    for i in range(3):
        miniTr.forward(longueurCote)
        miniTr.left(360/3)
miniTr.penup()
miniTr.sety(0)
miniTr.setx(-505)
miniTr.pendown()

def insideElipse():
    
    
    unTriangle(90)
    turtle.forward(90)

    miniTriangle(45)
    miniTr.forward(45)


    miniTriangle(45)
    miniTr.forward(45)


    unTriangle(140)
    turtle.forward(140)


    miniTriangle(70)
    miniTr.forward(70)


    miniTriangle(70)
    miniTr.forward(70)

    unTriangle(98)
    turtle.forward(98)


    miniTriangle(49)
    miniTr.forward(49)

    miniTriangle(49)
    miniTr.forward(49)
insideElipse()
insideElipse()
insideElipse()


def unRectangle(posx,posy,longueur, largeur):
    turtle.penup()
    turtle.sety(posy)
    turtle.setx(posx)
    turtle.pendown()


    turtle.forward(longueur)
    turtle.right(90)
    turtle.forward(largeur)
    turtle.right(90)
    turtle.forward(longueur)
    turtle.right(90)
    turtle.forward(largeur)
unRectangle(-515 ,0, 50,200)
turtle.right(90)

unRectangle(135 ,0, 50,200)
turtle.right(90)


unRectangle(-200 ,0, 50,200)
turtle.right(90)

unRectangle(455 ,0, 50,200)

done()