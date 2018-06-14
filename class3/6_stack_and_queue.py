#implement stack and queue using list
l=[]

#implementing list like stack
print("pushing element onto the stack")
l.append(int(input("enter first element")))
print(l)
l.append(int(input("enter second element")))
print(l)
l.append(int(input("enter third element")))
print(l)
l.append(int(input("enter forth element")))
print(l)
l.append(int(input("enter fifth element")))
print(l)
#poping elements  from the stack
print("number poped "+str(l.pop())+"  "+str(l))
print("number poped "+str(l.pop())+"  "+str(l))
print("number poped "+str(l.pop())+"  "+str(l))
print("number poped "+str(l.pop())+"  "+str(l))
print("number poped "+str(l.pop())+"  "+str(l))

#implementing list like queue
print("")
print("\n adding element in the queue")
l.append(int(input("enter first element")))
print(l)
l.append(int(input("enter second element")))
print(l)
l.append(int(input("enter third element")))
print(l)
l.append(int(input("enter forth element")))
print(l)
l.append(int(input("enter fifth element")))
print(l)
#removing element from the queue
del l[0]
print("removing element "+str(l))
del l[0]
print("removing element "+str(l))
del l[0]
print("removing element "+str(l))
del l[0]
print("removing element "+str(l))
del l[0]
print("removing element "+str(l))