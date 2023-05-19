"""Création et déplacement de la barre"""

import turtle as tr

tr.register_shape("image_barre.gif")
barre = tr.Turtle()
barre.speed(0)
barre.shape("image_barre.gif")
barre.shapesize(stretch_wid = 0.25, stretch_len=5)
barre.color("red")
barre.penup()
barre.setposition(0,-225)

if __name__ == "__main__":
    window = tr.Screen()
    window.bgcolor("black")
    window.setup(width=600, height=600)



def aller_droite():
    """Permer à la barre d'aller à droite"""
    position_x = barre.xcor()
    position_x += 30
    barre.setx(position_x)

window.listen()
window.onkeypress(aller_droite,"d")


def aller_gauche():
    """Permet à la barre d'aller à gauche"""
    position_x = barre.xcor()
    position_x -= 30
    barre.setx(position_x)

window.listen()
window.onkeypress(aller_gauche,"a")
