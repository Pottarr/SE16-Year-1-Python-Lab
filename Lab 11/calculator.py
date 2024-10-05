import math

class Calculaotr(object) :
    def __init__(self) :
        super().__init__()
        self.acc = 0.00
        
    def set_accumulator(self, a) :
        self.acc = a
        
    def get_accumulator(self) :
        return self.acc
    
    def add(self, x) :
        self.acc += x
        
    def subtract(self, x) :
        self.acc -= x
        
    def multiply(self, x) :
        self.acc *= x

    def divide(self, x) :
        self.acc /= x
        
    def print_result(self) :
        print("Result:", self.acc)
        
class Sci_calc(Calculaotr) :
    def __init__(self) :
        super().__init__()
        
    def square(self) :
        self.acc *= self.acc
        
    def exp(self, x) :
        self.acc = pow(self.acc, x)
        
    def factorial(self) :
        self.acc = math.factorial(self.acc)
                
    def print_result(self) :
        print("Result:", acc)