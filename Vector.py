from math import sin, cos, atan2, pi

def degrees(radians):
    '''
    Converts radians to degrees.
    '''
    return radians * 180 / pi

def radians(degrees):
    '''
    Converts degrees to radians.
    '''
    return degrees * pi / 180

class Vector2():
    '''
    Represents a 2D vector with X and Y axis.
    '''
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        '''
        Return repr(self).
        '''
        return f"Vector2({self.x}, {self.y})"
    
    def lenghtsquared(self):
        '''
        Return the square of this vector's lenght.
        '''
        return self.x**2 + self.y**2
    
    def lenght(self):
        '''
        Return this vector's lenght.
        '''
        return self.lenghtsquared()**0.5
    
    def normalize(self, default=None):
        '''
        Return a vector with equal ratio and a lenght of 1.
        default = Value to return if lenght is 0.
        '''
        if default is None:
            default = Vector2(0, 0)
        lenght = self.lenght()
        if lenght == 0:
            return default
        else:
            newx = self.x / lenght
            newy = self.y / lenght
            return Vector2(newx, newy)
    
    def torotation(self):
        '''
        Return this vector as an angle, in radians.
        0 is up, pi/2 is right.
        '''
        return atan2(self.x, self.y)
    
    def rotatedby(self, angle):
        '''
        Return this vector rotated by a certain angle, in radians.
        Angle growth is clockwise.
        '''
        lenght = self.lenght()
        origangle = self.torotation()
        newx = lenght * sin(origangle + angle)
        newy = lenght * cos(origangle + angle)
        return Vector2(newx, newy)
    
    def bool(self):
        '''
        True if self else False
        '''
        return self is not None
    
    def __add__(self, value):
        '''
        Return self+value
        '''
        return Vector2(self.x + value.x, self.y + value.y)
    
    def __radd__(self, value):
        '''
        Return value+self
        '''
        return Vector2(value.x + self.x, value.y + self.y)
    
    def __sub__(self, value):
        '''
        Return self-value
        '''
        return Vector2(self.x - value.x, self.y - value.y)
    
    def __rsub__(self, value):
        '''
        Return value-self
        '''
        return Vector2(value.x - self.x, value.y - self.y)
    
    def __mul__(self, value):
        '''
        Return self*value
        '''
        if type(value) == type(self):
            return Vector2(self.x * value.x, self.y * value.y)
        else:
            return Vector2(self.x * value, self.y * value)
    
    def __rmul__(self, value):
        '''
        Return value*self
        '''
        if type(value) == type(self):
            return Vector2(value.x * self.x, value.y * self.y)
        else:
            return Vector2(value * self.x, value * self.y)
    
    def __truediv__(self, value):
        '''
        Return self/value
        '''
        if type(value) == type(self):
            return Vector2(self.x / value.x, self.y / value.y)
        else:
            return Vector2(self.x / value, self.y / value)
    
    def __rtruediv__(self, value):
        '''
        Return value/self
        '''
        if type(value) == type(self):
            return Vector2(value.x / self.x, value.y / self.y)
        else:
            return Vector2(value / self.x, value / self.y)

    def __floordiv__(self, value):
        '''
        Return self//value
        '''
        if type(value) == type(self):
            return Vector2(self.x // value.x, self.y // value.y)
        else:
            return Vector2(self.x // value, self.y // value)
        
    def __rfloordiv__(self, value):
        '''
        Return value//self
        '''
        if type(value) == type(self):
            return Vector2(value.x // self.x, value.y // self.y)
        else:
            return Vector2(value // self.x, value // self.y)
    
    def __mod__(self, value):
        '''
        Return self%value
        '''
        if type(value) == type(self):
            return Vector2(self.x % value.x, self.y % value.y)
        else:
            return Vector2(self.x % value, self.y % value)
    
    def __rmod__(self, value):
        '''
        Return value%self
        '''
        if type(value) == type(self):
            return Vector2(value.x % self.x, value.y % self.y)
        else:
            return Vector2(value % self.x, value % self.y)
    
    def __pow__(self, value, mod=None):
        '''
        Return pow(self, value, mod)
        '''
        if type(self) == type(value):
            result = Vector2(self.x ** value.x, self.y ** value.y)
        else:
            result = Vector2(self.x ** value, self.y ** value)
        if mod is None:
            return result
        else:
            return result % mod
        
    def __rpow__(self, value, mod=None):
        '''
        Return pow(self, value, mod)
        '''
        if type(self) == type(value):
            result = Vector2(value.x ** self.x, value.y ** self.y)
        else:
            result = Vector2(value ** self.x, value ** self.y)
        if mod is None:
            return result
        else:
            return result % mod
    
    def __round__(self, ndigits=None):
        '''
        Return a Vector with rounded X and Y values.
        '''
        return Vector2(round(self.x, ndigits), round(self.y, ndigits))
    
    def __pos__(self):
        '''
        +self
        '''
        return self * 1
    
    def __neg__(self):
        '''
        -self
        '''
        return self * (-1)
    
    def __floor__(self):
        '''
        Return a Vector with the floor of X and Y values.
        '''
        new = round(self)
        if new.x > self.x:
            new.x -= 1
        if new.y > self.y:
            new.y -= 1
        return new
    
    def __ceil__(self):
        '''
        Return a Vector with the ceiling of X and Y values.
        '''
        new = round(self)
        if new.x < self.x:
            new.x += 1
        if new.y < self.y:
            new.y += 1
    
    def __eq__(self, value):
        '''
        Return self==value
        '''
        if type(value) != type(self):
            return False
        return self.x == value.x and self.y == value.y
    
    def __ne__(self, value):
        '''
        Return self!=value
        '''
        if type(value) != type(self):
            return True
        return self.x != value.x and self.y != value.y
    
    def __lt__(self, value):
        '''
        Return self<value
        '''
        return self.x < value.x and self.y < value.y
    
    def __le__(self, value):
        '''
        Return self<=value
        '''
        return self == value or self < value
    
    def __gt__(self, value):
        '''
        Return self>value
        '''
        return self.x > value.x and self.y > value.y
    
    def __ge__(self, value):
        '''
        Return self>=value
        '''
        return self > value or self == value
    