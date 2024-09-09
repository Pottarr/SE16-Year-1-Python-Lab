from turtle import Turtle

p1_x = int(input("Enter x-coordinate of the first point: "))
p1_y = int(input("Enter y-coordinate of the first point: "))
p2_x = int(input("Enter x-coordinate of the second point: "))
p2_y = int(input("Enter y-coordinate of the second point: "))
p3_x = int(input("Enter x-coordinate of the third point: "))
p3_y = int(input("Enter y-coordinate of the third point: "))

if (p3_x - p1_x == 0) and (p3_y - p1_y != 0) :
    if p2_x < p1_x :
        print("Left")
    elif p2_x > p1_x :
        print("Right")
    elif p2_x == p1_x :
        print("Between 2 points")
    else : 
        print("Error")
elif (p3_y - p1_y == 0) and (p3_x - p1_x != 0) :
    if p2_y > p1_y :
        print("Left (Top)")
    elif p2_y < p1_y :
        print("Right (Bottom)")
    elif p2_y == p1_y :
        print("Between 2 points")
    else : 
        print("Error")
elif (p3_x - p1_x) / (p3_y - p1_y) > 0 :
    c1 = p1_y - ((p3_x - p1_x) / (p3_y - p1_y) * p1_x)
    pz1_y = ((p3_x - p1_x) / (p3_y - p1_y) * p2_x) + c1
    if p2_y > pz1_y :
        print("Left")
    elif p2_y < pz1_y :
        print("Right")
    elif p2_y == pz1_y:
        print("Between 2 points")
    else :
        print("Error")
elif (p3_x - p1_x) / (p3_y - p1_y) < 0 :
    c2 = p3_y - ((p3_x - p1_x) / (p3_y - p1_y) * p3_x)
    pz2_y = ((p3_x - p1_x) / (p3_y - p1_y) * p2_x) + c2
    if p2_y < pz2_y :
        print("Left")
    elif p2_y > pz2_y :
        print("Right")
    elif p2_y == pz2_y :
        print("Between 2 points")
    else : 
        print("Error")
else :
    print("Error")
t = Turtle()

t.penup()
t.goto(p1_x, p1_y)
t.write("P0")
t.pendown()
t.goto(p3_x, p3_y)
t.write("P2")
t.penup()
t.goto(p2_x, p2_y)
t.write("P1")
t.hideturtle()
t.screen.mainloop()