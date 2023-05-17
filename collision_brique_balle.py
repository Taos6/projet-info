"""Fichier gérant les collisions entre les briques et la balle"""

import creation_mouvement_balle as move_balle
import module_briques as brick


"""Vérifie si la balle touche une brique"""
def collision_brique():
    for ligne_briques in brick.briques:
        for brique in ligne_briques:
            if brique.distance(move_balle.ball) < 25\
            and move_balle.ball.ycor() < brique.ycor() + 25\
            and move_balle.ball.ycor() > brique.ycor() - 25:
                brique.hideturtle()
                ligne_briques.remove(brique)
                move_balle.ball.dy *= -1




  