#Write a function to calculate power of a number raised to other ( a^b ) using recursion.
b=int(input("enter base : "))
p=int(input("enter power : "))
def power(x,y):
    if y==1:
        return x
    else:
        s=x*power(x,y-1)
        return s
print(power(b,p))