from turtle import *
droite=Turtle()
gauche=Turtle()
droite.speed("fastest")
gauche.speed("fastest")
def unCarreG(cote):
    gauche.forward(cote)
    gauche.left(90)
    gauche.forward(cote)
    gauche.left(90)
    gauche.forward(cote)
    gauche.left(90)
    gauche.forward(cote)
    gauche.hideturtle()
    droite.hideturtle()



def unCarreD(cote):
    gauche.forward(cote)
    gauche.right(90)
    gauche.forward(cote)
    gauche.right(90)
    gauche.forward(cote)
    gauche.right(90)
    gauche.forward(cote)
    gauche.hideturtle()
    droite.hideturtle()


def unRectangleG(longueur,largeur):
    gauche.forward(longueur)
    gauche.left(90)
    gauche.forward(largeur)
    gauche.left(90)
    gauche.forward(longueur)
    gauche.left(90)
    gauche.forward(largeur)
    gauche.hideturtle()
    droite.hideturtle()


def unRectangleD(longueur,largeur):
    gauche.forward(longueur)
    gauche.right(90)
    gauche.forward(largeur)
    gauche.right(90)
    gauche.forward(longueur)
    gauche.right(90)
    gauche.forward(largeur)
    gauche.hideturtle()
    droite.hideturtle()

def fourCarre(pox,poy):
# 4 carres
    gauche.penup()
    gauche.sety(poy)
    gauche.setx(pox)
    gauche.pendown()
    gauche.color('black', 'white')
    gauche.begin_fill()
    
    unCarreG(50)
    droite.right(180)
    unCarreD(50)

    droite.right(90)
    gauche.right(90)

    unCarreG(50)
    unCarreD(50)
    gauche.end_fill()
    gauche.hideturtle()
    droite.hideturtle()
# droite=Turtle()
# gauche=Turtle()
# fin 4 carres

def fourRectangle(pox,poy):
#  debut 4 rectangle
    gauche.penup()
    gauche.sety(poy)
    gauche.setx(pox)
    gauche.pendown()
    gauche.left(90)
    gauche.color('black', 'white')
    gauche.begin_fill()
    unRectangleG(100, 50)
    gauche.right(90)
    unRectangleD(100, 50)

    gauche.right(90)

    unRectangleG(100, 50)
    gauche.right(90)
    unRectangleD(100, 50)
    gauche.end_fill()
    gauche.hideturtle()
    droite.hideturtle()


def miniFourRectangle(pox,poy):
#  debut 4 rectangle
    gauche.penup()
    gauche.sety(poy)
    gauche.setx(pox)
    gauche.pendown()
    gauche.left(90)
    gauche.color('black', 'white')
    gauche.begin_fill()
    unRectangleG(50, 25)
    gauche.right(90)
    unRectangleD(50, 25)

    gauche.right(90)

    unRectangleG(50, 25)
    gauche.right(90)
    unRectangleD(50, 25)
    gauche.end_fill()
    gauche.hideturtle()
    droite.hideturtle()


def deuxRectangle(pox,poy):
#  debut 4 rectangle
    gauche.penup()
    gauche.sety(poy)
    gauche.setx(pox)
    gauche.pendown()
    gauche.left(90)
    gauche.color('black', 'white')
    gauche.begin_fill()
    unRectangleG(50, 25)
    gauche.right(90)
    # unRectangleD(50, 25)

    gauche.right(90)

    # unRectangleG(50, 25)
    gauche.right(90)
    unRectangleD(50, 25)
    gauche.end_fill()

    gauche.hideturtle()
    droite.hideturtle()



#   fin 4 rectangle
def englobeFourCarreAndFourRectangle(posx,posy):
    gauche.penup()
    gauche.sety(posy)
    gauche.setx(posx)
    gauche.pendown()
    gauche.right(90)
    gauche.color('black', 'grey')
    gauche.begin_fill()

    unRectangleD(370, 120)
    gauche.end_fill()
    gauche.hideturtle()
    droite.hideturtle()

