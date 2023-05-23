import partie_restart

def en_jeux():
    
    while True:
        window.update()
        move_balle.deplacement_balle()
        collision1.collision_barre()
    
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
    
def recommencer():
    
    coeur.vie = 3
    move_balle.ball.goto(0, -150)
    coeur.carre1.showturtle()
    coeur.carre2.showturtle()
    coeur.carre3.showturtle()
    
    
    
def mise_relation():
    