from turtle import *

turtle=Turtle()
miniTr=Turtle()
turtle.color('blue')
turtle.pensize(4)
miniTr.color("blue")
miniTr.pensize(2)
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
    turtle.hideturtle()

elipse(478,0)
elipse(150,0)
elipse(-178,0)

def unTriangle(longueurCote):
    for i in range(3):
        turtle.forward(longueurCote)
        turtle.left(360/3)


def miniper(longueur1,longueur2):
    
        miniTr.forward(longueur1)
        miniTr.left(90)
        miniTr.forward(longueur2)

miniTr.penup()
miniTr.sety(0)
miniTr.setx(-505)
miniTr.pendown()

def insideElipse():
    
    
    unTriangle(90)
    turtle.forward(90)
    miniTr.forward(45)
    miniTr.left(90)
    miniTr.forward(77)
    miniTr.left(180)
    miniTr.forward(77)
    miniTr.left(90)
    miniTr.forward(45)





    unTriangle(140)
    turtle.forward(140)
    
    miniTr.forward(70)
    miniTr.left(90)
    miniTr.forward(121)
    miniTr.left(180)
    miniTr.forward(121)
    miniTr.left(90)
    miniTr.forward(70)

    unTriangle(98)
    turtle.forward(98)
    
    miniTr.forward(49)
    miniTr.left(90)
    miniTr.forward(85)
    miniTr.left(180)
    miniTr.forward(85)
    miniTr.left(90)
    miniTr.forward(49)
insideElipse()
insideElipse()
insideElipse()


def unRectangle(posx,posy,longueur, largeur):
    turtle.penup()
    turtle.sety(posy)
    turtle.setx(posx)
    turtle.pendown()

    turtle.color("blue","blue")

    turtle.begin_fill()

    turtle.forward(longueur)
    turtle.right(90)
    turtle.forward(largeur)
    turtle.right(90)
    turtle.forward(longueur)
    turtle.right(90)
    turtle.forward(largeur)
    turtle.end_fill()

unRectangle(100 ,0, 100,25)


turtle.right(90)

unRectangle(50 ,-25, 200,25)

turtle.right(90)

unRectangle(-230 ,0,100,25)

turtle.right(90)

unRectangle(-280 ,-25,200,25)

turtle.right(90)

turtle.hideturtle()
done()
