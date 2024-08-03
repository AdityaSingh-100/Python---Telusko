

a = 5
b = 6

print(a+b)

int.__add__(a,b) # This is how the + operator works
print(int.__add__(a,b))
print(int.__sub__(a,b))
print(int.__mul__(a,b))
print(int.__truediv__(a,b))
print(int.__floordiv__(a,b))
print(int.__mod__(a,b))
print(int.__pow__(a,b))
print(int.__lt__(a,b))
print(int.__le__(a,b))
print(int.__eq__(a,b))



c = '5'
d = '6'

print(c+d)

print(str.__add__(c,d))