import turtle as t

input_str = input("Enter some text: ")

def find_aphabet_frequency(input_str) :
    chars = []
    for i in input_str :
        if i not in chars :
            chars.append(i)
        else :
            continue
    frequency_list = []
    for j in chars :
        frequency = input_str.count(j)
        frequency_list.append(frequency)
    return (chars, frequency_list)

def draw_graph(result) :
    chars = result[0]
    frequency_list = result[1]
    block = 20
    initial_x = -1 * block * len(chars)
    initial_y = -1 * block * len(frequency_list)
    t1 = t.Turtle()
    t2 = t.Turtle()
    t3 = t.Turtle()
    t4 = t.Turtle()
    t1.penup()
    t2.penup()
    t3.penup()
    t4.penup()
    t1.goto(initial_x, initial_y)
    t2.goto(initial_x, initial_y)
    t3.goto(initial_x, initial_y)
    t4.goto(initial_x, initial_y)
    t1.pendown()
    t2.pendown()
    t3.pendown()
    t1.left(90)
    t1.forward(20 * max(frequency_list))
    t2.forward(20 * (len(chars) + 1) * 3)
    for i in range(len(frequency_list)) :
        t3.forward(2 * block)
        t3.left(90)
        t3.forward(frequency_list[i] * block)
        t3.right(90)
        t3.forward(block)
        t3.right(90)
        t3.forward(frequency_list[i] * block)
        t3.left(90)
    t3.hideturtle()
    t4.right(90)
    t4.forward(block)
    t4.left(90)
    for i in range(len(chars)) :
        t4.forward(2.5 * block)
        t4.write(chars[i])   
        t4.forward(0.5 * block)
    t4.hideturtle()
    

draw_graph(find_aphabet_frequency(input_str))

t.exitonclick()