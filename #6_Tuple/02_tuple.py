tup = (21,36,14,25)
print(tup)

print(tup[1])

# tup[1] = 77 # TypeError: 'tuple' object does not support item asp.index(2)gnment or we cant change the value of tuple

tup.count(21) # count is used to count the number of times a value is present in the tuple
tup.index(21) # index is used to find the index of a value in the tuple 

#set = s
s = {22,25,14,21,5}
print(s)

s = {25,14,98,63,75,98}
print(s) # set does not allow duplicate values

# s[2] # TypeError: 'set' object does not support indexing

s.add(45) # add is used to add a value in the set
print(s)

   
# Correct usage of intersection method with assignment
s = {25, 14, 98, 63, 75, 98}
# Defining other sets to intersect with
set1 = {25, 14, 98}
set2 = {63, 75, 98}

# Finding the intersection of s with set1 and set2, and printing the result
intersection_result = s.intersection(set1, set2)
print(intersection_result)  # This will print the common elements among s, set1, and set2