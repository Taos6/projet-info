import turtle as tr
import time

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

vie = 3

carre1 = tr.Turtle()
carre1.speed(0)
carre1.shape("square")
carre1.shapesize(stretch_wid=0.5, stretch_len=0.5)
carre1.color("yellow")
carre1.penup()
carre1.setposition(280, 260)

carre2 = tr.Turtle()
carre2.speed(0)
carre2.shape("square")
carre2.shapesize(stretch_wid=0.5, stretch_len=0.5)
carre2.color("yellow")
carre2.penup()
carre2.setposition(250, 260)

carre3 = tr.Turtle()
carre3.speed(0)
carre3.shape("square")
carre3.shapesize(stretch_wid=0.5, stretch_len=0.5)
carre3.color("yellow")
carre3.penup()
carre3.setposition(220, 260)


def nb_vie():
    vies_text = tr.Turtle()
    vies_text.speed(0)
    vies_text.color("white")
    vies_text.penup()
    vies_text.setposition(280, 280)
    vies_text.write("Vous avez 3 vies et les carrés représentent le nombre de vies restants", align="right", font=("Goudy Old Style", 15, "normal"))
    vies_text.hideturtle()
    
def game_over_text():
    game_over_text = tr.Turtle()
    game_over_text.color("red")
    game_over_text.penup()
    game_over_text.goto(0, 50) # pour afficher le message plus haut  
    game_over_text.write("Game Over :/", align = "center", font = ("chalkduster", 40, "normal"))
    game_over_text.hideturtle()
    

def text_restart_game():
    text_restart_text = tr.Turtle()
    text_restart_text.color("white")
    text_restart_text.penup()
    text_restart_text.goto(0, -50) # pour afficher le message plus bas
    text_restart_text.write("Appuyer sur une B pour recommencer", align = "center", font = ("chalkduster", 20, "normal"))
    text_restart_text.hideturtle()
    
    
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


def game_over():
    ball.dx = 0
    ball.dy = 0
    ball.clear()
    game_over_text()
    text_restart_game()
   
   
nb_vie()


while True:
    window.update()
    deplacement_balle()

    
    if ball.ycor() < -280:
        if vie > 0:
            vie -= 1
            ball.goto(0, -150)
            ball.dy = -1
        if vie == 2:
            carre3.hideturtle()
            time.sleep(2)
        elif vie == 1:
            carre2.hideturtle()
            time.sleep(2)
        else:
            carre1.hideturtle()
            game_over()