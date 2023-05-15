"""Création et mouvement de la balle"""

import turtle as tr
import random

ball = tr.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_wid = 1.5, stretch_len = 1.5)
ball.color("red")
ball.penup()
ball.setposition(0,-150)
ball.dx = -2
ball.dy = -2


def deplacement_balle():
    """Fais se déplacer la balle"""
    while True:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        
        if ball.xcor() > 280:     # Rebond à droite
            ball.dx *= -1
        elif ball.xcor() < -280:  # Rebond à gauche
            ball.dx *= -1
        elif ball.ycor() > 280:   # Rebond en haut
            ball.dy *= -1
        elif ball.ycor() < -280:  # Rebond en bas
            ball.dy *= -1
        
        
if __name__ == "__main__":
    deplacement_balle()
    window.listen()