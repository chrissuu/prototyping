from math import comb
from math import gcd

from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        common_gcd = gcd(numerator, denominator)
        self.numerator = numerator // common_gcd
        self.denominator = denominator // common_gcd

    def __add__(self, other):
        if isinstance(other, Fraction):
            common_denominator = self.denominator * other.denominator
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            return Fraction(new_numerator, common_denominator)
        else:
            raise TypeError("Can only add another Fraction.")
    
    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Can only multiply by another Fraction.")
    
    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero fraction.")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Can only divide by another Fraction.")
    
    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"
    
def p(y_1, y_2):

    return Fraction(comb(4, y_1) * comb(3, y_2) * comb(2, 3-y_1-y_2), comb(9,3))

print(p(1,0) + p(1,1) + p(1,2) + Fraction(2, 1) * (p(2,0) + p(2,1)) + Fraction(3, 1) * p(3,0))

print(p(0,1) + p(1,1) + p(2,1) + Fraction(2, 1) * (p(0,2) + p(1,2)) + Fraction(3, 1) * p(0,3))