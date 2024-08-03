num = 5

#NOTE - 1 To get num address we can use id() function
id(num)
print(id(num))

name = 'Aditya'
print(id(name))

#NOTE - 2
a = 10
b = 10
print(a)
print(b)

id(a)
print(id(a))

id(b)
print(id(b))  #NOTE - Both a and b have same address points to same box which contain 10 which make it memory efficient

print(id(10))

k = 10
id(k)
print(id(k))

a = 9
id(a)
print(id(a)) # Now id will be different because that container is now containing different values

print(id(b))

b = 8
PI = 3.14 
print(PI)

#NOTE - Type of Variable

type(PI)
print(type(PI))

print(type(a))