def RectangleVide(posx,posy,longueur,largeur):
    gauche.penup()
    gauche.sety(posy)
    gauche.setx(posx)
    gauche.pendown()
    gauche.right(90)
    unRectangleD(longueur, largeur)
    gauche.hideturtle()
    droite.hideturtle()

    
def RectangleNonVide(posx,posy,longueur,largeur):
    gauche.penup()
    gauche.sety(posy)
    gauche.setx(posx)
    gauche.pendown()
    gauche.right(90)
    gauche.color('black', '#A6A6A6')
    gauche.begin_fill()
    unRectangleD(longueur, largeur)
    gauche.end_fill()
    gauche.hideturtle()
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
    gauche.hideturtle()
    droite.hideturtle()
def pointCentrale(posx,posy):
    droite.penup()
    droite.sety(posy)
    droite.setx(posx)
    droite.pendown()
    droite.dot(25)
    gauche.hideturtle()
    droite.hideturtle()
    
  
# le centre
# englobeFourCarreAndFourRectangle(60,160)


RectangleVide(125,280,50,250)


deuxRectangle(0, 230)
deuxRectangle(-100, 280)
deuxRectangle(100, 230)

droite=Turtle()
gauche=Turtle()

droite.speed("fastest")
gauche.speed("fastest")
#plafon
def plafond():
    
    gauche.color('black', 'green')
    gauche.begin_fill()

    gauche.penup()
    gauche.sety(280)
    gauche.setx(-400)
    gauche.pendown()
    gauche.begin_fill()

    gauche.left(15)
    gauche.forward(200)
    gauche.right(15)
    gauche.forward(420)

    gauche.left(345)
    gauche.forward(200)
    # gauche.left(15+180)
    # gauche.forward(820)
    gauche.end_fill()
    gauche.hideturtle()
    droite.hideturtle()


# gauche.right(15)
# gauche.forward(450)
plafond()
droite=Turtle()
gauche=Turtle()

gauche.hideturtle()
droite.hideturtle()

droite.speed("fastest")
gauche.speed("fastest")


RectangleVide(375,280,50,250)


deuxRectangle(375, 230)
deuxRectangle(225, 280)
# deuxRectangle(100, 230)

droite=Turtle()
gauche=Turtle()

gauche.hideturtle()
droite.hideturtle()

droite.speed("fastest")
gauche.speed("fastest")

RectangleVide(-125,280,50,250)


deuxRectangle(-375, 230)
deuxRectangle(-225, 280)

droite=Turtle()
gauche=Turtle()

gauche.hideturtle()
droite.hideturtle()

droite.speed("fastest")
gauche.speed("fastest")


RectangleVide(100,230,50,200)
gauche.right(90)
gauche.forward(35)
gauche.left(90)

# gauche.right(90)

gauche.forward(450)
gauche.right(90)
gauche.forward(420)

gauche.penup()
gauche.sety(195)
gauche.setx(-100)
gauche.pendown()

gauche.right(90)

gauche.forward(450)
gauche.left(90)
gauche.forward(420)


#deb

droite=Turtle()
gauche=Turtle()

gauche.hideturtle()
droite.hideturtle()

droite.speed("fastest")
gauche.speed("fastest")

gauche.penup()
gauche.sety(230)
gauche.setx(100)
gauche.pendown()


gauche.forward(485)
gauche.right(135)
gauche.forward(50)

gauche.penup()
gauche.sety(230)
gauche.setx(100)
gauche.pendown()

gauche.right(45)
gauche.forward(685)
gauche.left(135)
gauche.forward(50)



droite=Turtle()
gauche=Turtle()

gauche.hideturtle()
droite.hideturtle()

droite.speed("fastest")
gauche.speed("fastest")


RectangleVide(65,180,365,120)
RectangleVide(55,180,365,100)
RectangleNonVide(45,180,365,80)#ma nieuw
miniFourRectangle(5,-70)
droite=Turtle()
gauche=Turtle()

gauche.hideturtle()
droite.hideturtle()

droite.speed("fastest")
gauche.speed("fastest")

gauche.right(90)
RectangleVide(30, -190, 50, 5)


droite=Turtle()
gauche=Turtle()

