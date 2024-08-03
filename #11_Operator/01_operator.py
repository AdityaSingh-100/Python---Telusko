''' Arithmatic Operator '''
x = 2
y = 3 
print(x + y) # 5
print(x - y) # -1
print(x * y) # 6
print(x / y) # 0.6666666666666666  
print(x % y) # 2

x = x + 2
print (x) # 4   

x *= 3
print(x) # 12

a,b = 5,6
print(a,b) # 5 6

''' Unary Operator '''
n = 7
print(-n) # -7

n = -n
print(n) # 7

''' Relational Operator '''

a,b = 10,20
print(a < b) # True
print(a > b) # False
print(a <= b) # True
print(a >= b) # False
print(a == b) # False

a,b = 6, 6
print(a == b) # True

#NOTE - != is not equal to operator
print(a != b) # False

''' Logical Operator '''
a , b = 5,4
# And Operator - Both condition should be true

print(a < 8 and b < 5) # True

print(a < 8 and b < 4) # False

# Or Operator - Any one condition should be true

print(a < 8 or b < 4) # True

print(a > 9 or b < 3) # False

# Not Operator - Reverse the result

x = True
print(not x) # False

''' Bitwise Operator '''
#! Bitwise Operator works on bits and perform bit by bit operation
a,b = 10,4
print(a & b) # 0

print(a | b) # 14

print(a ^ b) # 14

print(~a) # -11

print(a << 2) # 40

print(a >> 2) # 2