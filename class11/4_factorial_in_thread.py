#Call factorial function using thread.

import threading
from threading import Thread
import time
import math

def factorial(n):
    fact=1
    for x in range(1,n+1):
        fact=fact*x
    print("factorial is : ",fact)

n=int(input("enter the number you want to find factorial :"))
t=Thread(target=factorial,args=(n,))
t.start()