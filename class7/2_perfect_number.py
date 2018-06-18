#Write a function “perfect()” that determines if parameter \
# number is a perfect number. Use this function in a program that\
#  determines and prints all the perfect numbers between 1 and 1000.
p=[]
def perfect():
    for x in range(1,1000):
        l=[]
        s=0
        for y in range(1,x):
            if x%y==0:
                l.append(y)
        for a in l:
            s=s+a
        if s==x:
            p.append(x)
perfect()
print(p)