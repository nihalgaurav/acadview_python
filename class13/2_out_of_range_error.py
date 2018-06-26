# Name and handle the exception occurred in the following program:
# l=[1,2,3]
# print(l[3])
try:
    l=[1,2,3]
    print(l[3])#index 3 is out of range as l has max index 2

except Exception as e:
    print(e)