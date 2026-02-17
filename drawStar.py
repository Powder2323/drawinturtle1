import turtle

t = turtle.Turtle('turtle')

t.color('red')
t.fillcolor('yellow')

t.begin_fill()

t.right(30)
t.forward(100)
t.left(150)
t.forward(100)
t.right(90)
t.forward(100)
t.left(90+60)
t.forward(100)
t.right(75)
t.forward(100)
t.left(75+75)
t.forward(100)
t.right(75)
t.forward(100)
t.right(360-150)
t.forward(100)
t.right(90)
t.forward(100)
t.left(150)
t.forward(105)

t.end_fill()
t.hideturtle()


turtle.exitonclick()