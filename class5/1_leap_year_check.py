#Take an input year from user and decide whether it is a leap year or not. 
year=int(input("enter a year for leap year check : "))
if year%4==0:
	print("entered year is leap year ")
else:
	print("entered year is not a leap year ")