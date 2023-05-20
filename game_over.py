"""Gère la défaite"""


import turtle as tr

tr.register_shape("fond jeu.gif")
window = tr.Screen()
window.bgpic("fond jeu.gif")
window.tracer(0)

def game_over():
    """Fais apparaître le texte Game Over"""
    window.clear()
    game_over_text = tr.Turtle()
    game_over_text.color("red")
    game_over_text.penup()
    game_over_text.goto(0, 50) # pour afficher le message plus haut
    game_over_text.write("Game Over :/", align = "center", font = ("chalkduster", 40, "normal"))
    game_over_text.hideturtle()
