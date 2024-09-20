import math
import turtle as t

class Circle :
    def __init__(self, x, y, r) :
        self.x = x
        self.y = y
        self.radius = r
    
    def getArea(self) :
        return math.pi * self.radius * self.radius
    
    def getPerimeter(self) :
        return 2 * math.pi * self.radius
    
    def move(self, new_x, new_y) :
        self.x = new_x
        self.y = new_y
    
    def draw(self) :
        t.penup()
        t.goto(self.x, self.y - self.radius)
        
        t.pendown()
        t.circle(self.radius)
        


c1 = Circle(20,10,50)
c1.draw()
c1.move(100,50)
c1.draw()
area = c1.getArea()
perimeter = c1.getPerimeter()
print(area)
print(perimeter)
t.exitonclick()
    