import turtle


t = turtle.Turtle()
t.hideturtle()
t.color('red')
t.begin_fill()
for i in range(4):
    if i%2==0:
        t.forward(100)
    else:
        t.forward(200)
    t.right(90)
t.end_fill()
t.color('yellow')
t.right(180)
t.begin_fill()
for i in range(4):
    if i%2==0:
        t.forward(100)
    else:
        t.forward(200)
    t.left(90)
t.end_fill()
t.forward(100)
t.color('blue')
t.begin_fill()
for i in range(4):
    if i%2==0:
        t.forward(100)
    else:
        t.forward(200)
    t.left(90)
t.end_fill()

turtle.exitonclick()