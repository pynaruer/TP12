import turtle

def fonction(turtle,l,order):
    if order == 0 :
        turtle.forward(l)
        return
    else :
        l /= 3
        fonction(turtle,l,order-1)
        turtle.left(60)
        fonction(turtle,l,order-1)
        turtle.right(120)
        fonction(turtle,l,order-1)
        turtle.left(60)
        fonction(turtle,l,order-1)

if __name__ == "__main__" :
    turtle.setup(800,400)
    fonction(turtle,300,2)
    turtle.exitonclick()
