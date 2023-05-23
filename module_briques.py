"""ce fichier s'occuppe de la création des briques de notre jeu"""


import turtle as tr
import random 

tr.register_shape("fond jeu.gif")
window = tr.Screen()
window.bgpic("fond jeu.gif")
window.register_shape("brick", ((0,0), (10,0), (10,50), (0,50)))

couleurs = ["sky blue", "tomato", "lime green", "yellow"]


def fabrication_briques(x, y, colors):
    """Fonction pour créer une ligne de briques"""
    index = random.randint(0,len(couleurs) - 1)
    ligne = []
    for i in range(8):
        
        brique = tr.Turtle()
        brique.speed(0)
        brique.shape("brick")
        brique.color(couleurs[index])
        brique.penup()
        brique.goto(x + 55*i,y)
        brique.pendown()
        ligne.append(brique)
        index = random.randint(0,len(colors) - 1)
    return ligne


# position initiale des briques
position_x = -230
position_y = 200

# liste des lignes de briques
briques = []

#ajout des lignes de briques
for i in range (3):
    briques.append(fabrication_briques(position_x, position_y - i * 35, couleurs))

