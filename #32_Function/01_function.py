
# Function is a block of code that only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

def greet():
    print("Hello, World!") # 
    print("Welcome to Python Programming")
    
    
greet() # Call the function

greet()

def add(a,b):
    c = a+b
    print(c)

add(5,4)



def add(a,b):
    c = a+b
    return c # return the value of c to the caller of the function 

result =  add(5,4)

print(result)




def add_sub(a,b):
    c = a+b
    d = a-b
    return c,d # return the value of c to the caller of the function

result1,result2 =  add_sub(5,4)

print(result1,result2)