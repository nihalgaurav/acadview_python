#Extract month from the time.
import time
t=time.gmtime()
print("time is :",time.ctime())
print("the month is :",str(t[1]))