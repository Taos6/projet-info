"""ce fichier s'occuppe de la création des briques de notre jeu"""

import turtle as tr
import random 

window = tr.Screen()
window.bgcolor("black")
window.setup(width=600, height=600)
window.register_shape("brick", ((0,0), (10,0), (10,50), (0,50)))

colors = ["sky blue", "tomato", "lime green", "yellow"]


def fabrication_briques(x, y, colors):
    """Fonction pour créer une ligne de briques"""
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


# position initiale des briques
x_base = -230
y_base = 200

# liste des lignes de briques
briques = []

#ajout des lignes de briques
for i in range (3):
    briques.append(fabrication_briques(x_base, y_base - i * 35, colors))
window.update
