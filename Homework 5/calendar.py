import turtle as t

cell_len = 30
max_tl_x = -500
max_tl_y = 700

t.speed(0)

space_btw_cal = 10*cell_len

cal_tl_x = max_tl_x
cal_tl_y = max_tl_y

cal_bl_x = max_tl_x
cal_bl_y = max_tl_y - 8 * cell_len

month = 1
while month <= 12:

    t.penup()
    
    if month % 4 == 1 :
        cal_tl_y -= space_btw_cal
        cal_tl_x = max_tl_x
    else :
        cal_tl_x += space_btw_cal

    horizon = 1
    while horizon <= 9 :
        t.goto(cal_tl_x, cal_tl_y - ((horizon - 1) * cell_len))
        t.pendown()
        t.forward(7 * cell_len)
        t.penup()
        horizon += 1
 
    if month % 4 == 1 :
        cal_bl_y -= space_btw_cal
        cal_bl_x = max_tl_x
    else :
        cal_bl_x += space_btw_cal
        
    verticle = 1
    t.left(90)
    while verticle <= 8 :
        if verticle == 1 or verticle == 8 :    
            t.goto(cal_bl_x + ((verticle - 1) * cell_len), cal_bl_y)
            t.pendown()
            t.forward(8 * cell_len)
        else :
            t.goto(cal_bl_x + ((verticle - 1) * cell_len), cal_bl_y)
            t.pendown()
            t.forward(7 * cell_len)
        t.penup()
        verticle += 1
    
    t.right(90)
    
    month_title_x = cal_tl_x + 10
    month_title_y = cal_tl_y -25
    
    t.goto(month_title_x, month_title_y)
    t.write("Month#")
    t.forward(35)
    t.write(str(month))
    t.penup()
    
    
    day = 1
    
    days_title_x = month_title_x
    days_title_y = month_title_y - 30
    
    while day <= 7 :
        t.goto(days_title_x + (day - 1) * cell_len, days_title_y)
        if day == 1 :
            t.write("Su")
        if day == 2 :
            t.write("Mo")
        if day == 3 :
            t.write("Tu")
        if day == 4 :
            t.write("We")
        if day == 5 :
            t.write("Th")
        if day == 6 :
            t.write("Fr")
        if day == 7 :
            t.write("Sa")
        day += 1
        
        
        
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 :
        month_days = 31
    elif month == 2 :
        month_days = 29
    else :
        month_days = 30
        
        
    date_x = days_title_x
    date_y = days_title_y - cell_len
        
    date = 1

    while date <= month_days :
        
        if month == 1 :
            calendar_gap = 1
            
        
        week_day = 0
        
        t.penup()
        date_x = days_title_x 
        
        
        
        while week_day >= 0 and date <= month_days :
            
            if date == 1 :
                date_x += cell_len * calendar_gap
                week_day += calendar_gap
            
            if week_day %7 ==  0 :
                date_x = days_title_x
                
            t.goto(date_x, date_y)
            t.write(str(date))
            
            if date == month_days :
                calendar_gap = week_day + 1
            
            
            week_day += 1
            week_day %= 7
            
            if week_day > 0 :
                date_x += cell_len
            else : 
                date_y -= cell_len
                
            date += 1
        
        
        date_y -= cell_len

    month += 1
    
t.hideturtle()
t.exitonclick()