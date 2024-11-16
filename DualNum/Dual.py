import math

class Dual:
    """
    A class to represent a dual number for use in automatic differentiation.
    
    Attributes
    ----------
    real : float
        The real part of the dual number.
        
    dual : float
        The dual part of the dual number.
        
    Methods
    -------
    __add__(self, other)
        Adds two dual numbers together.
    
    __sub__(self, other)
        Subtracts one dual number from another.

    __mul__(self, other)
        Multiplies two dual numbers together.

    __truediv__(self, other)
        Divides one dual number by another.

    __repr__(self)
        Returns a string representation of the dual number.

    real(self)
        Returns the real part of the dual number.

    dual(self)
        Returns the dual part of the dual number.

    sin(self)
        Returns the sine of the dual number.
    
    cos(self)
        Returns the cosine of the dual number.

    tan(self)
        Returns the tangent of the dual number.

    exp(self)
        Returns the exponential of the dual number.

    log(self)
        Returns the natural logarithm of the dual number.

    sqrt(self)
        Returns the square root of the dual number.
        
    """

    # Special Methods
    def __init__(self, real, dual):
        """
        Constructs all the necessary attributes for the Dual object.
        
        Parameters
        ----------
        
        real : float
            The real part of the dual number.
        
        dual : float
            The dual part of the dual number.
        """
        self.real = real
        self.dual = dual
    
    def __add__(self, other):
        """
        Adds two dual numbers together.

        Parameters
        ----------
        other : Dual
            The dual number to add to the current dual number.
        """
        if isinstance(other, Dual):
            return Dual(self.real + other.real, self.dual + other.dual)
        raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(type(self), type(other)))
    
    def __sub__(self, other):
        """
        Subtracts one dual number from another.

        Parameters
        ----------
        other : Dual
            The dual number to subtract from the current dual number.
        """
        if isinstance(other, Dual):
            return Dual(self.real - other.real, self.dual - other.dual)
        raise TypeError("unsupported operand type(s) for -: '{}' and '{}'".format(type(self), type(other)))
    
    def __mul__(self, other):
        """
        Multiplies two dual numbers together.

        Parameters
        ----------
        other : Dual
            The dual number to multiply with the current dual number.
        """
        if isinstance(other, Dual):
            return Dual(self.real * other.real, self.real * other.dual + self.dual * other.real)
        raise TypeError("unsupported operand type(s) for *: '{}' and '{}'".format(type(self), type(other)))
    
    def __truediv__(self, other):
        """
        Divides one dual number by another.

        Parameters
        ----------
        other : Dual
            The dual number to divide the current dual number by.
        """
        if isinstance(other, Dual):
            return Dual(self.real / other.real, (self.dual * other.real - self.real * other.dual) / (other.real ** 2))
        raise TypeError("unsupported operand type(s) for /: '{}' and '{}'".format(type(self), type(other)))

    def __repr__(self):
        """
        Returns a string representation of the dual number.
        """
        return f'Dual(real={self.real}, dual={self.dual})'
    

    # Class Methods
    def real(self):
        """
        Returns the real part of the dual number.
        """
        return self.real

    def dual(self):
        """
        Returns the dual part of the dual number.
        """
        return self.dual

    def sin(self):
        """
        Returns the sine of the dual number.
        """
        return Dual(math.sin(self.real), self.dual * math.cos(self.real))
    
    def cos(self):
        """
        Returns the cosine of the dual number.
        """
        return Dual(math.cos(self.real), -self.dual * math.sin(self.real))
    
    def tan(self):
        """
        Returns the tangent of the dual number.
        """
        return Dual(math.tan(self.real), self.dual / (math.cos(self.real) ** 2))
    
    def exp(self):
        """
        Returns the exponential of the dual number.
        """
        return Dual(math.exp(self.real), self.dual * math.exp(self.real))
    
    def log(self):
        """
        Returns the natural logarithm of the dual number.
        """
        return Dual(math.log(self.real), self.dual / self.real)
    
    def sqrt(self):
        """
        Returns the square root of the dual number.
        """
        return Dual(math.sqrt(self.real), self.dual / (2 * math.sqrt(self.real)))
    
    


