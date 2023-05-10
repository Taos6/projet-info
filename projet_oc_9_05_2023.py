import turtle as tr
import random

window = tr.Screen()
window.bgcolor("black")
window.setup(width=600, height=600)


ball = tr.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_wid = 1, stretch_len=1)
ball.color("yellow")
ball.penup()
ball.setposition(0,-150)


def deplacement_aleatoire():
    while True:
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
    
        ball.goto(x,y)
        
        tr.delay(300)
        
        
deplacement_aleatoire()

window.listen()