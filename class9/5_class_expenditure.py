#Create a class Expenditure and initialize it with expenditure,savings.Make the following methods.
#1. Display expenditure and savings
#2. Calculate total salary
#3. Display salary
class expenditure:
    def __init__(self,exp,saving):
        self.exp=exp
        self.saving=saving
    def calculate(self):
        self.sal=self.saving+self.exp
    def display(self):
        print("salary is : %f " % (self.sal))
        print("expenditure is : %f" % (self.exp))
        print("saving is : %f" % (self.saving))
e=int(input("enter your expenditure : "))
s=int(input("enter your saving : "))
e1=expenditure(e,s)
e1.calculate()
e1.display()