#Take inputs from user to make a list. Again take one input from user and search it in the\
#  list and delete that element, if found. Iterate over list using for loop.
l=[]
for x in range(5):
    l.append(input("input %d element of list : " % (x)))
s=input("input the element you want to search in the list : ")
print(l)
for x in l:
    if x==s:
        print("elemnet is found , deleting elemnet ")
        l.remove(s)
print(l)