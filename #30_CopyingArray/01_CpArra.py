from numpy import * 

arr = array([1,2,3,4,5])
arr1 = array([1,2,3,4,5])
arr2= array([1,2,3,4,5])

# arr = arr + 5
arr3 = arr1 + arr2

print(arr) 
print(arr3)

print(sin(arr))
print(log(arr))
print(sqrt(arr))
print(sum(arr))
print(min(arr))
print(max(arr))
print(sort(arr))

# concatenate two arrays
print(concatenate([arr1,arr2]))


# Copy array

arr4 = array([2,4,6,8,10])

arr5 = arr4

print(arr4)
print(arr5)

print(id(arr4))
print(id(arr5))

# View function
arr6 = arr4.view()
# View function is used to create a new array with the same data
print(id(arr4))
print(id(arr6))

# Shallow copy And Deep copy
# Shallow copy is copy data to another array but if we change the data in one array it will also change in another array
arr4[1] = 5

print(arr4)
print(arr6)
# Both value has been changed because of shallow copy

# Deep Copy is used to copy the data to another array but if we change the data in one array it will not change in another array

arr7 = arr4.copy() # Copy function is used to create a deep copy of the array

arr4[1] = 4
print(arr4)
print(arr7)