import math

class Dual:

    # Special Methods
    def __init__(self, real, dual):
        self.real = real
        self.dual = dual
    
    def __add__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real + other.real, self.dual + other.dual)
        raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(type(self), type(other)))
    
    def __sub__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real - other.real, self.dual - other.dual)
        raise TypeError("unsupported operand type(s) for -: '{}' and '{}'".format(type(self), type(other)))
    
    def __mul__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real * other.real, self.real * other.dual + self.dual * other.real)
        raise TypeError("unsupported operand type(s) for *: '{}' and '{}'".format(type(self), type(other)))
    
    def __truediv__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real / other.real, (self.dual * other.real - self.real * other.dual) / (other.real ** 2))
        raise TypeError("unsupported operand type(s) for /: '{}' and '{}'".format(type(self), type(other)))

    def __repr__(self):
        return f'Dual(real={self.real}, dual={self.dual})'
    

    # Class Methods
    def sin(self):
        return Dual(math.sin(self.real), self.dual * math.cos(self.real))
    
    def cos(self):
        return Dual(math.cos(self.real), -self.dual * math.sin(self.real))
    
    def tan(self):
        return Dual(math.tan(self.real), self.dual / (math.cos(self.real) ** 2))
    
    def exp(self):
        return Dual(math.exp(self.real), self.dual * math.exp(self.real))
    
    def log(self):
        return Dual(math.log(self.real), self.dual / self.real)
    
    def sqrt(self):
        return Dual(math.sqrt(self.real), self.dual / (2 * math.sqrt(self.real)))
    
    
    

x = Dual(2,1)
y = Dual(4,2)

print(x)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x.sin())

