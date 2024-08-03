
# MultiThreading in Python
# MultiThreading is a way to achieve multitasking. 
# We can execute multiple threads in a single process.
# Python has a multi-threading package but if you want to multi-thread to speed your code up, then it's usually not a good idea to use it.
# Python has a construct called the Global Interpreter Lock (GIL). The GIL makes sure that only one of your 'threads' can execute at any one time.
# A thread acquires the GIL, does a little work, then passes the GIL onto the next thread.
# This happens very quickly so to the human eye it may seem like your threads are executing in parallel, but they are really just taking turns using the same CPU core.
# If you want your code to run faster then use the multiprocessing package.
# Multi-threading is particularly useful when you have to perform I/O bound tasks.
 
from time import sleep # sleep is a function in time module

from threading import * #  means import everything from threading module

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1) # sleep for 1 second - it will pause the execution of the thread for 1 second
    

t1 = Hello()
t2 = Hi()

t1.start() # start() is a method of Thread class - it will call run() method

sleep(0.2) # sleep for 0.2 second

t2.start()

t1.join() # join() is a method of Thread class - it will wait for the thread to finish its execution
t2.join() # it will wait for the thread to finish its execution

print("Bye") # main thread will execute this line of code
