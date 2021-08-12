from turtle import *
from genieCivilOuvrage2D import *
droite=Turtle()
turtle=Turtle()
droite.speed("fastest")
turtle.speed("fastest")
def unCarreG(cote):
    turtle.forward(cote)
    turtle.left(90)
    turtle.forward(cote)
    turtle.left(90)
    turtle.forward(cote)
    turtle.left(90)
    turtle.forward(cote)
    turtle.hideturtle()
    droite.hideturtle()



def unCarreD(cote):
    turtle.forward(cote)
    turtle.right(90)
    turtle.forward(cote)
    turtle.right(90)
    turtle.forward(cote)
    turtle.right(90)
    turtle.forward(cote)
    turtle.hideturtle()
    droite.hideturtle()


def unRectangleG(longueur,largeur):
    turtle.forward(longueur)
    turtle.left(90)
    turtle.forward(largeur)
    turtle.left(90)
    turtle.forward(longueur)
    turtle.left(90)
    turtle.forward(largeur)
    turtle.hideturtle()
    droite.hideturtle()


def unRectangleD(longueur,largeur):
    turtle.forward(longueur)
    turtle.right(90)
    turtle.forward(largeur)
    turtle.right(90)
    turtle.forward(longueur)
    turtle.right(90)
    turtle.forward(largeur)
    turtle.hideturtle()
    droite.hideturtle()

def fourCarre(pox,poy):
# 4 carres
    turtle.penup()
    turtle.sety(poy)
    turtle.setx(pox)
    turtle.pendown()
    turtle.color('black', 'white')
    turtle.begin_fill()
    
    unCarreG(50)
    droite.right(180)
    unCarreD(50)

    droite.right(90)
    turtle.right(90)

    unCarreG(50)
    unCarreD(50)
    turtle.end_fill()
    turtle.hideturtle()
    droite.hideturtle()
# droite=Turtle()
# turtle=Turtle()
# fin 4 carres

def fourRectangle(pox,poy):
#  debut 4 rectangle
    turtle.penup()
    turtle.sety(poy)
    turtle.setx(pox)
    turtle.pendown()
    turtle.left(90)
    turtle.color('black', 'white')
    turtle.begin_fill()
    unRectangleG(100, 50)
    turtle.right(90)
    unRectangleD(100, 50)

    turtle.right(90)

    unRectangleG(100, 50)
    turtle.right(90)
    unRectangleD(100, 50)
    turtle.end_fill()
    turtle.hideturtle()
    droite.hideturtle()


def miniFourRectangle(pox,poy):
#  debut 4 rectangle
    turtle.penup()
    turtle.sety(poy)
    turtle.setx(pox)
    turtle.pendown()
    turtle.left(90)
    turtle.color('black', 'white')
    turtle.begin_fill()
    unRectangleG(50, 25)
    turtle.right(90)
    unRectangleD(50, 25)

    turtle.right(90)

    unRectangleG(50, 25)
    turtle.right(90)
    unRectangleD(50, 25)
    turtle.end_fill()
    turtle.hideturtle()
    droite.hideturtle()


def deuxRectangle(pox,poy):
#  debut 4 rectangle
    turtle.penup()
    turtle.sety(poy)
    turtle.setx(pox)
    turtle.pendown()
    turtle.left(90)
    turtle.color('black', 'white')
    turtle.begin_fill()
    unRectangleG(50, 25)
    turtle.right(90)
    # unRectangleD(50, 25)

    turtle.right(90)

    # unRectangleG(50, 25)
    turtle.right(90)
    unRectangleD(50, 25)
    turtle.end_fill()

    turtle.hideturtle()
    droite.hideturtle()



#   fin 4 rectangle
def englobeFourCarreAndFourRectangle(posx,posy):
    turtle.penup()
    turtle.sety(posy)
    turtle.setx(posx)
    turtle.pendown()
    turtle.right(90)
    turtle.color('black', 'grey')
    turtle.begin_fill()

    unRectangleD(370, 120)
    turtle.end_fill()
    turtle.hideturtle()
    droite.hideturtle()

