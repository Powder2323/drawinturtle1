import turtle

t = turtle.Turtle("turtle")

t.begin_fill()
for i in range(4):
    t.color('yellow')
    t.forward(100)
    t.right(90)
t.end_fill()

t.color('white')
t.left(90)
t.forward(10)
t.right(90)

t.begin_fill()
for i in range(4):
    t.color('red')
    t.left(90)
    t.forward(100)
t.end_fill()

t.color('white')
t.forward(10)

t.begin_fill()
t.left(90)
for i in range(4):
    t.color('green')
    t.forward(100)
    t.right(90)
t.end_fill()

t.color('white')
t.left(90)
t.forward(20)
t.left(90)
t.forward(10)
t.right(180)


t.left(90)
t.begin_fill()
for i in range(4):
    t.color('blue')
    t.forward(100)
    t.left(90)
t.end_fill()

turtle.exitonclick()