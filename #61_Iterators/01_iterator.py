

nums = [7,8,9,5]


# for i in nums:
    
#     print(i) 
    
    
# Iterating over a list using for loop is easy and readable.

it = iter(nums) # iter() function returns an iterator object

print(it.__next__())

print(next(it)) # next() function returns the next item from the iterator

for i in nums:
    print(i)