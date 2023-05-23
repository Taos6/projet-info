

def restart():
    """ cette fonction permet à l'utilisateur de choisir s'il veut recommencer une partie ou non."""

    rejouer = input("Veux-tu relancer une partie ?")
    return rejouer.lower() == "oui"