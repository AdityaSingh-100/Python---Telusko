# 1) Write a code to print all values from 1 to 100 and skip the number which are divisible by 3 and 5

i = 1

while i<100 :
    if i % 3 != 0 and i % 5 != 0:
        print(i)
    i += 1
    
