 # Create a user defined dictionary and get keys corresponding to the value using for loop.
d={}
key=""
value=""
for x in range(5):
    key=input("enter %d th key : "%(x))
    value=input("enter %d th value : "%(x))
    d[key]=value
print(d)
for key in d.keys():
    print(d[key],key)
