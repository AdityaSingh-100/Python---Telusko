 
def add(a,b):
   c= a+b
   print(c)
   
   
   
add(5,6)


# Formal arguments - Arguments which are passed in the function definition are called formal arguments.

print('------------------')
# Actual arguments - Arguments which are passed in the function call are called actual arguments.
# actual arguments are of four types:
# 1. Positional arguments
# 2. Keyword arguments
# 3. Default arguments
# 4. Variable-length arguments

# Positional arguments - The arguments which are passed in the function call in the same order as they are defined in the function definition are called positional arguments.

 
def add(name,age):
   print(name)
   print(age-5)
   
   
   
add('Aditya',20) # position
add(age= 20,name='Aditya') # Keyword


print('------------------')
# Default arguments - The arguments which are passed in the function call are called default arguments.
def add(name,age = 18):
   print(name)
   print(age)
   
   
add('Aditya')


print('------------------')
 
 
 
# Variable-length arguments - The arguments which are passed in the function call are called variable-length arguments.
 
 
def sum(a,*b):  # * is used to pass multiple arguments
    # c= a+b
#    print(a)
#    print(b)
   
   c = a
   
   for i in b:
       
       c = c+i
        
   print(c) # Will print the sum of all the arguments passed that are list and tuple type 
   
   
   
sum(5,6,34,78)


print('------------------')
print('OR')



def sum(*b):  # * is used to pass multiple arguments
    # c= a+b
#    print(a)
#    print(b)
   
   c = 0
   
   for i in b:
       
       c = c+i
        
   print(c) # Will print the sum of all the arguments passed that are list and tuple type 
   
   
   
sum(5,6,34,78)