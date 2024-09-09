from turtle import Turtle

rect1_x = int(input("Enter center x-coordinate of Rectangle 1: "))
rect1_y = int(input("Enter center y-coordinate of Rectangle 1: "))

rect1_w = int(input("Enter width of Rectangle 1: "))
rect1_h = int(input("Enter height of Rectangle 1: "))

rect2_x = int(input("Enter center x-coordinate of Rectangle 2: "))
rect2_y = int(input("Enter center y-coordinate of Rectangle 2: "))

rect2_w = int(input("Enter width of Rectangle 2: "))
rect2_h = int(input("Enter height of Rectangle 2: "))

rect1_top = rect1_y + rect1_h/2
rect1_bottom = rect1_y - rect1_h/2
rect1_left = rect1_x - rect1_w/2
rect1_right = rect1_x + rect1_w/2

rect2_top = rect2_y + rect2_h/2
rect2_bottom = rect2_y - rect2_h/2
rect2_left = rect2_x - rect2_w/2
rect2_right = rect2_x + rect2_w/2

top_touch_bottom = rect1_top == rect2_top or rect1_bottom == rect2_top
left_touch_right = rect1_left == rect2_right or rect1_right == rect2_left
rect_touch = top_touch_bottom or left_touch_right

same_rect = rect1_top == rect2_top and rect1_bottom == rect2_bottom and rect1_left == rect2_left and rect1_right == rect2_right

rect1_inside_rect2 = rect1_top < rect2_top and rect1_bottom > rect2_bottom and rect1_left  > rect2_left and rect1_right < rect2_right
rect2_inside_rect1 = rect1_top > rect2_top and rect1_bottom < rect2_bottom and rect1_left  < rect2_left and rect1_right > rect2_right

top_overlap_bottom = ((rect1_top > rect2_bottom) and (rect1_bottom < rect2_top)) or ((rect1_bottom < rect2_top) and (rect1_top > rect2_bottom))
left_overlap_right = ((rect1_left < rect2_right) and (rect1_right > rect2_left)) or ((rect1_right > rect2_left) and (rect1_left < rect2_right))

rect_overlap = top_overlap_bottom or left_overlap_right

if same_rect :
    print("Overlap (Same rectangle in same position)")
elif rect_touch :
    print("Overlap (Touch)")
elif rect1_inside_rect2 :
    print("Rectangle 1 is inside Rectangle 2")
elif rect2_inside_rect1 :
    print("Rectangle 2 is inside Rectangle 1")
elif rect_overlap :
    print("2 Rectanlgles Overlapping")
else :
    print("Error")
t = Turtle()

t.penup()
t.goto(rect1_x,rect1_y)
t.write("(" + str(rect1_x) + "," + str(rect1_y) + ")")
t.forward(rect1_w/2)
t.pendown()
t.right(90)
t.forward(rect1_h/2)
t.right(90)
t.forward(rect1_w)
t.right(90)
t.forward(rect1_h)
t.right(90)
t.forward(rect1_w)
t.right(90)
t.forward(rect1_h/2)

t.penup()

t.goto(rect2_x,rect2_y)
t.write("(" + str(rect2_x) + "," + str(rect2_y) + ")")
t.left(90)
t.forward(rect2_w/2)
t.pendown()
t.right(90)
t.forward(rect2_h/2)
t.right(90)
t.forward(rect2_w)
t.right(90)
t.forward(rect2_h)
t.right(90)
t.forward(rect2_w)
t.right(90)
t.forward(rect2_h/2)
t.penup()

t.hideturtle()
t.screen.mainloop()

