"""Création et déplacement de la barre"""

import turtle as tr

window = tr.Screen()
window.bgcolor("black")
window.setup(width=600, height=600)


barre = tr.Turtle()
barre.speed(0)
barre.shape("square")
barre.shapesize(stretch_wid = 0.25, stretch_len=5)
barre.color("red")
barre.penup()
barre.setposition(0,-225)


def aller_droite():
    """Permer à la barre d'aller à droite"""
    x = barre.xcor()
    x += 30
    barre.setx(x)

window.listen()
window.onkeypress(aller_droite,"d")


    
def aller_gauche():
    """Permet à la barre d'aller à gauche"""
    x = barre.xcor()
    x -= 30
    barre.setx(x)

window.listen()
window.onkeypress(aller_gauche,"a")