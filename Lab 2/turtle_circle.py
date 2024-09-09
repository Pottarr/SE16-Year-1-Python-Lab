from turtle import Turtle
from math import pi
t = Turtle()

r = 100
area = pi * r * r

t.circle(r)
t.penup()
t.left(90)
t.forward(r)
t.write(area)
t.ht()
t.screen.mainloop()