"""Fichier gérant les collisions entre les briques et la balle"""

import creation_mouvement_balle as move_balle
import module_briques as brick
import partie_gagnée as win


"""Vérifie si la balle touche une brique"""
def collision_brique():
    for ligne_briques in brick.briques:
        for brique in ligne_briques:
            if move_balle.ball.ycor()  < brique.ycor() + 5\
               and move_balle.ball.ycor() > brique.ycor() -5\
               and move_balle.ball.xcor() < brique.xcor() + 25\
               and move_balle.ball.xcor() > brique.xcor() -25:
                brique.hideturtle()
                ligne_briques.remove(brique)
                move_balle.ball.dy *= -1
                brick.briques.clear()
                if all(len(ligne) == 0 for ligne in brick.briques):
                    win.message_victoire()
                    return True






  