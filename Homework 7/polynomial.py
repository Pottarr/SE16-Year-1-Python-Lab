class Poly :
    def __init__(self, x) :
        self.x = x

    def adjust(self) :
        self_x = list(self.x)
        for i in range(len(self.x) - 1, 0, -1) :
            if self_x[i] == 0 :
                self_x.pop()
            else :
                break
        self.x = tuple(self_x)
    
    def add(self, p) :
        self_x = list(self.x)
        p_x = list(p.x)
        if len(self_x) < len(p_x) :
            for i in range(len(p_x) - len(self_x)) :
                self_x.append(0)
        elif len(self_x) > len(p_x) :
            for i in range(len(self_x) - len(p_x)) :
                p_x.append(0)  
                
        new_self_x = []        
        for i in range(len(self_x)) :
            self_x[i] += p_x[i]
            new_self_x.append(self_x[i])
        return Poly(tuple(new_self_x))

    def scalar_multiply(self, n) :
        self_x = list(self.x)
        new_self_x = []
        for i in range(len(self_x)) :
            self_x[i] *= n
            new_self_x.append(self_x[i])
        return Poly(tuple(new_self_x))
            
    def multiply(self, p) :
        self_x = list(self.x)
        p_x = list(p.x)
        
        init_result = []
        for i in range(len(self_x) + len(p_x) - 1) :
            init_result.append(0)
            
        result = Poly(tuple(init_result))
        
        if len(self_x) < len(p_x) :
            for i in range(len(p_x) - len(self_x)) :
                self_x.append(0)
        elif len(self_x) > len(p_x) :
            for i in range(len(self_x) - len(p_x)) :
                p_x.append(0) 
                     
        new_self_x = []
        for i in range(len(self_x)) :
            new_self_x_term = []
            for j in range(i) :
                new_self_x_term.append(0)
            for j in range(len(self_x)) :
                product = self_x[i] * p_x[j]
                new_self_x_term.append(product)
            for j in range(len(self_x) - i - 1) :
                new_self_x_term.append(0)
            new_self_x.append(new_self_x_term)
            
            result = result.add(Poly(tuple(new_self_x_term)))
            result.adjust()
            
        return result

        
    def power(self, n) :
        result = Poly((1,0))
        base = self
        
        for i in range(n) :
            result = result.multiply(base)
        return result
            
            
        
    def diff(self) :
        self_x = list(self.x)
        for i in range(len(self_x)) :
            self_x[i] *= i
        expo_down = self_x.pop(0)
        
        return Poly(tuple(self_x))
        
    def integrate(self) :
        self_x = list(self.x)
        self_x.insert(0, 0)
        for i in range(len(self_x)) :
            if i == 0 :
                self_x[0] == 0
                continue
            self_x[i] /= i
            
        return Poly(tuple(self_x))
            
            
    def eval(self, n) :
        self_x = list(self.x)
        result = 0
        for i in range(len(self_x)):
            result += self_x[i] * n ** i
        print(result)
            
    def print(self) :
        self_x = list(self.x)
        for i in range(len(self_x)) :
            if i == 0 :
                if self_x[0] != 0 :
                    print(self_x[0], " + ", end="")
                    continue
                continue
            if self_x[i] == 0 :
                continue
            else :
                if i == 1 :
                    print("x", end="")
                    if 1 != len(self_x ) - 1 :
                        print(" + ", end="")
                        continue
                    continue
                print(self_x[i], end="")
                var = "x^" + str(i)
                print(var, end="")
                if i == len(self_x) - 1 :
                    break
                print(" + ", end="")
        print()
            
p = Poly((1, 0, -2))
p.print()
q = p.power(2)
q.print()
p.eval(3)
r = p.add(q)
r.print()
r.diff().print()