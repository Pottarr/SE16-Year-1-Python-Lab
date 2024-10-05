from turtle import *
from random import *

t = Turtle()
def pie_chart(num_list) :

    nums = []

    for i in num_list :
        if i not in nums :
            nums.append(i)
        else :
            continue
        
    nums.sort()
        
    data = [[i] for i in nums]

    for j in range(len(data)) :
        frequency = num_list.count(data[j][0])
        data[j].append(frequency)      
    
    total_freq = 0
    for f in data :
        total_freq += f[1]
    
    colors = [ "#cccccc", "#2740c6", "#e6db74", "#6cd4ff", "#5ead6f", "#f5a2e6", "#c41a14", "#c15bcf", "#e88809", "#5b0870" ]
    
    r = 100
        
    
    t.pencolor("black")
    t.left(90)
    t.forward(r)
    t.left(90)
    
    for i in range(len(data)) :
        t.pendown()
        t.fillcolor(colors[i])
        t.begin_fill()
        t.circle(r, 360 * data[i][1] / total_freq)
        t.left(90)
        t.forward(r)
        t.end_fill()
        t.left(180)
        t.forward(r)
        t.left(90)
    t.hideturtle()
    
pie_chart([3, 1, 3, 3, 2, 3, 3, 2, 3, 2, 4, 3, 3, 3, 3, 4, 3, 4, 3, 3, 3, 4, 3])
exitonclick()
