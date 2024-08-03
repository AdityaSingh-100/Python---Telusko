# 2) write a code to reverse an array without using in-built function.

# reversed() returns an iterator that allows you to traverse the list in reverse order, but it doesn't directly give you a reversed list or array. To print the reversed array, you can convert the iterator to a list first. Here’s the corrected code
from array import *

# arr = array('i',[2,3,4,5,6,7,8,9])


# print(list(reversed(arr)))


arr = array('u',['a','b','c','d'])
#
len = len(arr)
arr1 = array(arr.typecode,[]) # new array to store reversed array
#
i = 1
while i <= len:
    arr1.append(arr[4-i])
    i+=1
print(arr1)

#collection[start:stop:step]
#collection denotes the data collection (list, string, array, and so on).
# start denotes where the slicing operation should start from.
# stop denotes where the operation should stop.
# step denotes the sequence of iterating through the elements.
print(arr[::-1 ])