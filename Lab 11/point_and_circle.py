import math

class Point(object) :
    def __init__(self) :
        self.x = 0.00
        self.y = 0.00
        
    def printInfo(self) :
        print("Position:", self.x, ",", self.y)
    
class Circle(Point) :
    def __init__(self) :
        self.radius = 0.00
        
    def area(self) :
        return math.pi * radius * radius
    
    def printInfo() :
        print("Position:", self.x, ",", self.y, "; Radius:", self.radius, "; Area:", self.area())