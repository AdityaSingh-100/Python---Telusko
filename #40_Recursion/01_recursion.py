# Recursion - A function that calls itself is called a recursive function 


import sys

# To increase the recursion limit
sys.setrecursionlimit(2000)  # This will increase the recursion limit to 2000

print(sys.getrecursionlimit())  # 1000 - This is the default recursion limit in Python


i = 0

def greet():
    global i
    i += 1
    print("Hello",i)
    greet()          # This will cause an infinite loop, because the function is calling itself 
    
    
    
    
    
greet()