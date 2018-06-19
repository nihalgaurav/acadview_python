#Find the GCD of a number input by user using math package functions.
import math
x=int(input("input first number for gcd :"))
y=int(input("input second number for gcd :"))
print("gcd of number %d and %d is :" % (x,y))
print(math.gcd(x,y))