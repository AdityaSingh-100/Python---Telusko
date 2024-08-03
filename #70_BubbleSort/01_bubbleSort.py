
# Bubble Sort
# Comparing and swapping adjacent elements if they are in the wrong order'
# 2 loops - outer loop for the number of passes and inner loop for the number of comparisons

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums = [5, 3, 8, 6, 7, 2]
sort(nums)

print(nums)