""""Vérifie si les briques ont disparus et affiche un message de victoire"""

import turtle as tr
import module_briques as brick
import creation_mouvement_balle as move_balle
import creation_mouvement_barre as move_barre

window = tr.Screen()
window.bgcolor("black")
window.setup(width=600, height=600)

def message_victoire():
    """Crée le message de victoire"""
    window.clear()
    message = tr.Turtle()
    message.speed(0)
    message.color("blue")
    message.penup()
    message.setposition(0,0)
    message.write("Bravo tu as gagné !", align = "center",font=("chalkduster", 40, "normal"))
    message.hideturtle()