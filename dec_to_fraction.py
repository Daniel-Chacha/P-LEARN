from fractions import Fraction

dec=input('Enter a decimal number: ')
frac=Fraction(dec).limit_denominator()

print(dec)
print(frac)