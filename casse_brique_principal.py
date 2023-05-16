import turtle as tr
import game_over as over
import creation_mouvement_balle as move_balle
import creation_mouvement_barre as move_barre
import creation_coeur as coeur

window = tr.Screen()
window.bgcolor("black")
window.setup(width=600, height=600)

coeur.nb_vie()

while True:
    window.update()
    move_balle.deplacement_balle()
    if move_balle.ball.ycor() < -280:
        print(move_balle.ball.ycor())
        coeur.vie -= 1
        move_balle.ball.goto(0,-150)
    elif coeur.vie == 2:
        coeur.carre3.hideturtle()
    elif coeur.vie == 1:
        coeur.carre2.hideturtle()
    elif coeur.vie == 0:
        coeur.carre1.hideturtle()
        over.game_over()
        
