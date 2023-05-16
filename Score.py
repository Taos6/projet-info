import turtle as tr

window = tr.Screen()
window.bgcolor("black")
window.setup(width=600, height=600)

score = 0


def final_score():
    score_text = tr.Turtle()
    score_text.speed(0)
    score_text.color("white")
    score_text.penup()
    score_text.hideturtle()
    score_text.goto(-270, 280)
    score_text.write("Score: {}".format(score), align="center", font=("Courier", 12, "normal"))

final_score()

def augmentation_score():
    score = 0
    if brique_disparait:
        brique.supprime(briques)
    score += 100
    score_texte.clear()
    score_text.write("Score: {}".format(score), align="center", font=("Courier", 12, "normal"))
    

augmentation_score()
    