"""Création et mouvement de la balle"""


import turtle as tr

tr.register_shape("balle.gif")
ball = tr.Turtle()
ball.speed(0)
ball.shape("balle.gif")
ball.shapesize(stretch_wid = 0.75, stretch_len = 0.75)
ball.color("red")
ball.penup()
ball.setposition(0,-150)
ball.dx = -3
ball.dy = -3


def deplacement_balle():
    """Fais se déplacer la balle"""
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.xcor() > 285:  # Rebond à droite
        ball.dx *= -1
    elif ball.xcor() < -285:  # Rebond à gauche
        ball.dx *= -1
    elif ball.ycor() > 285:   # Rebond en haut
        ball.dy *= -1
    elif ball.ycor() < -285:  # Rebond en bas
        ball.dy *= -1


if __name__ == "__main__":
    tr.register_shape("fond jeu.gif")
    window = tr.Screen()
    window.bgpic("fond jeu.gif")
    window.tracer(0)
    deplacement_balle()
    window.listen()
