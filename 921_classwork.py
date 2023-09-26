class LongFloat():
    def __init__(self, sig_digits, exp):
        self.exp = exp
        self.sig_digits = sig_digits * 10 ** self.exp

    #def print(self, string):
	#print(self.sig_digits * 10 ** self.exp)

    def to_longfloat(self,other):
        if isinstance(other, LongFloat):
            return other
        elif isinstance(other, float):
            return LongFloat(other, self.exp)
            
    def __add__(self, other):
        other = self.to_longfloat(other)
        sig = self.sig_digits + other.sig_digits
        #exp = self.exp
        return LongFloat(sig, 1)
    
    def __sub__(self, other):
        other = self.to_longfloat(other)
        sig = self.sig_digits - other.sig_digits
        #exp = self.exp
        return LongFloat(sig, 1)
        
    def __mul__(self, other):
        other = self.to_longfloat(other)
        sig = self.sig_digits * other.sig_digits
        #exp = self.exp
        return LongFloat(sig, 1)
        
    def __truediv__(self, other):
        other = self.to_longfloat(other)
        sig = self.sig_digits / other.sig_digits
        #exp = self.exp
        return LongFloat(sig, 1)
    
lf1 = LongFloat(3.14, 20)  # Creates a LongFloat instance with sig_digits=3.14 and exp=2
lf2 = LongFloat(2.718, 10)  # Creates another LongFloat instance

result_add = lf1 + lf2  # Adds the two LongFloat instances
result_sub = lf1 - lf2 
result_mul = lf1 * lf2  
result_div = lf1 / lf2

print(result_add.sig_digits)  # Print the result's sig_digits
print(result_sub.sig_digits)
print(result_mul.sig_digits)
print(result_div.sig_digits)


