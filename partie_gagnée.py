""""Vérifie si les briques ont disparus et affiche un message de victoire"""

import turtle as tr
import module_briques as brick

"""Crée le message de victoire"""
def message_victoire():
    message = tr.Turtle()
    message.speed(0)
    message.color("withe")
    message.hideturtle()
    message.goto(0,0)
    message.write("Bravo tu as gagné !", align = "center",font=("chalkduster", 40, "normal"))
    
"""Détermine si il reste des briques"""
def victoire():
    if all(len(ligne) == 0 for ligne in brick.briques):
        message_victoire()
        