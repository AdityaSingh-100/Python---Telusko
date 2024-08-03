import math as m

x = int(input("Enter a number:"))

print(m.factorial(x))

# Without prebuild function


num = int(input("Enter a number"))

# n! = n*(n-1) ..
# 3! = 3*2*1

factorial = 1
if num < 0:
    print("Factorial doesn't exist for negative number")
    
elif num ==0:
    print("Factorial of 0 is 1")
    
else :
    for i in range(1,num+1):
        factorial = factorial*i
    print("The factorial of",num,"is",factorial)
