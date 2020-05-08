import turtle
from Exercice6 import fonction

def fonction_2(turtle,l,order) :
    for i in range (3):
        fonction(turtle,l,order)
        turtle.right(120)

if __name__ == "__main__" :
    turtle.setup(800,400)
    turtle.tracer(False)
    turtle.hideturtle()
    turtle.color("green")
    fonction_2(turtle,150,3)
    turtle.tracer(True)
    turtle.exitonclick()

