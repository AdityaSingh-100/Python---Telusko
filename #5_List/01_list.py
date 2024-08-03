nums = [25,12,36,95,14]
print(nums)

print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[4])


print(nums[2:])

print(nums[-1])
print(nums[-5])


names = ['Aditya', 'Eren', 'Goku']
print(names)

values = [9.5, 'Aditya', 25]
print(values)

mil = [nums, names] # list inside a list
nums.append(45)
print(mil) # add 45 in end of nums list

nums.insert(2, 77) # insert is used to add a value at a specific index
print(mil)


nums.remove(14) # remove is used to remove a value from the list
print(mil)

nums.pop(1) # pop is used to remove a value from the list using index
print(mil) 

del nums[2:] # del is used to remove a value from the list using index
print(nums)

nums.extend([29, 12, 14, 36]) # extend is used to add multiple values in the list
print(nums)

print(max(nums))

print(min(nums))

print(sum(nums))

nums.sort() # sort is used to sort the list in ascending order
print(nums)  