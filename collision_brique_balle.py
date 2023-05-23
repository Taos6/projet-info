"""Fichier gérant les collisions entre les briques et la balle"""


import creation_mouvement_balle as move_balle
import module_briques as brick
import victoire as win


def collision_brique(): 
    """Vérifie si la balle touche une brique"""
    for ligne_briques in brick.briques:
        for brique in ligne_briques:
            if move_balle.ball.ycor()  < brique.ycor() + 5\
               and move_balle.ball.ycor() > brique.ycor() -5\
               and move_balle.ball.xcor() < brique.xcor() + 25\
               and move_balle.ball.xcor() > brique.xcor() -25:
                brique.hideturtle()
                ligne_briques.remove(brique)
                move_balle.ball.dy *= -1
                if all(len(ligne) == 0 for ligne in brick.briques):
                    win.message_victoire()
                    return True
                
                
