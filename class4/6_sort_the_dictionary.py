d={}
name=""
marks=""
l=[]
for x in range(10):
	name=input("enter name of the student : ")
	marks=int(input("enter marks of the student : "))
	l.append(marks)
	d[name]=marks
print("dictionary is : ")
print(d)
print(l)
l.sort()
print(l)