import turtle as tr
import game_over as over
import creation_mouvement_balle as move_balle
import creation_mouvement_barre as move_barre

window = tr.Screen()
window.bgcolor("black")
window.setup(width=600, height=600)


while True:
    window.update()
    move_balle.deplacement_balle()
    
    if ball.ycor() < -280:
         game_over()
