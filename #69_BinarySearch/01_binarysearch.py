

# Binary Search
# 4 7 8 12 45 99
# low = 0
# high = 5
# mid = (0+5)/2 = 2 (int value) - 8

# if 8 is not equal to 45 

'''
step 1 - set the lowerBound and upperBound
step 2 - find a min index i.e lowerBound + upperBound / 2
step 3 - now we have to check that the mid value is same or not with the value we are seaching for
step 4 - next change your lowerBound or upperBound
     4.1 - the value we are searching for is smaller or bigger than the mid value
     4.1.1 - if your value is smaller change the upperBound to midindex
     4.1.2 - if your value is bigger change the lowerBound to midindex
step 5 - again find a mid value
'''
pos = -1

def search(list,n):
    
    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1 
            else:
                u = mid - 1
    return False


list = [4, 7, 8, 12, 45, 99]

n = 2

if search(list,n):
    print("Found at",pos+1)
else:
    print("Not Found")