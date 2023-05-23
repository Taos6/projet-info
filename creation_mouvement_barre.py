"""Création et déplacement de la barre"""


import turtle as tr

tr.register_shape("image_barre.gif")
barre = tr.Turtle()
barre.speed(0)
barre.shape("image_barre.gif")
barre.penup()
barre.setposition(0,-225)

tr.register_shape("fond jeu.gif")
window = tr.Screen()
window.bgpic("fond jeu.gif")
window.tracer(0)


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
