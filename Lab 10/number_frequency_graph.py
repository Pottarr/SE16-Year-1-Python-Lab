from turtle import *

def find_number_frequency(num_list) :
    nums = []
    for i in num_list :
        if i not in nums :
            nums.append(i)
        else :
            continue
        
        
    for i in range(1, len(nums)) :
        currect_num = nums[i]
        k = i -1
        while k >= 0 and nums[k] > currect_num :
            nums[k+1] = nums[k]
            k -= 1
            
            nums[k+1] = currect_num
            
            
    frequency_list = []
    for j in nums :
        frequency = num_list.count(j)
        frequency_list.append(frequency)

        
        
    block = 20
    initial_x = -1 * block * len(nums)
    initial_y = -1 * block * len(frequency_list)
    t1 = Turtle()
    t2 = Turtle()
    t3 = Turtle()
    t4 = Turtle()
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
    t2.forward(20 * (len(nums) + 2.5))
    t3.forward(block)
    for i in range(len(frequency_list)) :
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
    t4.forward(block)
    for i in range(len(nums)) :
        t4.forward(0.5 * block)
        t4.write(nums[i])   
        t4.forward(0.5 * block)
    t4.hideturtle()
    
find_number_frequency([1, 2, 2, 1, 3, 4, 6, 5, 3, 4, 5, 6, 4, 3, 5, 4, 5, 3, 4, 4, 3, 3, 4, 3, 3, 4, 4, 4])

exitonclick()