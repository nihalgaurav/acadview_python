# Write a program to show and handle following exceptions:
# 1. Import Error
# 2. Value Error
# 3. Index Error
# outer_import_2.7.py

#1. Import error

try:
    import sys
    import gw_utility.Book
except Exception as e:
    print(e)

#2.Value Errror

try:
    number = int("hello")

except ValueError as f:
    print (f,"\tEnter numbers only")

#3. Index Error

l=[5,6,8]
try:
    print(l[5])
except Exception as e:
    print(e)

