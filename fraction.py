def mlt(nums):
    result = 1
    for num in nums:
        result *= num
    return result

def common(a, b):
    tings = []
    for item in a:
        if item in b:
            tings.append(item)
    return tings

def mmc(nums):
    mults = []
    for x in nums:
        while nums.count(x) > 1:
            nums.remove(x)
    mul = mlt(nums)
    for num in nums:
        mult = []
        x = 0
        while x*num < mul:
            x += 1
            mult.append(x*num)
        mults.append(mult)
    curr = mults[0]
    for mult in mults[1:]:
        curr = common(curr, mult)
    if len(curr) == 0:
        return mul
    return min(curr)

def mindiv(nums):
    div = 1
    i = 2
    while div == 1 and i <= min(nums):
        mods = []
        for x in nums:
            mods.append(x%i)
        if sum(mods) == 0:
            div = i
        i += 1
    return div

class Fraction():
    '''
    Convert an integer or floating point number to a fraction, composed of a numerator and a denominator.
    If no denominator is given, one will be automatically calculated.
    '''
    
    def __init__(self, num, den=1):
        if not den.is_integer() and type(den) != Fraction:
            den = Fraction(den)
        if not num.is_integer() and type(num) != Fraction:
            newnum = 0.1
            mult = 0
            while not newnum.is_integer():
                mult += 1
                newnum = num*(10**mult)
            num = Fraction(int(newnum), 10**mult)
        if den == 1 and type(den) != Fraction and type(num) == Fraction:
            den = num.den
            num = num.num
        if type(num) == float and num.is_integer():
            num = int(num)
        if type(den) == float and den.is_integer():
            den = int(den)
        self.num = num
        self.den = den
    
    def __repr__(self):
        '''
        Return repr(self)
        '''
        return f"({self.num}/{self.den})"
    
    def simp(self):
        '''
        Return a simplified fraction by reducing the numerator and denominator
        '''
        num = Fraction(self.num)
        den = Fraction(self.den)
        while type(num) == Fraction or type(den) == Fraction:
            newself = num / den
            num = newself.num
            den = newself.den
        div = 0
        while div != 1:
            div = mindiv([num, den])
            num /= div
            den /= div
        if type(num) == float:
            num = int(num)
        if type(den) == float:
            den = int(den)
        newself = Fraction(num, den)
        return newself
    
    @property
    def value(self):
        '''
        The numerical value of this fraction as a floating point number
        '''
        num = self.num
        den = self.den
        if type(num) == Fraction:
            num = num.value
        if type(den) == Fraction:
            den = den.value
        return num/den
    
    def inv(self):
        '''
        The inverse of this fraction
        '''
        return Fraction(self.den, self.num)
    
    def is_integer(self):
        '''
        Return True if the fraction represents an integer
        '''
        return self.value.is_integer()
    
    def to_den(self, newden):
        '''
        Return a fraction with the given denominator and the same numerical value as self
        '''
        return Fraction(self.num*(newden/self.den), newden)
    
    def __int__(self):
        '''
        int(self)
        '''
        return int(self.value)
    
    def __float__(self):
        '''
        float(self)
        '''
        return float(self.value)
    
    def __bool__(self):
        '''
        True if self else False
        '''
        return self is not None
    
    def __abs__(self):
        '''
        abs(self)
        '''
        return Fraction(abs(self.num), abs(self.den))
    
    def __add__(self, value):
        '''
        Return self+value
        '''
        if type(value) != Fraction:
            value = Fraction(value*self.den, self.den)
        newden = mmc([self.den, value.den])
        newself = self.to_den(newden)
        value = value.to_den(newden)
        return Fraction(newself.num + value.num, newden)
    
    def __radd__(self, value):
        '''
        Return self+value
        '''
        return self + value
    
    def __sub__(self, value):
        '''
        Return self-value
        '''
        if type(value) != Fraction:
            value = Fraction(value*self.den, self.den)
        return self + Fraction(-value.num, value.den)
    
    def __rsub__(self, value):
        '''
        Return value-self
        '''
        if type(value) != Fraction:
            value = Fraction(value*self.den, self.den)
        return Fraction(value.num, value.den) - self
    
    def __mul__(self, value):
        '''
        Return self*value
        '''
        if type(value) != Fraction:
            value = Fraction(value)
        return Fraction(self.num*value.num, self.den*value.den)
    
    def __rmul__(self, value):
        '''
        Return value*self
        '''
        return self * value
    
    def __truediv__(self, value):
        '''
        Return self/value
        '''
        if type(value) != Fraction:
            value = Fraction(value)
        return Fraction(self.num*value.den, self.den*value.num)
    
    def __rtruediv__(self, value):
        '''
        Return value/self
        '''
        if type(value) != Fraction:
            value = Fraction(value)
        return Fraction(value.num*self.den, value.den*self.num)
    
    def __floordiv__(self, value):
        '''
        Return self//value
        '''
        return (self / value).__floor__()
    
    def __rfloordiv__(self, value):
        '''
        Return value//self
        '''
        return (value / self).__floor__()
    
    def __mod__(self, value):
        '''
        Return self%value
        '''
        return float(self) % float(value)
    
    def __rmod__(self, value):
        '''
        Return value%self
        '''
        return float(value) % float(self)
    
    def __divmod__(self, value):
        '''
        Return divmod(self, value)
        '''
        return divmod(self, value)
    
    def __rdivmod__(self, value):
        '''
        Return divmod(value, self)
        '''
        return divmod(value, self)
    
    def __pow__(self, value, mod=None):
        '''
        Return pow(self, value, mod)
        '''
        if value >= 0:
            result = Fraction(self.num**value, self.den**value)
        else:
            result = Fraction(self.den**abs(value), self.num**abs(value))
        if mod is None:
            return result
        else:
            return result % mod
    
    def __rpow__(self, value, mod=None):
        '''
        Return pow(value, self, mod)
        '''
        if mod is None:
            return value ** self.value
        else:
            return value ** self.value % mod
    
    def __round__(self, ndigits=None):
        '''
        Return the Integral closest to x, rounding half toward even.
        
        When an argument is passed, work like built-in round(x, ndigits):
        '''
        return round(self.value, ndigits)
    
    def __pos__(self):
        '''
        +self
        '''
        return self*1
    
    def __neg__(self):
        '''
        -self
        '''
        return self*(-1)
    
    def __floor__(self):
        '''
        Return the floor as an Integral
        '''
        val = self.value
        rnd = round(val)
        if rnd > val:
            return rnd-1
        else:
            return rnd
    
    def __ceil__(self):
        '''
        Return the ceiling as an Integral
        '''
        val = self.value
        rnd = round(val)
        if rnd < val:
            return rnd+1
        else:
            return rnd
    
    def __trunc__(self):
        '''
        Return the Integral closest to x between 0 and x
        '''
        return self.__floor__()
    
    def __eq__(self, value):
        '''
        Return self==value
        '''
        return float(self) == float(value)
    
    def __ne__(self, value):
        '''
        Return self!=value
        '''
        return not self == value
    
    def __lt__(self, value):
        '''
        Return self<value
        '''
        return float(self) < float(value)
    
    def __le__(self, value):
        '''
        Return self<=value
        '''
        return self < value or self == value
    
    def __gt__(self, value):
        '''
        Return self>value
        '''
        return float(self) > float(value)
    
    def __ge__(self, value):
        '''
        Return self>=value
        '''
        return self > value or self == value

