#Print multiplication table of 12 using recursion.
def table(n):
    if n>10:
        return
    else:
        print(12*n)
        table(n+1)
table(1)