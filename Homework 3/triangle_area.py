from turtle import Turtle
t = Turtle()

point1_x = int(input("Enter the X coordinate of Point 1: "))
point1_y = int(input("Enter the Y coordinate of Point 1: "))
point2_x = int(input("Enter the X coordinate of Point 2: "))
point2_y = int(input("Enter the Y coordinate of Point 2: "))
point3_x = int(input("Enter the X coordinate of Point 3: "))
point3_y = int(input("Enter the Y coordinate of Point 3: "))

t.penup()
t.goto(point1_x,point1_y)
t.pendown()
t.goto(point2_x,point2_y)
t.goto(point3_x,point3_y)
t.goto(point1_x,point1_y)
t.penup()

min_x = min(point1_x,point2_x,point3_x)
min_y = min(point1_y,point2_y,point3_y)
area = str(abs(point1_x * (point2_y - point3_y) + point2_x * (point1_y - point3_y) + point3_x * (point1_y - point2_y)) / 2)

t.goto(min_x,min_y-50)
t.write("Area:" + area)
t.ht()
t.screen.mainloop()