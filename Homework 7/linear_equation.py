class LinearEquation :
    def __init__(self, a, b, c, d, e, f) :
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
        
    def get_a(self) :
        return self.__a
    
    def get_b(self) :
        return self.__b
    
    def get_c(self) :
        return self.__c
    
    def get_d(self) :
        return self.__d
    
    def get_e(self) :
        return self.__e
    
    def get_f(self) :
        return self.__f
    
    def isSolvable(self) :
        
        if (self.__a * self.__d) - (self.__b * self.__c) == 0 :
            return False
        else :
            return True
        
    def getX(self) :
        
        if self.isSolvable() == True :
            return ((self.__e * self.__d) - (self.__b * self.__f)) / ((self.__a * self.__d) - (self.__b * self.__c))
        elif self.isSolvable() == False :
            return "Cannot find the answer"
        
    def getY(self) :
        
        if self.isSolvable() == True :
            return ((self.__a * self.__f) - (self.__e * self.__c)) / ((self.__a * self.__d) - (self.__b * self.__c))
        elif self.isSolvable() == False :
            return "Cannot find the answer"
        
lineq1 = LinearEquation(1, 2, 1, 4, 5, 6)
a1 = lineq1.get_a()
b1 = lineq1.get_b()
x1 = lineq1.getX()
y1 = lineq1.getY()
print("a of linear equation 1:", a1)
print("b of linear equation 1:", b1)
print("x of linear equation 1:", x1)
print("y of linear equation 1:", y1)

lineq2 = LinearEquation(2, 1, 5, 4, 7, 1)
c2 = lineq2.get_c()
d2 = lineq2.get_d()
x2 = lineq2.getX()
y2 = lineq2.getY()
print("c of linear equation 2:", c2)
print("d of linear equation 2:", d2)
print("x of linear equation 2:", x2)
print("y of linear equation 2:", y2)

lineq3 = LinearEquation(1, 2, 3, 6, 4, 5)
e3 = lineq3.get_e()
f3 = lineq3.get_f()
x3 = lineq3.getX()
y3 = lineq3.getY()
print("e of linear equation 3:", e3)
print("f of linear equation 3:", f3)
print("x of linear equation 3:", x3)
print("y of linear equation 3:", y3)