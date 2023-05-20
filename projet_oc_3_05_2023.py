"""Création de la balle"""


import turtle as tr

window = tr.Screen()
window.bgcolor("black")
window.setup(width=600, height=600)

balle=tr.Turtle()
balle.speed(0)
balle.shape("circle")
balle.color("yellow")
balle.penup()
balle.setposition(0,-200)