def RectangleVide(posx,posy,longueur,largeur):
    turtle.penup()
    turtle.sety(posy)
    turtle.setx(posx)
    turtle.pendown()
    turtle.right(90)
    unRectangleD(longueur, largeur)
    turtle.hideturtle()
    droite.hideturtle()

    
def RectangleNonVide(posx,posy,longueur,largeur):
    turtle.penup()
    turtle.sety(posy)
    turtle.setx(posx)
    turtle.pendown()
    turtle.right(90)
    turtle.color('black', '#A6A6A6')
    turtle.begin_fill()
    unRectangleD(longueur, largeur)
    turtle.end_fill()
    turtle.hideturtle()
    droite.hideturtle()
def unDemiCercle(posx,posy,rayon):
    droite.penup()
    droite.sety(posy)
    droite.setx(posx)
    droite.pendown()
    droite.color('black', 'white')
    droite.begin_fill()
    droite.circle(rayon, 180)
    droite.end_fill()
    turtle.hideturtle()
    droite.hideturtle()
def pointCentrale(posx,posy):
    droite.penup()
    droite.sety(posy)
    droite.setx(posx)
    droite.pendown()
    droite.dot(25)
    turtle.hideturtle()
    droite.hideturtle()
    
  
# le centre
# englobeFourCarreAndFourRectangle(60,160)


RectangleVide(125,280,50,250)


deuxRectangle(0, 230)
deuxRectangle(-100, 280)
deuxRectangle(100, 230)

droite=Turtle()
turtle=Turtle()

droite.speed("fastest")
turtle.speed("fastest")
#plafon
def plafond():
    
    turtle.color('black', 'green')
    turtle.begin_fill()

    turtle.penup()
    turtle.sety(280)
    turtle.setx(-400)
    turtle.pendown()
    turtle.begin_fill()

    turtle.left(15)
    turtle.forward(200)
    turtle.right(15)
    turtle.forward(420)

    turtle.left(345)
    turtle.forward(200)
    # turtle.left(15+180)
    # turtle.forward(820)
    turtle.end_fill()
    turtle.hideturtle()
    droite.hideturtle()


# turtle.right(15)
# turtle.forward(450)
plafond()
droite=Turtle()
turtle=Turtle()

turtle.hideturtle()
droite.hideturtle()

droite.speed("fastest")
turtle.speed("fastest")


RectangleVide(375,280,50,250)


deuxRectangle(375, 230)
deuxRectangle(225, 280)
# deuxRectangle(100, 230)

droite=Turtle()
turtle=Turtle()

turtle.hideturtle()
droite.hideturtle()

droite.speed("fastest")
turtle.speed("fastest")

RectangleVide(-125,280,50,250)


deuxRectangle(-375, 230)
deuxRectangle(-225, 280)

droite=Turtle()
turtle=Turtle()

turtle.hideturtle()
droite.hideturtle()

droite.speed("fastest")
turtle.speed("fastest")


RectangleVide(100,230,50,200)
turtle.right(90)
turtle.forward(35)
turtle.left(90)

# turtle.right(90)

turtle.forward(450)
turtle.right(90)
turtle.forward(420)

turtle.penup()
turtle.sety(195)
turtle.setx(-100)
turtle.pendown()

turtle.right(90)

turtle.forward(450)
turtle.left(90)
turtle.forward(420)


#deb

droite=Turtle()
turtle=Turtle()

turtle.hideturtle()
droite.hideturtle()

droite.speed("fastest")
turtle.speed("fastest")

turtle.penup()
turtle.sety(230)
turtle.setx(100)
turtle.pendown()


turtle.forward(485)
turtle.right(135)
turtle.forward(50)

turtle.penup()
turtle.sety(230)
turtle.setx(100)
turtle.pendown()

turtle.right(45)
turtle.forward(685)
turtle.left(135)
turtle.forward(50)



droite=Turtle()
turtle=Turtle()

turtle.hideturtle()
droite.hideturtle()

droite.speed("fastest")
turtle.speed("fastest")


RectangleVide(65,180,325,120)
RectangleVide(55,180,325,100)
RectangleNonVide(45,180,325,80)#ma nieuw
miniFourRectangle(5,-95)
droite=Turtle()
turtle=Turtle()

turtle.hideturtle()
droite.hideturtle()

droite.speed("fastest")
turtle.speed("fastest")

