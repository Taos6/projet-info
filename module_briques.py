screen.register_shape("brick", ((0, 0), (10, 0), (10, 50), (0, 50)))

colors = ["sky blue", "tomato", "lime green", "yellow"]


def makeRow(x, y, colors):
    index = random.randint(0,len(colors) - 1)
    row = []
    
    for i in range(8):
        
        brique = turtle.Turtle()
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

x_start = -230
y_start = 200


briques = []

for i in range(3):
    briques.append(makeRow(x_start, y_start - i * 35, colors))

screen.update()