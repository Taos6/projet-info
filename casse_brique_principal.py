"""Ce fichier importe tous les autres et fais tourner le jeu"""


import turtle as tr
import game_over as over
import creation_mouvement_balle as move_balle
import creation_mouvement_barre as move_barre
import creation_coeur as coeur
import collision_balle_barre as collision1
import module_briques as brick
import collision_brique_balle as collision2

tr.register_shape("fond jeu.gif")
window = tr.Screen()
window.bgpic("fond jeu.gif")

# window.setup(width=600, height=600)
window.tracer(0)

coeur.nb_vie()


while True:
    window.update()
    move_balle.deplacement_balle()
    collision1.collision_barre()
    test_victoire = collision2.collision_brique()
    if test_victoire == True:
        break
    if move_balle.ball.ycor() < -280:
        coeur.vie -= 1
        move_balle.ball.goto(0,-150)
        move_balle.ball.dy *= -1
    elif coeur.vie == 2:
        coeur.vie3.hideturtle()
    elif coeur.vie == 1:
        coeur.vie2.hideturtle()
    elif coeur.vie == 0:
        coeur.vie1.hideturtle()
        over.game_over()
        break
        