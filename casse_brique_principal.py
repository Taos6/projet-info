import turtle as tr
import game_over as over
import creation_mouvement_balle as move_balle
import creation_mouvement_barre as move_barre
import creation_coeur as coeur
import collision_balle_barre as collision1
import module_briques as brik


window = tr.Screen()
window.bgcolor("black")
window.setup(width=600, height=600)

coeur.nb_vie()

while True:
    window.update()
    move_balle.deplacement_balle()
    collision1.collision_barre()
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
        
def makeRow(x, y, colors):
    index = random.randint(0,len(colors) - 1)
    row = []
    
    for i in range(8):
        
        brique = tr.Turtle()
        brique.speed(0)
        brique.shape("brick")
        brique.color(colors[index])
        brique.penup()
        brique.goto(x + 55*i,y)
        brique.pendown()
        row.append(brique)
        index = random.randint(0,len(colors) - 1)
    return row
makeRow(-230,230,colors)

x_base = -230
y_base = 200

briques = []

for i in range (3):
    briques.append(makeRow(x_base, y_base - i * 35, colors))
window.update

