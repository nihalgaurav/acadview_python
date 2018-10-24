#counting odd and even number in list
l=[1,2,3,4,5,6,7,8,9]			#list of even and odd numbers
odd=0
even=0
for x in l:
	if x%2==0:
		even+=1			#count the even no
	else:
		odd=odd+1		#count the odd no
print("number of odd numbers in the list is :"+str(odd))		
print("number of even numbers in the list is :"+str(even))
