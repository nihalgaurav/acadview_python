#Create a Student class and initialize it with name and roll number. Make methods to :
#1. Display - It should display all informations of the student.
class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def display(self):
        print("name : ",self.name)
        print("roll number : ",self.roll)
n = input("enter name of the student : ")
r = int(input("enter roll nuber : "))
s = student(n,r)
s.display()