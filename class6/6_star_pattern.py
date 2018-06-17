"""Print the following patterns:
*
**
***
****"""
for x in range(5):
    for y in range(x):
        print('*',end="")
    print('\n')