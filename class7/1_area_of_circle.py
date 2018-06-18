#Create a function to calculate the area of a circle by taking radius from user.
pi=3.14
rad=int(input("enter the radius of the circle : "))
def area(r):
    return (pi*r*r)
print("area of the circle is : ",str(area(rad)))