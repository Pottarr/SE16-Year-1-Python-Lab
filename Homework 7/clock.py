class Clock :
    def __init__(self) :
        self.hour = 0
        self.minute = 0
        self.second = 0
        
    def set_time(self, hour, minute, second) :
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def get_time(self) :
        
        
        if len(str(self.hour % 12)) == 1 :
            hour_12 = "0" + str(self.hour % 12)
            if hour_12 == "00" :
                hour_12 = "12"
        else :
            hour_12 = str(self.hour % 12)
            
        if len(str(self.minute)) == 1 :
            minute_12 = "0" + str(self.minute)
        else :
            minute_12 = str(self.minute)
        
        if len(str(self.second)) == 1 :
            second_12 = "0" + str(self.second)
        else :
            second_12 = str(self.second)
                    
        if self.hour % 24 >= 12 :
            suffix = "PM"
        else :
            suffix = "AM"
            
        time_12 = hour_12 + ":" + minute_12 + ":" + second_12 + suffix
        
        return time_12
        
    def tick(self, tick_second) :
        self.second += tick_second
        if self.second >= 60 :
            tick_minute = self.second // 60
            self.second -= 60 * tick_minute
            self.minute += tick_minute
        if self.minute >= 60 :
            tick_hour = self.minute // 60
            self.minute -= 60 * tick_hour
            self.hour += tick_hour
        if self.hour >= 24 :
            tick_day = self.hour // 24
            self.hour -= 24 * tick_day
    
    def display_time(self) :
        time_12 = self.get_time()
        print(time_12)
            
            
        
clock = Clock()
clock.set_time(23, 4, 11)
clock.display_time()
clock.tick(1234)
clock.display_time()
clock.tick(3600)
clock.display_time()
clock.tick(12345)
clock.display_time()