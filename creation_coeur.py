"""Fais apparaître les coeurs du joueur et un message explicatif"""

import turtle as tr
import time

vie = 3
tr.register_shape("image coeur.gif")

vie1 = tr.Turtle()
vie1.speed(0)
vie1.shape("image coeur.gif")
vie1.color("yellow")
vie1.penup()
vie1.setposition(280, 260)

vie2 = tr.Turtle()
vie2.speed(0)
vie2.shape("image coeur.gif")
vie2.color("yellow")
vie2.penup()
vie2.setposition(250, 260)

vie3 = tr.Turtle()
vie3.shape("image coeur.gif")
vie3.speed(0)
vie3.color("yellow")
vie3.penup()
vie3.setposition(220, 260)


def nb_vie():
    """Ce message donne une instruction sur le nombre de vie"""
    vies_text = tr.Turtle()
    vies_text.speed(0)
    vies_text.color("white")
    vies_text.penup()
    vies_text.setposition(280, 280)
    vies_text.write("Vous avez 3 vies et les coeurs représentent le nombre de vies restants", align="right", font=("Goudy Old Style", 15, "normal"))
    vies_text.hideturtle()
    

   
   