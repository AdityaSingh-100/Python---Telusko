
 
a = 10 # Global variable - can be accessed from anywhere in the program - outside the function


def something():
    # a = 15      # Local variable - can be accessed only within the function where it is defined - inside the function
    # b = 8 
    global b # to change the value of global variable inside the function, we need to use global keyword  
    a = 15 
    print("in func",a) # 15
    
    a = 9
    
    
    
something()




# print(b) # NameError: name 'b' is not defined   

print("outside funct",a) # 10



print("----------------------------------")






a = 10 # Global variable - can be accessed from anywhere in the program - outside the function
print(id(a))

def something():
    a = 9
    
    x = globals()['a'] # to access the global variable inside the function, we can use globals() function
    print(id(x))
    print("in func",a) 
    
    
    globals()['a'] = 15 #* to change the value of global variable inside the function, we can use globals() function
    
    print(a)
    
something()




# print(b) # NameError: name 'b' is not defined   

print("outside funct",a) # 10