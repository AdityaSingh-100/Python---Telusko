from array import *

vals = array('L',[5,9,8,4,2])

print(vals.buffer_info())
# buufer_info() returns the address and size of the array
print(vals.typecode)
# typecode returns the type of the array
vals.reverse()
print(vals)
# reverse() reverses the array

print(vals[0])
# prints the element at index 0
for i in  range(5):
    print(vals[i])
    
print()
# if we dont know the size/lenght of the array
for i in range(len(vals)):
    print(vals[i])
    
print()

#more dynamic way
for e in vals:
    print(e)
    
print()
# Creating a new array from an existing array and copying the values into the new array
values = array('i',[5,9,8,4,2])

newArr = array(values.typecode, (a for a in values))

for e in newArr:
    print(e)    
    
print()

# square of the elements of the array
values = array('i',[5,9,8,4,2])

newArr = array(values.typecode, (a*a for a in values))

for e in newArr:
    print(e)    
    
print()


# using while loop
values = array('i',[5,9,8,4,2])

newArr = array(values.typecode, (a for a in values))

i = 0

while i<len(newArr):
    print(newArr[i])
    i+=1