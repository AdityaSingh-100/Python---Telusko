
#* Anonymous function - lambda - is a small, anonymous function that can have any number of arguments, but can only have one expression.

#* functiion are objects in python, so we can assign them to variables and pass them as arguments to other functions.



f = lambda a : a * a

# def square(a):
#     return a*a




result = f(5)

print(result)



print("------------------")





f = lambda a,b : a + b


result = f(5,6)

print(result)