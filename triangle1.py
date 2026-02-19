import turtle

t = turtle.Turtle('turtle')

t.hideturtle()
t.penup()
t.goto(200, -200)
t.pendown()
t.showturtle()
t.speed(10)
n = 0
t.fillcolor('red')
while n<=400:
    t.begin_fill()
    for i in range(3):
        t.left(120)
        t.forward(n)
    n = n + 20
    t.end_fill()

turtle.exitonclick()