gauche.hideturtle()
droite.hideturtle()


droite.speed("fastest")
gauche.speed("fastest")


gauche.right(90)
RectangleVide(65, -190, 35, 5)

droite=Turtle()
gauche=Turtle()


gauche.hideturtle()
droite.hideturtle()

droite.speed("fastest")
gauche.speed("fastest")

gauche.right(90)
RectangleVide(-20, -190, 35, 5)


RectangleVide(30, -195, 50, 5)

RectangleVide(35, -200, 60, 5)
RectangleVide(40, -205, 70, 5)
RectangleVide(45, -210, 80, 5)
RectangleVide(50, -215, 90, 5)
RectangleVide(55, -220, 100, 5)
RectangleVide(550, -225, 1100, 5)#bi ssi souff
gauche.left(90)
RectangleVide(65, -185, 35, 5)
RectangleVide(-50, -185, 35, 5)

droite=Turtle()
gauche=Turtle()

gauche.hideturtle()
droite.hideturtle()


droite.speed("fastest")
gauche.speed("fastest")

droite.left(90)
unDemiCercle(30,-20,25)
pointCentrale(0,50)
deuxRectangle(0, 75)
droite=Turtle()
gauche=Turtle()

gauche.hideturtle()
droite.hideturtle()

droite.speed("fastest")
gauche.speed("fastest")
# 1ere a droite
englobeFourCarreAndFourRectangle(210,160)
fourCarre(150,100)
droite=Turtle()
gauche=Turtle()

gauche.hideturtle()
droite.hideturtle()

droite.speed("fastest")
gauche.speed("fastest")
fourRectangle(150,-100)
droite=Turtle()
gauche=Turtle()

gauche.hideturtle()
droite.hideturtle()

droite.speed("fastest")
gauche.speed("fastest")

# 1ere a gauche
englobeFourCarreAndFourRectangle(-90,160)
fourCarre(-150,100)
droite=Turtle()
gauche=Turtle()

gauche.hideturtle()
droite.hideturtle()

droite.speed("fastest")
gauche.speed("fastest")
fourRectangle(-150,-100)
droite=Turtle()
gauche=Turtle()

gauche.hideturtle()
droite.hideturtle()

droite.speed("fastest")
gauche.speed("fastest")
# 2ere a droite
englobeFourCarreAndFourRectangle(360,160)
fourCarre(300,100)
droite=Turtle()
gauche=Turtle()

gauche.hideturtle()
droite.hideturtle()

droite.speed("fastest")
gauche.speed("fastest")
fourRectangle(300,-100)
droite=Turtle()
gauche=Turtle()

gauche.hideturtle()
droite.hideturtle()

droite.speed("fastest")
gauche.speed("fastest")


# 2eme a gauche
englobeFourCarreAndFourRectangle(-240,160)
fourCarre(-300,100)
droite=Turtle()
gauche=Turtle()

gauche.hideturtle()
droite.hideturtle()

droite.speed("fastest")
gauche.speed("fastest")
fourRectangle(-300,-100)
droite=Turtle()
gauche=Turtle()

gauche.hideturtle()
droite.hideturtle()

droite.speed("fastest")
gauche.speed("fastest")

# 3ere a droite
englobeFourCarreAndFourRectangle(510,160)
fourCarre(450,100)
droite=Turtle()
gauche=Turtle()

gauche.hideturtle()
droite.hideturtle()

droite.speed("fastest")
gauche.speed("fastest")
fourRectangle(450,-100)
droite=Turtle()
gauche=Turtle()

gauche.hideturtle()
droite.hideturtle()

droite.speed("fastest")
gauche.speed("fastest")

# 3eme a gauche
englobeFourCarreAndFourRectangle(-390,160)
fourCarre(-450,100)
droite=Turtle()
gauche=Turtle()

gauche.hideturtle()
droite.hideturtle()

droite.speed("fastest")
gauche.speed("fastest")
fourRectangle(-450,-100)
droite=Turtle()
gauche=Turtle()

gauche.hideturtle()
droite.hideturtle()
    
droite.speed("fastest")
gauche.speed("fastest")
done()
