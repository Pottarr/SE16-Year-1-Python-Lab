import turtle as t

def draw_square(x) :
    for i in range(4) :
        t.left(90)
        t.forward(x)
        
def draw_all_squares(x) :
    for j in range(4) :
        for k in range(4) :
            draw_square((k + 1) * x)
        t.right(90)

draw_all_squares(10)
t.exitonclick()