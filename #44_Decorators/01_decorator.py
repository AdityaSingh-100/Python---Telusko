
#*  Decorators are used to modify the behavior of function or class.- It is a function that takes another function as an argument and returns a new function. 
# * Decorators are used to add extra features to the existing functions.
# * Decorators can change the behaviour of an existing function at the compile itself.



def div(a,b):
    print(a/b) 


def smart_div(func):
    
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    
    return inner


div = smart_div(div)

div(2,4)

