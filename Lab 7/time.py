class Time :
    
    def __init__(self,hour,minute,second) :
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def print(self) :
        
        if self.hour // 10 == 0 :
            formated_hour = "0" + str(self.hour)
        else :
            formated_hour= str(self.hour)
        if self.minute // 10 == 0 :
            formated_minute = "0" + str(self.minute)
        else :
            formated_minute = str(self.minute)
        if self.second // 10 == 0 :
            formated_second = "0" + str(self.second)
        else :
            formated_second = str(self.second)
        
        time = formated_hour + ":" + formated_minute + ":" + formated_second + "Hrs."
        print(time)
        
time1 = Time(9,30,0)
time1.print()