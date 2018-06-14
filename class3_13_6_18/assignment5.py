#given are two 1-dimentional array a and b which are sorted in assending order 
#write the prog to merge them into a single sorted array c that 
#contains every item from array a and b in assending order []list
a=[10,50,42,89,21,8]
b=[52,42,18,65,94,1]
print("array a is :")
print(a)
print("array b is :")
print(b)
#shorting array a
a.sort()
#sorting array b
b.sort()
#merging array a and b
c=(a+b)
#sorting c
c.sort()
print("array a+b after sorting")
print(c)