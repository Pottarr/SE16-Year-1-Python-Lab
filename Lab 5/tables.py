from turtle import Turtle

blocks = int(input("Enter number of blocks per role: "))

t = Turtle()

x = 0
y = 0

i = 1
while i <=  blocks + 1:
    t.pendown()
    t.forward(100)
    t.penup()
    t.goto(x, y + i * (100 / blocks))
    i += 1

t.goto(x, y)
t.left(90)

j = 1
while j <= blocks + 1 :
    t.pendown()
    t.forward(100)
    t.penup()
    t.goto(x + j * (100 / blocks), y)
    j += 1


t.screen.mainloop()