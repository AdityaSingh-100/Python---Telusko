from array import *

arr = array('i',[])

n = int(input("Enter the lenght of the array"))

for i in range(n):
    x = int(input("Enter the values"))
    arr.append(x)
    
print(arr) 

val = int(input("Enter the value to search"))

k = 0

for e in arr:
    if e == val:
         print(k)
         break 
    k += 1
    
    
# or using function

print(arr.index(val))