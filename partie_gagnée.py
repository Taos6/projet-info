

briques_restantes = len(briques)



def potentielle_victoire():
    global briques_restantes
    if briques_restantes == 0:
        potentielle_victoire = tr.Turtle()
        potentielle_victoire.color("green")
        potentielle_victoire.penup()
        potentielle_victoire.goto(0, 50) # pour afficher le message plus haut  
        potentielle_victoire.write("Bravo tu as gagné ! ", align = "center", font = ("chalkduster", 40, "normal"))
        potentielle_victoire.hideturtle()
                
        