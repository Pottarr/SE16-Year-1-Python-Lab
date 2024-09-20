import turtle as t

class Rectangle :
    
    def __init__(self, x, y, w, h) :
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        
    def getArea(self) :
        return self.width * self.height
        
    def getPerimeter(self) :
        return self.width * 2 + self.height * 2
    
    def move(self, new_x, new_y) :
        self.x = new_x
        self.y = new_y
    
    def intersect(self, rec):
        self_bottom = self.y - self.height
        self_right = self.x + self.width
        rec_bottom = rec.y - rec.height
        rec_right = rec.x + rec.width
        if not (self.x > rec_right or self_right < rec.x or self.y < rec_bottom or self_bottom > rec.y):
            if self.x > rec.x and self_right < rec_right and self.y < rec.y and self_bottom > rec_bottom:
                return Rectangle(self.x, self.y, self.width, self.height)
            elif self.x < rec.x and self_right > rec_right and self.y > rec.y and self_bottom < rec_bottom:
                return Rectangle(rec.x, rec.y, rec.width, rec.height)
            else:
                if self.x < rec.x:
                    if self.y > rec.y:
                        return Rectangle(rec.x, rec.y, self_right - rec.x, rec.y - self_bottom)
                    else:
                        return Rectangle(rec.x, self.y, self_right - rec.x, self.y - rec_bottom)
                elif self.x > rec.x:
                    if self.y > rec.y:
                        return Rectangle(self.x, rec.y, rec_right - self.x, rec.y - self_bottom)
                    else:
                        return Rectangle(self.x, self.y, rec_right - self.x, self.y - rec_bottom)
                else:
                    if self.y > rec.y:
                        if self.width > rec.width:
                            return Rectangle(rec.x, rec.y, rec.width, rec.y - self_bottom)
                        else:
                            return Rectangle(rec.x, rec.y, self.width, rec.y - self_bottom)
                    else:
                        if self.width > rec.width:
                            return Rectangle(self.x, self.y, rec.width, self.y - rec_bottom)
                        else:
                            return Rectangle(self.x, self.y, self.width, self.y - rec_bottom)
        else:
            return None
        
    def draw(self) :
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        for i in range(2) :
            t.forward(self.width)
            t.right(90)
            t.forward(self.height)
            t.right(90)
            
rec1 = Rectangle(10,10,200,100)
area = rec1.getArea()
perimeter = rec1.getPerimeter()
rec1.draw()
rec1.move(50, 10)
rec1.draw()
rec2 = rec1.intersect(Rectangle(10,10,150,100))
rec2.draw()

print(area)
print(perimeter)
t.exitonclick()