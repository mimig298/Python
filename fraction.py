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

def dvs(num):
    divs = []
    for x in range(1, int(abs(num/2))+1):
        if x > num/2:
            break
        if x in divs:
            break
        if num % x == 0:
            divs.append(x)
            if not int(num/x) in divs:
                divs.append(int(num/x))
    if not num in divs:
        divs.append(num)
    return sorted(divs)

def mmc(nums):
    mults = []
    for num in nums:
        mult = []
        x = 0
        while x*num < mlt(nums):
            x += 1
            mult.append(x*num)
        mults.append(mult)
    curr = mults[0]
    for mult in mults[1:]:
        curr = common(curr, mult)
    if len(curr) == 0:
        return mlt(nums)
    return min(curr)

def mdc(nums):
    divs = []
    for num in nums:
        divs.append(dvs(num))
    curr = divs[0]
    for div in divs[1:]:
        curr = common(curr, div)
    if len(curr) == 0:
        return 1
    return max(curr)

class fraction():
    def __init__(self, num, den=1):
        if type(num) == fraction and den == 1:
            self.num = num.num
            self.den = num.den
        else:
            if not den.is_integer() and type(den) != fraction:
                den = fraction(den)
            if not num.is_integer() and type(num) != fraction:
                newnum = 0.1
                mult = 0
                while not newnum.is_integer():
                    mult += 1
                    newnum = num*(10**mult)
                num = fraction(int(newnum), 10**mult).simp()
            self.num = num
            self.den = den
    
    def __repr__(self):
        return f"({self.num}/{self.den})"
    
    def simp(self):
        
        div = mdc([self.num, self.den])
        newself = fraction(self.num/div, self.den/div)
        if newself.den == 1:
            newself = newself.num
        return newself
    
    def value(self):
        num = self.num
        den = self.den
        if type(num) == fraction:
            num = num.value()
        if type(den) == fraction:
            den = den.value()
        return num/den
    
    def is_integer(self):
        return self.value().is_integer()
    
    def to_den(self, newden):
        return fraction(self.num*(newden/self.den), newden)
    
    def __int__(self):
        return int(self.value())
    
    def __float__(self):
        return float(self.value())
    
    def __abs__(self):
        return fraction(abs(self.num), abs(self.den))
    
    def __add__(self, other):
        if type(other) != fraction:
            other = fraction(other*self.den, self.den)
        newden = mmc([self.den, other.den])
        newself = self.to_den(newden)
        other = other.to_den(newden)
        return fraction(newself.num + other.num, newden)
    
    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        if type(other) != fraction:
            other = fraction(other*self.den, self.den)
        return self + fraction(-other.num, other.den)
    
    def __rsub__(self, other):
        if type(other) != fraction:
            other = fraction(other*self.den, self.den)
        return fraction(other.num, other.den) - self
    
    def __mul__(self, other):
        if type(other) != fraction:
            other = fraction(other)
        return fraction(self.num*other.num, self.den*other.den)
    
    def __rmul__(self, other):
        return self * other
    
    def __truediv__(self, other):
        if type(other) != fraction:
            other = fraction(other)
        return fraction(self.num*other.den, self.den*other.num)
    
    def __rtruediv__(self, other):
        if type(other) != fraction:
            other = fraction(other)
        return fraction(other.num*self.den, other.den*self.num)
    
    def __floordiv__(self, other):
        return (self / other).__floor__()
    
    def __rfloordiv__(self, other):
        return (other / self).__floor__()
    
    def __mod__(self, other):
        return float(self) % float(other)
    
    def __rmod__(self, other):
        return float(other) % float(self)
    
    def __pow__(self, other):
        return fraction(self.num**other, self.den**other)
    
    def __rpow__(self, other):
        return other ** self.value()
    
    def __round__(self, ndigits=None):
        return round(self.value(), ndigits)
    
    def __pos__(self):
        return self*1
    
    def __neg__(self):
        return self*(-1)
    
    def __floor__(self):
        val = self.value()
        rnd = round(val)
        if rnd > val:
            return rnd-1
        else:
            return rnd
    
    def __ceil__(self):
        val = self.value()
        rnd = round(val)
        if rnd < val:
            return rnd+1
        else:
            return rnd
    
    def __trunc__(self):
        return self.__floor__()
    
    def __eq__(self, other):
        return float(self) == float(other)
    
    def __ne__(self, other):
        return not self == other
    
    def __lt__(self, other):
        return float(self) < float(other)
    
    def __le__(self, other):
        return self < other or self == other
    
    def __gt__(self, other):
        return float(self) > float(other)
    
    def __ge__(self, other):
        return self > other or self == other
