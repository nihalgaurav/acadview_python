#Extract day from the time.
import time
t=time.gmtime()
print("time is :",time.ctime())
day=t[6]
print("the day is :",str(day),end="\t")
if day==0:
    print("monday")
elif day==1:
    print("tuesday")
elif day==2:
    print("wednesday")
elif day==3:
    print("thursday")
elif day==4:
    print("friday")
elif day==5:
    print("saturday")
elif day==6:
    print("sunday")