import turtle as tr

window = tr.Screen()
window.bgcolor("black")
window.setup(width=600, height=600)


barre = tr.Turtle()
barre.speed(0)
barre.shape("square")
barre.shapesize(stretch_wid = 1, stretch_len=5)
barre.color("red")
barre.penup()
barre.setposition(0,-225)

ball = tr.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_wid = 1.5, stretch_len = 1.5)
ball.color("red")
ball.penup()
ball.setposition(0,-150)
ball.dx = -2
ball.dy = -2

def aller_droite():
    x = barre.xcor()
    x += 20
    barre.setx(x)

window.listen()
window.onkeypress(aller_droite,"d")

    
def aller_gauche():
    x = barre.xcor()
    x -= 20
    barre.setx(x)

window.listen()
window.onkeypress(aller_gauche,"a")


def deplacement_balle():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
        
    if ball.xcor() > 280:     # Rebond à droite
        ball.dx *= -1
    elif ball.xcor() < -280:  # Rebond à gauche
        ball.dx *= -1
    elif ball.ycor() > 280:   # Rebond en haut
        ball.dy *= -1
    elif ball.ycor() < -280:  # Rebond en bas
        ball.dy *= -1


while True:
    window.update()
    deplacement_balle()
