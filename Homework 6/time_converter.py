def time24hourTo12hour(time_24) :
    hour = ""
    suffix = ""
    for i in time_24 :
        
        if i == ":" :
            break
        else :
            hour = hour + i
            
    if int(hour) // 2 == 0 :
        suffix = "AM"
    else : 
        suffix = "PM"
        
    if int(hour) % 24 == 0 :
        hour_12 = "12"
    else :
        hour_12 = int(hour) % 12
    approach_colon = False
    minute = ""
    for i in time_24 :
        if i == ":" :
            approach_colon = True
        if approach_colon == True :
            minute = minute + i
    return str(hour_12) + str(minute) + suffix

time_12_1124pm = time24hourTo12hour("23:24")
time_12_1234am = time24hourTo12hour("00:34")
time_12_0330pm = time24hourTo12hour("15:30")

print("We can convert from 23:24 to", time_12_1124pm)
print("We can convert from 00:34 to", time_12_1234am)
print("We can convert from 15:30 to", time_12_0330pm)