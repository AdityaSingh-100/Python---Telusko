'''
Basic User Input 

x = input("Enter 1st number:")
print(type(x)) # <class 'str'>
a = int(x)

y = input("Enter 2nd number:")
print(type(y)) # <class 'str'>
b = int(y)  

z = a + b
print(z) # concatenation of x and y

'''

#NOTE - OR reducing LOC

x = int(input("Enter 1st number:"))
y = int(input("Enter 2nd number:"))
z = x + y
print(z) 

# For character input
ch = input("Enter a character:")
print(ch) # a

print(ch[0])

# OR
ch = input("Enter a character:")[0]

print(ch)


# eval() - evaluates the string expression directly
result = eval(input("Enter an expression:"))
print(result) # 8

