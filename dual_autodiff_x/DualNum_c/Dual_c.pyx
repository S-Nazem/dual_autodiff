import math

class Dual_c:
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

    sinh(self)
        Returns the hyperbolic sine of the dual number.
    
    cosh(self)
        Returns the hyperbolic cosine of the dual number.
    
    tanh(self)
        Returns the hyperbolic tangent of the dual number.

    asin(self)
        Returns the arcsine of the dual number.

    acos(self)
        Returns the arccosine of the dual number.

    atan(self)
        Returns the arctangent of the dual number.
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

        Raises
        ------
        TypeError
            If 'real' or 'dual' is not of type float or int.
        """
        if not isinstance(real, (float, int)):
            raise TypeError(f"Expected 'real' to be of type float or int, got {type(real).__name__} instead.")
    
        if not isinstance(dual, (float, int)):
            raise TypeError(f"Expected 'dual' to be of type float or int, got {type(dual).__name__} instead.")
    
        self.real = real
        self.dual = dual
    
    def __add__(self, other):
        """
        Adds two dual numbers together.

        Parameters
        ----------
        other : Dual_c
            The dual number to add to the current dual number.
        """
        if isinstance(other, Dual_c):
            return Dual_c(self.real + other.real, self.dual + other.dual)
        raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(type(self), type(other)))
    
    def __sub__(self, other):
        """
        Subtracts one dual number from another.

        Parameters
        ----------
        other : Dual_c
            The dual number to subtract from the current dual number.
        """
        if isinstance(other, Dual_c):
            return Dual_c(self.real - other.real, self.dual - other.dual)
        raise TypeError("unsupported operand type(s) for -: '{}' and '{}'".format(type(self), type(other)))
    
    def __mul__(self, other):
        """
        Multiplies two dual numbers together.

        Parameters
        ----------
        other : Dual_c
            The dual number to multiply with the current dual number.
        """
        if isinstance(other, Dual_c):
            return Dual_c(self.real * other.real, self.real * other.dual + self.dual * other.real)
        raise TypeError("unsupported operand type(s) for *: '{}' and '{}'".format(type(self), type(other)))
    
    def __truediv__(self, other):
        """
        Divides one dual number by another.

        Parameters
        ----------
        other : Dual_c
            The dual number to divide the current dual number by.
        """
        if isinstance(other, Dual_c):
            return Dual_c(self.real / other.real, (self.dual * other.real - self.real * other.dual) / (other.real ** 2))
        raise TypeError("unsupported operand type(s) for /: '{}' and '{}'".format(type(self), type(other)))
    
    def __pow__(self, other):
        """
        Raises the dual number to the power of another dual number.

        Parameters
        ----------
        other : Dual_c
            The dual number to raise the current dual number to the power of.
        """
        if isinstance(other, Dual_c):
            return Dual_c(self.real ** other.real, self.real ** other.real * (other.dual * math.log(self.real) + other.real * self.dual / self.real))
        raise TypeError("unsupported operand type(s) for **: '{}' and '{}'".format(type(self), type(other)))

    def __eq__(self, other):
        """
        Checks if two dual numbers are equal.

        Parameters
        ----------
        other : Dual_c
            The dual number to compare with the current dual number.
        """
        if isinstance(other, Dual_c):
            return self.real == other.real and self.dual == other.dual
        return False
    


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
        return Dual_c(math.sin(self.real), self.dual * math.cos(self.real))
    
    def cos(self):
        """
        Returns the cosine of the dual number.
        """
        return Dual_c(math.cos(self.real), -self.dual * math.sin(self.real))
    
    def tan(self):
        """
        Returns the tangent of the dual number.
        """
        return Dual_c(math.tan(self.real), self.dual / (math.cos(self.real) ** 2))
    
    def exp(self):
        """
        Returns the exponential of the dual number.
        """
        return Dual_c(math.exp(self.real), self.dual * math.exp(self.real))
    
    def log(self):
        """
        Returns the natural logarithm of the dual number.
        """
        if self.real <= 0:
            raise ValueError("Logarithm of a non-positive number is undefined.")
        return Dual_c(math.log(self.real), self.dual / self.real)
    
    def sqrt(self):
        """
        Returns the square root of the dual number.
        """
        return Dual_c(math.sqrt(self.real), self.dual / (2 * math.sqrt(self.real)))
    
    def sinh(self):
        """
        Returns the hyperbolic sine of the dual number.
        """
        return Dual_c(math.sinh(self.real), self.dual * math.cosh(self.real))

    def cosh(self):
        """
        Returns the hyperbolic cosine of the dual number.
        """
        return Dual_c(math.cosh(self.real), self.dual * math.sinh(self.real))
    
    def tanh(self):
        """
        Returns the hyperbolic tangent of the dual number.
        """
        return Dual_c(math.tanh(self.real), self.dual / (math.cosh(self.real) ** 2))
    
    def asin(self):
        """
        Returns the arcsine of the dual number.
        """
        return Dual_c(math.asin(self.real), self.dual / math.sqrt(1 - self.real ** 2))
    
    def acos(self):
        """
        Returns the arccosine of the dual number.
        """
        return Dual_c(math.acos(self.real), -self.dual / math.sqrt(1 - self.real ** 2))
    
    def atan(self):
        """
        Returns the arctangent of the dual number.
        """
        return Dual_c(math.atan(self.real), self.dual / (1 + self.real ** 2))