# 1) Print this 
'''1 2 3 4
   2 3 4
   3 4
   4
'''

for i in range(4):   # This denotes row in the output
    for j in range(i+1,5):  # This denotes column in the output 
        print(j,end=" ")
        
    print()