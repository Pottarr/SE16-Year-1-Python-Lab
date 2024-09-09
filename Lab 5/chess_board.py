import turtle as t

try:
    n = int(input("Enter the number of rows and columns: "))
except:
    print("Please input a valid integer")
else:
    if n > 0:
        spaces = 100 / n

        t.speed(50)
        for rows in range(n):
            t.penup()
            t.goto(0, spaces * rows)
            t.pendown()
            if rows % 2 == 0:
                for columns in range(n):
                    if columns % 2 == 0:
                        t.fillcolor("black")
                        t.begin_fill()
                        for block in range(4):
                            t.forward(spaces)
                            t.right(90)
                        t.end_fill()
                    else:
                        t.fillcolor("white")
                        t.begin_fill()
                        for block in range(4):
                            t.forward(spaces)
                            t.right(90)
                        t.end_fill()
                    t.forward(spaces)       
            else:
                for columns in range(n):
                    if columns % 2 == 0:
                        t.fillcolor("white")
                        t.begin_fill()
                        for block in range(4):
                            t.forward(spaces)
                            t.right(90)
                        t.end_fill()
                    else:
                        t.fillcolor("black")
                        t.begin_fill()
                        for block in range(4):
                            t.forward(spaces)
                            t.right(90)
                        t.end_fill()
                    t.forward(spaces)
        t.exitonclick()
    else:
        print("Please input a positive integer")