turtle.right(90)
RectangleVide(30, -155, 50, 10)


droite=Turtle()
turtle=Turtle()

turtle.hideturtle()
droite.hideturtle()


droite.speed("fastest")
turtle.speed("fastest")


turtle.right(90)
RectangleVide(65, -155, 35, 10)

droite=Turtle()
turtle=Turtle()


turtle.hideturtle()
droite.hideturtle()

droite.speed("fastest")
turtle.speed("fastest")

turtle.right(90)
RectangleVide(-20, -155, 35, 10)


RectangleVide(30, -165, 50, 10)

RectangleVide(35, -175, 60, 10)
RectangleVide(40, -185, 70,10)
RectangleVide(45, -195, 80,10)
RectangleVide(50, -205, 90,10)
RectangleVide(55, -215, 100,10)
RectangleVide(550, -225, 1100,10)#bi ssi souff
turtle.left(90)
RectangleVide(65, -155, 60, 10)
RectangleVide(-45, -155, 60,10)

droite=Turtle()
turtle=Turtle()

turtle.hideturtle()
droite.hideturtle()


droite.speed("fastest")
turtle.speed("fastest")

droite.left(90)
unDemiCercle(30,-45,25)
pointCentrale(5,20)
deuxRectangle(5, 70)
droite=Turtle()
turtle=Turtle()

turtle.hideturtle()
droite.hideturtle()

droite.speed("fastest")
turtle.speed("fastest")
# 1ere a droite
englobeFourCarreAndFourRectangle(210,160)
fourCarre(150,100)
droite=Turtle()
turtle=Turtle()

turtle.hideturtle()
droite.hideturtle()

droite.speed("fastest")
turtle.speed("fastest")
fourRectangle(150,-100)
droite=Turtle()
turtle=Turtle()

turtle.hideturtle()
droite.hideturtle()

droite.speed("fastest")
turtle.speed("fastest")

# 1ere a turtle
englobeFourCarreAndFourRectangle(-90,160)
fourCarre(-150,100)
droite=Turtle()
turtle=Turtle()

turtle.hideturtle()
droite.hideturtle()

droite.speed("fastest")
turtle.speed("fastest")
fourRectangle(-150,-100)
droite=Turtle()
turtle=Turtle()

turtle.hideturtle()
droite.hideturtle()

droite.speed("fastest")
turtle.speed("fastest")
# 2ere a droite
englobeFourCarreAndFourRectangle(360,160)
fourCarre(300,100)
droite=Turtle()
turtle=Turtle()

turtle.hideturtle()
droite.hideturtle()

droite.speed("fastest")
turtle.speed("fastest")
fourRectangle(300,-100)
droite=Turtle()
turtle=Turtle()

turtle.hideturtle()
droite.hideturtle()

droite.speed("fastest")
turtle.speed("fastest")


# 2eme a turtle
englobeFourCarreAndFourRectangle(-240,160)
fourCarre(-300,100)
droite=Turtle()
turtle=Turtle()

turtle.hideturtle()
droite.hideturtle()

droite.speed("fastest")
turtle.speed("fastest")
fourRectangle(-300,-100)
droite=Turtle()
turtle=Turtle()

turtle.hideturtle()
droite.hideturtle()

droite.speed("fastest")
turtle.speed("fastest")

# 3ere a droite
englobeFourCarreAndFourRectangle(510,160)
fourCarre(450,100)
droite=Turtle()
turtle=Turtle()

turtle.hideturtle()
droite.hideturtle()

droite.speed("fastest")
turtle.speed("fastest")
fourRectangle(450,-100)
droite=Turtle()
turtle=Turtle()

turtle.hideturtle()
droite.hideturtle()

droite.speed("fastest")
turtle.speed("fastest")

# 3eme a turtle
englobeFourCarreAndFourRectangle(-390,160)
fourCarre(-450,100)
droite=Turtle()
turtle=Turtle()

turtle.hideturtle()
droite.hideturtle()

droite.speed("fastest")
turtle.speed("fastest")
fourRectangle(-450,-100)
droite=Turtle()
turtle=Turtle()

turtle.hideturtle()
droite.hideturtle()
    
droite.speed("fastest")
turtle.speed("fastest")
done()
