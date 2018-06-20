#Create a circle class and initialize it with radius. Make two methods \
# getArea and getCircumference inside this class.
class circle:
    def __init__(self,rad):
        self.rad = rad
    def area(self):
        self.area=(3.14 * self.rad * self.rad)
        print("area is : ",str(self.area))

    def circumference(self):
        self.cir = (2*3.14*self.rad)
        print("circumference is : ",str(self.cir))
r=int(input("enter radius : "))
c=circle(r)
c.area()
c.circumference()