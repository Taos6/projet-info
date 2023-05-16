"""Gère la défaite"""
import creation_mouvement_balle as move_balle
import turtle as tr


def game_over_text():
    """Fais apparaître le texte Game Over"""
    game_over_text = tr.Turtle()
    game_over_text.color("red")
    game_over_text.penup()
    game_over_text.goto(0, 50) # pour afficher le message plus haut  
    game_over_text.write("Game Over :/", align = "center", font = ("chalkduster", 40, "normal"))
    game_over_text.hideturtle()
    

def game_over():
    """Stoppe la partie"""
    move_balle.ball.dx = 0
    move_balle.ball.dy = 0
    move_balle.ball.clear()
    game_over_text()
    text_restart_game()