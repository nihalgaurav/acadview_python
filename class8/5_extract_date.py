#Extract date (ex : 11 in 11/01/2021) from the time.
import time
t=time.gmtime()
print("time is :",time.ctime())
date=t[2]
print("the date is :",str(date),end="\t")