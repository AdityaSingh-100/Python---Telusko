from numpy import * 

arr1 = array([
               
               [1,2,3,6,2,9],
               
               [4,5,6,7,5,3]
              
    
            ])

print(arr1.dtype)
print(arr1.ndim) # ndim is used to find the dimension of the array
print(arr1.shape) # shape is used to find the shape of the array - give no of rows and columns
print(arr1.size) # size is used to find the size of the array - total no of elements in the array

arr2 = arr1.flatten() # flatten is used to convert the 2D array into 1D array
print(arr2)

arr3 =arr2.reshape(3,4) # reshape is used to convert the 1D array into 2D array
print(arr3)

arr3 = arr2.reshape(2,2,3)
print(arr3)
