import turtle as tr
import time

vie = 3
tr.register_shape("image coeur.gif")

carre1 = tr.Turtle()
carre1.speed(0)
carre1.shape("image coeur.gif")
carre1.color("yellow")
carre1.penup()
carre1.setposition(280, 260)

carre2 = tr.Turtle()
carre2.speed(0)
carre2.shape("image coeur.gif")
carre2.color("yellow")
carre2.penup()
carre2.setposition(250, 260)

carre3 = tr.Turtle()
carre3.shape("image coeur.gif")
carre3.speed(0)
carre3.color("yellow")
carre3.penup()
carre3.setposition(220, 260)


def nb_vie():
    """Ce message donne une instruction sur le nombre de vie"""
    vies_text = tr.Turtle()
    vies_text.speed(0)
    vies_text.color("white")
    vies_text.penup()
    vies_text.setposition(280, 280)
    vies_text.write("Vous avez 3 vies et les coeurs représentent le nombre de vies restants", align="right", font=("Goudy Old Style", 15, "normal"))
    vies_text.hideturtle()
    

   
   