import calc
#*  __name__ is a special variable in Python that is used to check if the code is being run from the same file or not.
# If the code is being run from the same file, the value of __name__ is __main__.
# If the code is being run from a different file, the value of __name__ is the name of the file.

# if we import cal from another file, the value of __name__ will be the name of the file.


# print("specVar says: " + __name__) # Output: __name__
print(__name__)

def main():
    print("Hello")
    print("welcome user")

if __name__ == "__main__":
    main()
    
    
    
'''
1-They are two modules name demo and calc 
2- when you are working on demo and print(_name )
Output- _main_(because it is starting point of a code)
3- Now we will work on calc and print hello name
Output- hello main 
This is happening and it is giving name as main output because we are working on same module 

Now when we import one module to other ( import calc to demo)
1- All the things in calc will be printed along with demo statements
2- but it will print hello calc (the module name )
Instead of hello main 
Because we are importing it to other module 
"sooo when you are importing it in same module it will give name output as main 
And if in other module it will give name output along with module name...... that's it
'''