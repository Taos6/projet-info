
"""détermine le nombre de briques"""

briques_restantes = len(briques)


"""affiche le message de victoire lorsqu'il n'y a plus de briques """

def potentielle_victoire():
   
    
    if briques_restantes == 0:
        potentielle_victoire = tr.Turtle()
        potentielle_victoire.color("green")
        potentielle_victoire.penup()
        potentielle_victoire.goto(0, 50) # pour afficher le message plus haut  
        potentielle_victoire.write("Bravo tu as gagné ! ", align = "center", font = ("chalkduster", 40, "normal"))
        potentielle_victoire.hideturtle()
                
        
