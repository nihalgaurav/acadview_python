#Create a threading process such that it sleeps for 5 seconds and then prints out a message.
import threading
from threading import Thread
import time

def message():
    time.sleep(5)
    print("hello python")

t= Thread (target=message)
t.start()