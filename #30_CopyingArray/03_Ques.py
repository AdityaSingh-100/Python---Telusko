# 2) Write a code to find the maximum value from an array without using built in function

from numpy import *

arr = array([3,4,2,7,9,11])

max_value = 0
for i in range(len(arr)):
        if(arr[i] >max_value ):
            max_value = arr[i]
print(max_value)