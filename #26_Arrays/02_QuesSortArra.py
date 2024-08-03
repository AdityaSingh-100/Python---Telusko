# 1) Write a code to sort an array in ascending order

from array import *

vals = array('i',[2,8,4,6,3,9])

print(sorted(vals))


'''
2nd Approach
from array import *
arr=array('i',[4,3,1,2,5,23,45,56,12,7,9])

for i in range(len(arr)):
    for j in range(len(arr)-i-1) :
        if arr[i]>arr[i+j+1] :
            arr[i],arr[i+j+1]=arr[i+j+1],arr[i]

print(arr)'''