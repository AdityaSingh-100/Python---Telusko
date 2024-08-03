from array import *

arr = array('i',[2,5,1,6,4,8,3,7,9])

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[i]>arr[i+j+1]:
            arr[i],arr[i+j+1]=arr[i+j+1],arr[i]

print(arr)