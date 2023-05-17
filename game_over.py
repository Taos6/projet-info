"""Gère la défaite"""
import creation_mouvement_balle as move_balle
import turtle as tr

window = tr.Screen()
window.bgcolor("black")
window.setup(width=600, height=600)


def game_over():
    """Fais apparaître le texte Game Over"""
    window.clear()
    game_over_text = tr.Turtle()
    game_over_text.color("red")
    game_over_text.penup()
    game_over_text.goto(0, 50) # pour afficher le message plus haut  
    game_over_text.write("Game Over :/", align = "center", font = ("chalkduster", 40, "normal"))
    game_over_text.hideturtle()
    

