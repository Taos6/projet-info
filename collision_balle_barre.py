"""Fichier gérant la collision entre la balle et la barre"""

import turtle as tr
import creation_mouvement_balle as move_balle
import creation_mouvement_barre as move_barre


window = tr.Screen()
window.bgcolor("black")
window.setup(width=600, height=600)

def collision_barre():
    if move_balle.ball.ycor() > -230 and move_balle.ball.ycor() < -220\
    and move_balle.ball.xcor() < move_barre.barre.xcor() + 50\
    and move_balle.ball.xcor() > move_barre.barre.xcor() - 50:
        move_balle.ball.dy *= -1
        

if __name__ == "__main__":
    while True:
        window.update()
        move_balle.deplacement_balle()
        collision_barre()
        if move_balle.ball.ycor() < -280:
            move_balle.ball.goto(0,-150)
        
        
        
        