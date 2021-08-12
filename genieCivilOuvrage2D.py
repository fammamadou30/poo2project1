# Un module contenant des fonctions nous permettant de tracer les figures suivantes:
#• Un cercle
#• Un demi - Cercle
#• Un carré
#• Un triangle
#• Un rectangle
#• Un polygone
#• Un trapèze
#• Un losange
#• Une Ellipse
from turtle import*
from math import*

# Fonction Python pour dessiner un cercle
def cercle(rayon):
    circle(rayon)

# Fonction Python pour dessiner un demi cercle
def demiCercle(rayon):
    seth(90)
    circle(rayon, 180)

def carre(cote):
    for i in range(4):
        forward(cote)
        left(90)

def triangle(coteA, coteB, coteC):
    angleB = degrees(acos(((coteA**2) + (coteB**2) - (coteC**2))/(2*coteA*coteB)))
    forward(coteA)
    left(180 - angleB)
    angleC = degrees(acos(((coteB**2) + (coteC**2) - (coteA**2))/(2*coteB*coteC)))
    forward(coteB)
    left(180 - angleC)
    forward(coteC)
    angleA = degrees(acos(((coteB**2) + (coteA**2) - (coteC**2))/(2*coteB*coteA)))
    left(180 - angleA)

def rectangle(longueur, largeur):
    for i in range(2):
        forward(longueur)
        left(90)
        forward(largeur)
        left(90)

def polygone(nombreDeCote, longueurCote):
    for i in range(nombreDeCote):
        fd(longueurCote)
        lt(360/longueurCote)       

def trapeze(grandeBase, petiteBase, cote):
    forward(petiteBase)
    forward(cote)
    left(130)
    forward(grandeBase)
    left(130)
    forward(cote)


def ellispe(rayon):
    seth(-45)
    for i in range(2):
        circle(rayon, 90)
        circle(rayon/3, 90)
