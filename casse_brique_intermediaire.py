import turtle as tr
import game_over as over
import projet_oc_10_05_2023 as move_balle
import creation_mouvement_barre as bar

window = tr.Screen()
window.bgcolor("black")
window.setup(width=600, height=600)


while True:
    window.update()
    move_balle.deplacement_balle()
    
    if ball.ycor() < -280:
         game_over()
