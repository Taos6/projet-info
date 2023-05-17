""""Vérifie si les briques ont disparus et affiche un message de victoire"""

import turtle as tr
import module_briques as brick

window = tr.Screen()
window.bgcolor("black")
window.setup(width=600, height=600)

"""Crée le message de victoire"""
def message_victoire():
    window.reset()
    message = tr.Turtle()
    message.speed(0)
    message.color("white")
    message.penup()
    message.setposition(0,0)
    message.write("Bravo tu as gagné !", align = "center",font=("chalkduster", 40, "normal"))
    message.hideturtle()
    
    


    


    
        
        