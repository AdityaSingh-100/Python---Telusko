# 1) Print this pattern
'''
A P Q R
A B Q R
A B C R
A B C D

'''
a = "ABCD"
b = "PQR"
for i in range(4):
    print(a[:i+1]+ b[i:])
    
name = "Aditya"
#       012345
print(name[3:])
# [Start:Ending]