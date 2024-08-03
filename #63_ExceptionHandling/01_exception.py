

# Exception Handling in Python
# Exceptions are errors that occur during the execution of a program.
# They disrupt the normal flow of the program and are usually unexpected.
# Exceptions in Python are objects that represent errors.


# Compiler time error - Syntax error
# Run time error - Logical error


a = 5
b = 2

try:
    print("Resource Open")
    print(a/b) # jumps to except block
    
    k = int(input("Enter a number: "))
    print(k)

        
except ZeroDivisionError as e:
    print("Hey,You cannot divide a number by zero",e)
    
    
except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something went wrong")
    
finally: # finally block will executed if we get error as we as if we don't get error
    print("Resource Closed")
