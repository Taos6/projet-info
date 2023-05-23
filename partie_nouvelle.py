"""Vérifie si le joueur veut rejouer, si oui une nouvelle partie est lancée, sinon la fenêtre est fermée"""


def Nouvelle_partie():
    """Cette fonction crée une nouvelle partie"""

    tr.register_shape("fond jeu.gif")
    window = tr.Screen()
    window.bgpic("fond jeu.gif")
    window.tracer(0)

    vie = 3
    tr.register_shape("image coeur.gif")

    vie1 = tr.Turtle()
    vie1.speed(0)
    vie1.shape("image coeur.gif")
    vie1.color("yellow")
    vie1.penup()
    vie1.setposition(280, 260)

    vie2 = tr.Turtle()
    vie2.speed(0)
    vie2.shape("image coeur.gif")
    vie2.color("yellow")
    vie2.penup()
    vie2.setposition(250, 260)

    vie3 = tr.Turtle()
    vie3.shape("image coeur.gif")
    vie3.speed(0)
    vie3.color("yellow")
    vie3.penup()
    vie3.setposition(220, 260)

    x_base = -230
    y_base = 200
    briques = []

    tr.register_shape("balle.gif")
    ball = tr.Turtle()
    ball.speed(0)
    ball.shape("balle.gif")
    ball.shapesize(stretch_wid = 0.75, stretch_len = 0.75)
    ball.color("red")
    ball.penup()
    ball.setposition(0,-150)
    ball.dx = -3
    ball.dy = -3

    tr.register_shape("image_barre.gif")
    barre = tr.Turtle()
    barre.speed(0)
    barre.shape("image_barre.gif")
    barre.shapesize(stretch_wid = 0.25, stretch_len=5)
    barre.color("red")
    barre.penup()
    barre.setposition(0,-225)

    for i in range (3):
        briques.append(fabrication_briques(x_base, y_base - i * 35, colors))
    window.update

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
    recommencer()
 
 

def recommencer():
    """ cette fonction permet à l'utilisateur de choisir s'il veut recommencer une partie ou non."""

    rejouer = input("Veux-tu relancer une partie (oui/non) ?")

    if rejouer == 'oui':
        nouvelle_partie()
    else:
        tr.bye()
    

