import turtle as t


def calendar_of_2024(chosen_month):
    block = 50
    main_x = -200
    main_y = 200
    t.speed(0)
    weeks = 6
    days_in_week = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    dates_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = 0
    total_days = 0
    
    month_title = str(months[chosen_month-1] + " 2024")
    
    while month < chosen_month - 1:
        total_days += dates_in_month[month]
        month += 1
    start_col = total_days % 7
    
    t.penup()
    t.goto(main_x, main_y)
    t.pendown()
    for i in range(2) :
        t.forward(7 * block)
        t.right(90)
        t.forward(block)
        t.right(90)
    t.penup()
    #Vertical Line
    for i in range(8) :
        t.goto(main_x + i * block, main_y - block)
        t.pendown()
        t.right(90)
        t.goto(main_x + i * block, main_y - block * (weeks + 2))
        t.penup()
    #Horizontal Line
    for j in range(weeks + 1) :
        t.goto(main_x, main_y - block * (j + 2))
        t.pendown()
        t.forward(7 * block)
        t.penup()
    
    t.goto(main_x + 100, main_y - 40)
    t.pendown()
    t.write(month_title, font=("Arial", 20, "normal"))
    t.penup()
    
    for k in range(7) :
        t.goto(main_x + 8 + k * block, main_y - block - 40)
        t.pendown()
        t.write(days_in_week[k], font=("Arial", 18, "normal"))
        t.penup()    
    
    day = 1
    row = 0
    col = start_col
    while row < 6:
        while col < 7:
            t.goto(main_x + 8 + col * block, main_y - 2 * block - 40 - row * block)
            t.write(str(format(day, "2d")), font=("Arial", 16, "normal"))
            day += 1
            col += 1
            if day > dates_in_month[chosen_month - 1]:
                day = 1
                if col == 7:
                    col = 0
                break
        col = 0
        if day == 1:
            break
        row += 1
    
    
calendar_of_2024(8)
t.hideturtle()
t.exitonclick()