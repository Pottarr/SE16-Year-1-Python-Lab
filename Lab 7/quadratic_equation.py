import math

class QuadraticEquation :
    def __init__(self, a, b, c) :
        self.a = a
        self.b = b
        self.c = c
        
    def getDiscriminant(self) :
        if self.b ** 2 - 4 * self.a * self.c >= 0 :
            return self.b ** 2 - 4 * self.a * self.c
        else :
            return 0
        
    def getRoot1(self) :
        if self.a == 0 :
            return "Woah"
        else :
            return (-self.b + math.sqrt(self.getDiscriminant())) / (2 * self.a)
    
    def getRoot2(self) :
        if self.a == 0 :
            return "Woah"
        else :
            return (-self.b - math.sqrt(self.getDiscriminant())) / (2 * self.a)
    
eq1 = QuadraticEquation(1,0,-1)
dis1 = eq1.getDiscriminant()
rt11 = eq1.getRoot1()
rt12 = eq1.getRoot2()

eq2 = QuadraticEquation(0,3,-1)
dis2 = eq2.getDiscriminant()
rt21 = eq2.getRoot1()
rt22 = eq2.getRoot2()

eq3 = QuadraticEquation(1,1,3)
dis3 = eq3.getDiscriminant()
rt31 = eq3.getRoot1()
rt32 = eq3.getRoot2()

print(dis1)
print(rt11)
print(rt12)
print(dis2)
print(rt21)
print(rt22)
print(dis3)
print(rt31)
print(rt32)
