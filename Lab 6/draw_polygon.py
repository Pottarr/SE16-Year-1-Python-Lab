import turtle as t

def draw_polygon(x = 0, y = 0, angles = 4, size = 100) :
    t.goto(x, y)
    t.pendown()
    for i in range(angles) :
        t.forward(size)
        t.left(180 - ((angles - 2) * 180 / angles))
    t.penup()
    
draw_polygon(0, 0)
draw_polygon(10, 10, 5)
draw_polygon(0, 0, 5, 200)

t.exitonclick()
