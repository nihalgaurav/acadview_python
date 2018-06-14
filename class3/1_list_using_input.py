#create a list with a user define input
l=[4,'d','d',5]
#first method 
l[0]=int(input("enter first number :"))
l[1]=int(input("enter secound number :"))
l[2]=int(input("enter third number :"))
l[3]=int(input("enter fourth number :"))
#secound method (dynamic)
l.append(int(input("enter fifth number :")))
l.append(int(input("enter sixth number :")))
#printing final list
print(l)