#From a list containing ints, strings and floats, make three lists to store them
l=[1,'a',5,'d',4.5,'r',5.3]
i=[]
c=[]
f=[]
for x in l:
        if type(x)==int:
            i.append(x)
        elif type(x)==str:
            c.append(x)
        elif type(x)==float:
            f.append(x)
print(l)
print(i)
print(c)
print(f)