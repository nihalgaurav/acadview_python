#Create a class Shape.Initialize it with length and breadth Create the method Area.\
#  Create class rectangle and square which inherits shape and access the method Area.
class shape:
    def __init__(self):
        self.length=0
        self.width=0

class rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def arae(self):
        a=self.length*self.width
        print("area of the rectangle is : ",a)

class square(shape):
    def __init__(self,side):
        self.length=side
        self.width=side
    def area(self):
        a=self.length*self.width
        print("area of square  is : ",a)

s1=square(5)
s1.area()
r1=rectangle(5,10)
r1.arae()