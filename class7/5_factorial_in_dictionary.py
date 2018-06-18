#Write a function to find factorial of a\
#  number but also store the factorials calculated in a dictionary
def fact(x):
    if x==1:
        return 1
    else:
        x=x*fact(x-1)
        return x
n=int(input("enter the number : "))
f=fact(n)
print(f)
d={}
d[n]=f
print(d)