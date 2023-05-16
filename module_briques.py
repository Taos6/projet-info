window.register_shape("brick", ((0, 0), (10, 0), (10, 50), (0, 50)))

"""couleur des briques"""
colors = ["sky blue", "tomato", "lime green", "yellow"]


"""fonction pour créer les briques"""
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

"""position initiale des briques"""
x_start = -230
y_start = 200


"""liste des lignes de briques"""
briques = []


"""ajout des lignes de briques"""
for i in range(3):
    briques.append(makeRow(x_start, y_start - i * 35, colors))

window.update()