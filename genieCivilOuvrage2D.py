from turtle import *

droite=Turtle()
turtle=Turtle()
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
    
  
