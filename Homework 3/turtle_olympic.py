from turtle import Turtle
t = Turtle()
r = 100

t.pensize(10)
t.penup()
t.left(180)
t.forward(r*2)
t.left(180)

t.pendown()
t.pencolor("#0081C8")
t.circle(r)
t.penup()

t.forward(r*2.25)
t.pendown()
t.pencolor("#000000")
t.circle(r)
t.penup()

t.forward(r*2.25)
t.pendown()
t.pencolor("#EE334E")
t.circle(r)
t.penup()

t.right(120)
t.forward(r/2)
t.left(180)
t.pendown()
t.color("#00A651")
t.circle(r)
t.penup()

t.left(120)
t.forward(r*2.25)
t.right(120)
t.pendown()
t.color("#FCB131")
t.circle(r)
t.hideturtle()
t.screen.mainloop()