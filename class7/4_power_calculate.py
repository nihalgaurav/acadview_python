#Write a function to calculate power of a number raised to other ( a^b ) using recursion.
b=int(input("enter base : "))
p=int(input("enter power : "))
def power(x,y):
    return x**y
print(power(b,p))